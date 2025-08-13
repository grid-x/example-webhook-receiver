# go-hmac-verification

This example includes a simple HTTP server that listens on `:8080/hooks/xenon`. It verifies the HMAC digests parsed from
the HTTP request header `X-Signature` against the secret key provided on the environment variable `HMAC_SECRET_KEY`.

```bash
# terminal 1
$ export HMAC_SECRET_KEY=<...>
$ go run ./cmd/server
```

Then send requests to it from a different terminal:

**Request without `X-Signature` header:**
```bash
# terminal 2
$ curl -I http://localhost:8080/hooks/xenon
HTTP/1.1 401 Unauthorized
Date: Wed, 13 Aug 2025 13:45:22 GMT
```

The server will log:
```
2025/08/13 15:45:16 WARN Missing HMAC signature header
```

**Request with no valid digest in `X-Signature` header:**

If you want to test requests with a valid digest, you can use the dummy client in this example:
```bash
# terminal 2
$ export HMAC_SECRET_KEY=foo # different than in terminal 1
$ go run ./cmd/client
2025/08/13 16:13:44 401
```

The server will log:
```
2025/08/13 16:13:44 WARN failed verifying HMAC signature error="no valid HMAC digest found"
```

**Request with valid digest in `X-Signature` header:**

If you want to test requests with a valid digest, you can use the dummy client in this example:
```bash
# terminal 2
$ export HMAC_SECRET_KEY=<...> # same as for the server
$ go run ./cmd/client
2025/08/13 16:13:33 204
```

And the server will log:
```
2025/08/13 16:13:33 INFO Received request body="{\"id\":\"8bb71fef-9cb5-4054-89c3-d4aeac5489a7\",..."
```
