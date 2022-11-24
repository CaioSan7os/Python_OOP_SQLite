#Importa nosso arquivo Pessoa.py no diretório model
from model.Pessoa import Pessoa
from database.Database import Database
from dao.PessoaDAO import PessoaDAO
#Exemplo de uso
poyatos = Pessoa(1, "Caio Santos")
print(poyatos)

#Quero mostrar só o nome
print(poyatos.nome)

#chama o objeto de banco de dados
db = Database()
pessoaDAO = PessoaDAO(db.conexao, db.cursor)
pessoas = pessoaDAO.getAll()
for pessoa in pessoas:
  print(pessoa)