from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from schema.mongo_db import conn
from auth.auth_handler import signJWT
from auth.auth_bearer import JWTBearer
from routes.pessoa import retorna_uma_pessoa
from schema.pessoa import pessoasEntity

Route_Autenticacao = APIRouter()

@Route_Autenticacao.post("/autentica/${emailUser}", status_code=200, tags=["Segurança"])
async def login(form_data:  OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    
    try:
        pessoasEntity(conn.local.pessoas.find({'email': email}))
        
        id_usuario = 0
        email = ''
        nome = ''
        tipo_usuario = ''
        print(result)

        for user in result:
            id_usuario = user.id_usuario    
            email = user.email
            nome = user.nome
            tipo_usuario = user.tipo_usuario
            print(user)
            
        print(id_usuario)
        if id_usuario == 0:
            raise HTTPException(status_code=401, detail="Falha na autenticação")
        else:
            return {"access_token": signJWT(form_data.username), "id_usuario": id_usuario, "email": email, "nome_usuario": nome, "tipo_usuario": tipo_usuario}

    except Exception as e:
        print(e)
        
@Route_Autenticacao.get("/valida-token/", dependencies=[Depends(JWTBearer())], tags=["Segurança"])
async def valida_token(token: str):
    return {"token": token}