#!/bin/sh

RAND_SECRET_NAMES="django-secret-key postgres-passwd"
USER_SECRET_NAMES="\
    documents-generator-username \
    documents-generator-password \
    recaptcha-public-key \
    recaptcha-private-key"



for name in $RAND_SECRET_NAMES; do
    DEST=./secrets/"$name"
    echo "Generating secret for ${name}"

    if [ ! -e "$DEST" ]; then
        tr -d -c "a-zA-Z0-9" < /dev/urandom | fold -w32 | head -n 1 > "$DEST"
    fi
done

for name in ${USER_SECRET_NAMES}; do
    DEST=./secrets/$name

    envname=$(echo "$name" | sed 's/-/_/g')
    envvalue="$(eval echo "\${$envname}")"
    if [ -n "$envvalue" ]; then
        echo "Writing secret for ${name} from env..."
        echo "$envvalue" > "${DEST}"
        continue
    fi
    if [ ! -e "${DEST}" ]; then
        echo "Please input a value for ${name}: "
        read -r value
        echo "${value}" > "${DEST}"
    fi
done

echo "tVOgJ4hxT8uV0bjMIjT4psPARaR1XgxhIYoXcqnGIFZVmCpMTrhDKEK2qy6TT9VO" > ./secrets/oidc-client-id
echo "t9pvgKnwB37CeutWpPOEKMDv3gmp9kjUtQ5ifDzF9gBPMGO4yhHLdUNnh7AjRuWH" > ./secrets/oidc-client-secret

echo "BOAGOnqH0OyR086rYF8oT6VUcCo1tNYITWlRTyyOU5BzJpLjV6VWBom3boADe4Z0" > ./secrets/documents-generator-client-id

echo "accessKey1" > ./secrets/s3-access
echo "verySecretKey1" > ./secrets/s3-secret
