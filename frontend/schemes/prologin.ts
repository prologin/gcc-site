import qs from "querystring";
import axios from "axios";
import bodyParser from "body-parser";
import defu from "defu";
import type {
  StrategyOptions,
  ProviderOptions,
  ProviderPartialOptions,
  Oauth2SchemeOptions
} from '@nuxt-auth/types';

// From https://github.com/nuxt-community/auth-module/blob/dfbbb540c5e6c1f0bff0b356c46f50d48ee3f9a5/src/utils/provider.ts
function assignDefaults<SOptions extends StrategyOptions>(
  strategy: SOptions,
  defaults: SOptions
): void {
  Object.assign(strategy, defu(strategy, defaults))
}

// From https://github.com/nuxt-community/auth-module/blob/dfbbb540c5e6c1f0bff0b356c46f50d48ee3f9a5/src/utils/provider.ts
function addAuthorize<SOptions extends StrategyOptions<Oauth2SchemeOptions>>(
  nuxt: any,
  strategy: SOptions,
  useForms = false
): void {
  // Get clientSecret, clientId, endpoints.token and audience
  const clientSecret = strategy.clientSecret
  const clientID = strategy.clientId
  const tokenEndpoint = strategy.endpoints.token
  const audience = strategy.audience

  // IMPORTANT: remove clientSecret from generated bundle
  delete strategy.clientSecret

  // Endpoint
  const endpoint = `/_auth/oauth/${strategy.name}/authorize`
  strategy.endpoints.token = endpoint

  // Set response_type to code
  strategy.responseType = 'code';

  // Form data parser
  const formMiddleware = bodyParser.urlencoded({ extended: true })

  // Register endpoint
  nuxt.options.serverMiddleware.unshift({
    path: endpoint,
    handler: (req, res, next) => {
      if (req.method !== 'POST') {
        return next()
      }

      formMiddleware(req, res, () => {
        const {
          code,
          code_verifier: codeVerifier,
          redirect_uri: redirectUri = strategy.redirectUri,
          response_type: responseType = strategy.responseType,
          grant_type: grantType = strategy.grantType,
          refresh_token: refreshToken
        } = req.body

        // Grant type is authorization code, but code is not available
        if (grantType === 'authorization_code' && !code) {
          return next()
        }

        // Grant type is refresh token, but refresh token is not available
        if (grantType === 'refresh_token' && !refreshToken) {
          return next()
        }

        let data: qs.ParsedUrlQueryInput | string = {
          client_id: clientID,
          client_secret: clientSecret,
          refresh_token: refreshToken,
          grant_type: grantType,
          response_type: responseType,
          redirect_uri: redirectUri,
          audience,
          code_verifier: codeVerifier,
          code
        };

        console.log(data)

        const headers = {
          Accept: 'application/json',
          'Content-Type': 'application/json',
        }

        if (useForms) {
          data = qs.stringify(data)
          headers['Content-Type'] = 'application/x-www-form-urlencoded';
        }

        axios
          .request({
            method: 'post',
            url: tokenEndpoint,
            data,
            headers
          })
          .then((response) => {
            res.end(JSON.stringify(response.data))
          })
          .catch((error) => {
            console.log(error)
            console.log(error.response.data)
            res.statusCode = error.response.status
            res.end(JSON.stringify(error.response.data))
          });
      })
    },
  })
}

export interface ProloginProviderOptions
  extends ProviderOptions,
    Oauth2SchemeOptions {}

export default function (
  nuxt: any,
  strategy: ProviderPartialOptions<ProloginProviderOptions>
): void {
  const DEFAULTS: typeof strategy = {
    scheme: 'openIDConnect',
    endpoints: {
      configuration:
        "https://auth.prologin.org/application/o/prologin-public-test-client/.well-known/openid-configuration",
      token: "https://auth.prologin.org/application/o/token/",
    },
    acrValues: "goauthentik.io/providers/oauth2/default",
    grantType: 'authorization_code',
    codeChallengeMethod: 'S256',
    scope: ["openid", "profile", "email"],
  }

  assignDefaults(strategy, DEFAULTS)

  addAuthorize(nuxt, strategy, true)
}
