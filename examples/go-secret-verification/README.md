# ✅ Example go server verifying X-Signature

This example shows how to verify the `X-Signature` used by gridX. It parses the incoming `X-Signature` header using the secret that is passed as environtment variable `WEBHOOK_SECRET`. The parser goes through the following steps to verify the signature:
1. Check if the signature has the correct prefix.
    ```go
    const signaturePrefix = "sha512="
    ```
2. Sign event payload with notification rule secret and compare resulting signature with `X-Signature` header value
    ```go
    localSignature := signBody(secret, h.Payload)
    hmac.Equal(localSignature, actualSignature)
    ```
   
## Usage

```sh
export WEBHOOK_SECRET=<your token> # from notification rule
```

```sh
go run main.go
```