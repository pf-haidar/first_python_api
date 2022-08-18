# Comandos para executar a API
- Verificar se estou no mesmo diretório do arquivo Main.py ou do arquivo principal
- No terminal:
-- uvicorn nome_do_arquivo:nome_da_variavel_fastAPI --host 0.0.0.0 --port numero_da_porta --reload (para não precisar reexecutar a API)
-- EX: uvicorn main:app --host 0.0.0.0 --port 8081 --reload

- localhost:8081/docs