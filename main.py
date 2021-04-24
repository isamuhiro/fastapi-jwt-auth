import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from auth import AuthHandler
from schemas import AuthRequest

app = FastAPI()

auth_handler = AuthHandler()
users = []


@app.post('/register', status_code=201)
def register(auth_request: AuthRequest):
    if any(user['username'] == auth_request.username for user in users):
        raise HTTPException(status_code=400, detail='Username is taken')

    hashed_password = auth_handler.get_password_hash(auth_request.password)
    users.append({
        'username': auth_request.username,
        'password': hashed_password
    })
    return


@app.post('/login')
def login(auth_request: AuthRequest):
    user = next(user for user in users if user['username'] == auth_request.username)

    if (user is None) or (not auth_handler.verify_password(auth_request.password, user['password'])):
        raise HTTPException(status_code=401, detail='Invalid username and/or password')

    token = auth_handler.encode_token(user['username'])
    return {'token': token}


@app.get('/')
def index():
    return {'message': 'Unprotected Route'}


@app.get('/protected')
def protected(username=Depends(auth_handler.auth_wrapper)):
    return {'username': username}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
