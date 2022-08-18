from fastapi import APIRouter, FastAPI
from routes.pessoa import Pessoas_Router

app = FastAPI(title='Hello World!!!', version='1.0.0')
api = APIRouter()

@api.get('/')
def entra_no_docs():
    try:
        return 'Digite /docs para entrar no Swagger!!!'
    except Exception as e:
        print(e)
        return {'response': 'Não retornou ninguém'}


app.include_router(Pessoas_Router)
app.include_router(api)