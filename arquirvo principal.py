class Aluno:
    def __init__(self, nome, matricula):
        # Atributos privados
        self.__nome = None 
        self.__matricula = None
        self.__notas = []
        
      
        self.set_nome(nome)
        self.set_matricula(matricula)

    # --- MÉTODOS GETTERS (Para ler os dados) ---
    def get_nome(self):
        return self.__nome

    def get_matricula(self):
        return self.__matricula

    def get_notas(self):
        return self.__notas

    # --- MÉTODOS SETTERS (Para modificar os dados) ---
    def set_nome(self, nome):
        self.__nome = nome

    def set_matricula(self, matricula):
        self.__matricula = matricula

    def set_notas(self, lista_notas):
        if isinstance(lista_notas, list):
            self.__notas = lista_notas

    # --- MÉTODOS DE LÓGICA ---
    def calcular_media(self):
        if not self.__notas:
            return 0.0
        return sum(self.__notas) / len(self.__notas)

    def mostrar_dados(self):
        print(f"Nome: {self.get_nome()}")
        print(f"Matrícula: {self.get_matricula()}")
        print(f"Notas: {self.get_notas()}")
        print(f"Média: {self.calcular_media():.2f}")

# --- ÁREA DE EXECUÇÃO (Fora da classe) ---

aluno1 = Aluno("Marcos", "2025101035")
aluno1.set_notas([8.0, 7.0, 9.0])

aluno2 = Aluno("Ana", "2025101036")
aluno2.set_notas([9.0, 8.5, 7.5])

print("--- Dados do Aluno 1 ---")
aluno1.mostrar_dados()

print("\n--- Dados do Aluno 2 ---")
aluno2.mostrar_dados()