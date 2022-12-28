#!/bin/sh

RAND_SECRET_NAMES="django-secret-key postgres-passwd"

for name in $RAND_SECRET_NAMES; do
    DEST=./secrets/"$name"
    if [ ! -e "$DEST" ]; then
        tr -d -c "a-zA-Z0-9" < /dev/urandom | fold -w32 | head -n 1 > "$DEST"
    fi
done

echo "accessKey1" > ./secrets/s3-access
echo "verySecretKey1" > ./secrets/s3-secret

echo "tVOgJ4hxT8uV0bjMIjT4psPARaR1XgxhIYoXcqnGIFZVmCpMTrhDKEK2qy6TT9VO" > ./secrets/prologin-oidc-client-id
echo "t9pvgKnwB37CeutWpPOEKMDv3gmp9kjUtQ5ifDzF9gBPMGO4yhHLdUNnh7AjRuWH" > ./secrets/prologin-oidc-client-secret
