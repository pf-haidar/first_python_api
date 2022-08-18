def pessoaEntity(item) -> dict:
    return{
        '_id': str(item['_id']),
        'nome': item['nome']
    }

def pessoasEntity(entity) -> list:
    return[pessoaEntity(item) for item in entity]