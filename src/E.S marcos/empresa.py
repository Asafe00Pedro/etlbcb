class Pilar:
    def __init__(self, nome: str, descricao: str):
        self.nome = nome
        self.descricao = descricao

    def __str__(self):
        return f"{self.nome}: {self.descricao}"


class Funcionario:
    def __init__(self, nome: str):
        self.nome = nome

    def __str__(self):
        return self.nome


class Empresa:
    def __init__(self, nome: str):
        self.__nome = nome
        self.__pilares = []
        self.__funcionarios = []

    def cadastrar_pilar(self, nome: str, descricao: str):
        novo_pilar = Pilar(nome, descricao)
        self.__pilares.append(novo_pilar)

    def adicionar_funcionario(self, nome: str):
        novo_funcionario = Funcionario(nome)
        self.__funcionarios.append(novo_funcionario)

    def listar_pilares(self):
        return [str(p) for p in self.__pilares]

    def listar_funcionarios(self):
        return [str(f) for f in self.__funcionarios]

    def get_nome(self):
        return self.__nome

emp = Empresa("Turma 34")

emp.cadastrar_pilar("Ética", "Agir de forma correta.")
emp.cadastrar_pilar("Exelência", "Fazer o melhor possivel com o maximo de qualidade.")

emp.adicionar_funcionario("Pedro")
emp.adicionar_funcionario("Rafael")

print("Pilares da empresa:")
for p in emp.listar_pilares():
    print("-", p)

print("\nFuncionários:")
for f in emp.listar_funcionarios():
    print("-", f)
