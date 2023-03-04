from flask import Flask, request
from abc import ABC, abstractmethod

app = Flask(__name__)

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
        return f"O {pessoa} tem relação com a instituição como Coordenador"

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

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        pessoa = FabricaPortaria().criar_pessoa(request.form['cargo'])
        mensagem = pessoa.entrar(request.form['nome'])
        return f'<h1>{mensagem}</h1>'
    return '''
        <form method="post">
            <label>Nome:</label>
            <input type="text" name="nome"><br><br>
            <label>Cargo:</label>
            <select name="cargo">
                <option value="Aluno">Aluno</option>
                <option value="Professor">Professor</option>
                <option value="Coordenador">Coordenador</option>
                <option value="Diretor">Diretor</option>
                <option value="Vestibulando">Vestibulando</option>
                <option value="Administrativo">Administrativo</option>
                <option value="naoPossui">Não possui relação com a instituição</option>
            </select><br><br>
            <input type="submit" value="Entrar">
        </form>
    '''

if __name__ == '__main__':
    app.run()
