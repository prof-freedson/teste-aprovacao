import unittest

from aprovacao import Aprovacao

class TesteAprovacao(unittest.TestCase):
    # Primeiro teste
    # Calculo da média para as notas 6, 7, 8 e 9
    # Resultado esperado: 7.5
    def teste_calculo_media(self):
        media_um = Aprovacao
        self.assertEqual(media_um.calculoMedia(6,7,8,9), 7.5)

    def teste_aprovacao_aluno(self):
        aluno_um = Aprovacao
        self.assertEqual(aluno_um.aprova_ou_reprova(7.5), 'Aluno(a) aprovado(a)')

if __name__ == "__main__":
    unittest.main()