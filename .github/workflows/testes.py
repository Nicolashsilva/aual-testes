import unittest
from aluno import AlunoClass
from turma import Turma


class TurmaTest(unittest.TestCase):

    def setUp(self):
        print('Teste', self._testMethodName, 'sendo executado')
        self.alunos = []
        self.alunos.append(AlunoClass('alex', 'jorge', 10))
        self.alunos.append(AlunoClass('gustavo', 'souza', 9))
        self.alunos.append(AlunoClass('isabela', 'costa', 9))
        self.alunos.append(AlunoClass('enzo', 'almeira', 8))
        self.alunos.append(AlunoClass('joao', 'miguel', 7))
        self.turmaObject = Turma()
        self.turmaObject.cadastrarAlunos(self.alunos)

    def tearDown(self):
        print('Teste', self._testMethodName, 'finalizado.')

    def testMaior(self):
        self.assertEqual(10, self.turmaObject.maiorNota.nota,
                         'Erro ao encontrar maior nota')

    def testMenor(self):
        self.assertEqual(7, self.turmaObject.menorNota.nota,
                         'Error ao encontrar menor nota')

    def testIntervalo(self):
        self.assertTrue((self.turmaObject.menorNota.nota > 0
                         and self.turmaObject.maiorNota.nota <= 10),
                        'Error ao verificar intervalo')


if __name__ == "__main__":
    unittest.main()
