from curso import Curso
from aluno import Aluno

def cadastro_curso():
    cursos = []
    quantidade = int(input("Quantos cursos deseja cadastrar? "))
    for i in range(quantidade):
        print(f"\nCadastro do curso {i + 1}:")
        nome = input("Nome do curso: ")
        duracao = int(input("Duração do curso (em semestres): "))
        cursos.append(Curso(nome, duracao))
    return cursos

# Alterado: agora recebe 'lista_cursos' como parâmetro
def cadastro_aluno(lista_cursos): 
    alunos = []
    quantidade = int(input("Quantos alunos deseja cadastrar? "))
    
    for i in range(quantidade):
        print(f"\nCadastro do aluno {i + 1}:")
        nome = input("Nome do aluno: ")
        matricula = input("Matrícula (8 a 10 dígitos): ")
        
        while True:
            # Exibe as opções para o usuário
            for idx, c in enumerate(lista_cursos):
                print(f"{idx + 1} - {c.nome}")
                
            escolha = input("Digite o numero do curso: ")
            if escolha.isdigit() and 1 <= int(escolha) <= len(lista_cursos):
                 curso_selecionado = lista_cursos[int(escolha) - 1]
                 break
            else:
                print("Escolha inválida. Tente novamente.")

        aluno = Aluno(nome, matricula, curso_selecionado)
        alunos.append(aluno)    
    return alunos # Retorna a lista de alunos

def adicionar_notas(lista_alunos):
    # Percorre cada aluno na lista recebida
    for aluno in lista_alunos:
        print(f"\n--- Adicionando 2 notas para: {aluno.get_nome()} ---")
        
        # O range(2) garante que o loop execute exatamente 2 vezes (0, 1)
        for i in range(2):
            while True:
                try:
                    entrada = input(f"Digite a nota {i + 1}: ")
                    nota = float(entrada)
                    
                    # Validação do intervalo da nota (0 a 10)
                    if 0 <= nota <= 10:
                        aluno.adicionar_nota(nota)
                        break # Sai do while e vai para a próxima iteração do range
                    else:
                        print("Nota inválida! A nota deve estar entre 0 e 10.")
                except ValueError:
                    print("Entrada inválida! Por favor, digite um número.")