from aluno import AlunoClass
from turma import Turma

alunos = []
alunos.append(AlunoClass('alex', 'jorge', 10))
alunos.append(AlunoClass('gustavo', 'souza', 9))
alunos.append(AlunoClass('isabela', 'costa', 9))
alunos.append(AlunoClass('Enzo', 'almeira', 8))
alunos.append(AlunoClass('joao', 'Miguel', 7))

turmaObject = Turma()
turmaObject.cadastrarAlunos(alunos)

turmaObject.mostrarAlunos()
print('*' * 30)
print('Aluno com menor nota:', turmaObject.menorNota.mostrarAluno())
print('Aluno com maior nota:', turmaObject.maiorNota.mostrarAluno())
