# SEGUNDA VERSÃO DA ATIVIDADE CRIADA PELO PROFESSOR

from abc import ABC, abstractmethod


class portaria(ABC):
    @abstractmethod
    def entrar(self,pessoa):
        pass


class Aluno(portaria):
    def entrar(self, pessoa):
        return f"O {pessoa} tem relação com a instituição como Aluno"

class Professor(portaria):
    def entrar(self, pessoa):
        return f"O {pessoa} tem relação com a instiuição como Professor"

class Coordenador(portaria):
    def entrar(self, pessoa):
        return f"O {pessoa} tem relação com a instituição como Professor"

class Diretor(portaria):
    def entrar(self,pessoa):
        return f"O {pessoa} tem relação com a instituição como Diretor"

class Vestibulando(portaria):
    def entrar(self, pessoa):
        return f"O {pessoa} tem relação com a instituição como Vestibulando"

class Administrativo(portaria):
    def entrar(self, pessoa):
        return f"O {pessoa} tem relação com a instituição como Administrativo"
class naoPossui(portaria):
    def entrar(self, pessoa):
        return f"O {pessoa} não possui relação com a instituição, acompanhar até a secretaria" 

class FabricaPortaria:
    def criar_pessoa(self,cargo):
        if cargo=="Aluno":
            return Aluno()
        elif cargo=="Professor":
            return Professor()
        elif cargo=="Coordenador":
            return Coordenador()
        elif cargo=="Diretor":
            return Diretor()
        elif cargo=="Vestibulando":
            return Vestibulando()
        elif cargo=="Administrativo":
            return Administrativo()
        else:
            return naoPossui()
    
fabrica_pessoa = FabricaPortaria()
p= str(input("Digite S para cadastrar uma pessoa ou digite Q para sair: "))
while p!="Q":
    pessoa = fabrica_pessoa.criar_pessoa(str(input("Qual a sua relação com a FATEC: ")))
    print(pessoa.entrar(str(input("Entre com o seu nome: "))))
    print("---------------------------------------------------------------------")
    p= str(input("Digite S para cadastrar outra pessoa ou digite Q para sair: "))

