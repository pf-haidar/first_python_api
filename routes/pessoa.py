from bson import ObjectId
from fastapi import APIRouter
from mongo_db import conn
from pessoa import Pessoa
from schema.pessoa import pessoaEntity, pessoasEntity

Pessoas_Router = APIRouter()

@Pessoas_Router.get('/lista-todas-pessoas', tags=['pessoas'])
def retorna_todas_pessoas():
    try:
        return pessoasEntity(conn.local.pessoas.find())
    except Exception as e:
        print(e)
        return {'response': 'Não retornou ninguém'}

@Pessoas_Router.get('/{idPessoa}', tags=['pessoas'])
def retorna_uma_pessoa(idPessoa: str):
    try:
        id = ObjectId(idPessoa)
        return pessoasEntity(conn.local.pessoas.find({'_id': id}))
    except Exception as e:
        print(e)
        return {'response': 'Não achou ninguém'}

@Pessoas_Router.put('/adicionarNome', tags=['pessoas'])
async def adicionar_nome(pessoa: Pessoa):
    try:
        conn.local.pessoas.insert_one(dict(pessoa))
        return {'response': 'Adicionou o nome.'}
    except Exception as e:
        print(e)
        return{'response': 'Não adicionou o nome.'}