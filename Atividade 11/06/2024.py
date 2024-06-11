# forma simplificada 
import os
from dataclasses import dataclass # biblioteca da classe 

# Constante 
Quantidade_Aluno = 2
# Limpar tela do terminal  
os.system("cls || clear")

# Criando uma classe
@dataclass # o @dataclass é como uma anotação 

class Aluno:
    nome: str
    idade: int 
    peso: float
    altura: float

alunos = []
# Solicitando dados ao usuário como nome e idade 
for i in range (Quantidade_Aluno):
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    peso = float (input("Informe seu peso: "))
    altura = float (input("Informe sua altura: "))
    aluno = Aluno(nome = nome, idade = idade, peso = peso, altura = altura)
    alunos.append(aluno)
# Exibindo o resultado que tá armazenado na lista do vetor.
for dados_aluno in alunos:
    print(f"Nome: {dados_aluno.nome}")
    print(f"Idade: {dados_aluno.idade } anos")
    print(f"Peso: {dados_aluno.peso}")
    print(f"Altura: {dados_aluno.altura}\n")