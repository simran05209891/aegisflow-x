from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = "aegisflow-secret"
ALGORITHM = "HS256"

@app.post("/login")
def login():
    token = jwt.encode({"user": "admin"}, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": token, "token_type": "bearer"}

@app.get("/secure")
def secure(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return {"status": "Authorized", "user": payload["user"]}
    except:
        raise HTTPException(status_code=401, detail="Unauthorized")
