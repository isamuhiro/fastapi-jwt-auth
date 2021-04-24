# FastAPI JWT Auth

Simple authentication and authorization app using FastAPI.

## Sign up

```bash
curl --request POST \
  --url http://127.0.0.1:8000/register \
  --header 'content-type: application/json' \
  --data '{"username": "teste", "password": "teste"}'
```


## Sign in

```bash
curl --request POST \
  --url http://127.0.0.1:8000/login \
  --header 'content-type: application/json' \
  --data '{"username": "teste", "password": "teste"}'
```


## Access restrict resource

```bash
curl --request GET \
  --url http://127.0.0.1:8000/protected \
  --header 'authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MTkyMzU1OTEsImlhdCI6MTYxOTIzNTI5MSwic3ViIjoidGVzdGUifQ.J1nHt7iNN7SDaAbqVDb2LyXiWZMJfySS66g1wr9IDW0'
```