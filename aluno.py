class Aluno: 
    def __init__(self, nome, matricula, curso):
        self.__nome = None
        self.__matricula = None
        self.__notas =[]
        self.curso = curso # ADC em 23/03

        self.set_nome(nome)
        self.set_matricula(matricula)
 # -----------Métodos-----------
    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        if nome:
            self.__nome = nome
        else:
            print("Nome Inválido.")

    def get_matricula(self):
        return self.__matricula

    def set_matricula(self, matricula):
        if matricula.isdigit() and 8 <= len(matricula) <= 10:
            self.__matricula = matricula
        else: 
            print ("Matrícula Inválida.")
    
    def adicionar_nota(self, nota):
        if 0 <= nota <= 10:
            self.__notas.append(nota)
        else:
            print("Nota inválida!")

    def calcular_media(self): # Retorna a média das notas do aluno ou 0 se não houver notas.
        if len(self.__notas) == 0:
            return 0
        return sum(self.__notas) / len(self.__notas)
    def mostrar_dados(self):
        print(f"Nome : {self.get_nome()}")
        print(f"Matricula : {self.get_matricula()}")
        print(f"Média : {self.calcular_media()}")
        print(self.curso.descricao())