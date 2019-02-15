import unittest
import componentes



class MyTestCase(unittest.TestCase):
    def test_cria_tabuleiro(self):
        a = componentes.Tabuleiro(1, 1)
        self.assertIsNotNone(a)
        self.assertEqual(len(a.casas), 1,)
        self.assertEqual(len(a.casas[0]), 1)

    def test_cria_peca(self):
        tabuleiro = componentes.Tabuleiro(1, 1)
        peca = componentes.Peca(casa=tabuleiro.casas[0][0])
        self.assertIsNotNone(peca)
        self.assertIsNotNone(tabuleiro.casas[0][0])
        self.assertEqual(peca.casa.posicaoX, 0)
        self.assertEqual(peca.casa.posicaoY, 0)

    def test_cria_peca_casa_ocupada(self):
        tabuleiro = componentes.Tabuleiro(1, 1)
        peca = componentes.Peca(casa=tabuleiro.casas[0][0])
        with self.assertRaises(componentes.MovimentoInvalidoError):
            componentes.Peca(casa=tabuleiro.casas[0][0])

    def test_move_peca_movel_para_cima(self):
        tabuleiro = componentes.Tabuleiro(1, 2)
        peca = componentes.PecaMovel("COR", casa=tabuleiro.casas[0][0])
        self.assertEqual(peca.casa.posicaoX, 0)
        self.assertEqual(peca.casa.posicaoY, 0)
        peca.moverParaCima()
        self.assertEqual(peca.casa.posicaoX, 0)
        self.assertEqual(peca.casa.posicaoY, 1)
        self.assertFalse(tabuleiro.casas[0][0].ocupada())

    def test_move_peca_movel_para_cima_casa_ocupada(self):
        tabuleiro = componentes.Tabuleiro(1, 2)
        peca = componentes.PecaMovel("COR", casa=tabuleiro.casas[0][0])
        componentes.PecaMovel("COR", casa=tabuleiro.casas[0][1])

        with self.assertRaises(componentes.MovimentoInvalidoError):
            peca.moverParaCima()

    def test_move_peca_movel_limite(self):
        tabuleiro = componentes.Tabuleiro(1, 1)
        peca = componentes.PecaMovel("COR", casa=tabuleiro.casas[0][0])

        with self.assertRaises(componentes.MovimentoInvalidoError):
            peca.moverParaCima()

        with self.assertRaises(componentes.MovimentoInvalidoError):
            peca.moverParaBaixo()

        with self.assertRaises(componentes.MovimentoInvalidoError):
            peca.moverParaDireita()

        with self.assertRaises(componentes.MovimentoInvalidoError):
            peca.moverParaEsquerda()


    def test_move_peca_movel_para_baixo(self):
        tabuleiro = componentes.Tabuleiro(1, 2)
        peca = componentes.PecaMovel("COR", casa=tabuleiro.casas[0][1])
        self.assertEqual(peca.casa.posicaoX, 0)
        self.assertEqual(peca.casa.posicaoY, 1)
        self.assertFalse(tabuleiro.casas[0][0].ocupada())
        self.assertTrue(tabuleiro.casas[0][1].ocupada())
        peca.moverParaBaixo()
        self.assertEqual(peca.casa.posicaoX, 0)
        self.assertEqual(peca.casa.posicaoY, 0)
        self.assertTrue(tabuleiro.casas[0][0].ocupada())
        self.assertFalse(tabuleiro.casas[0][1].ocupada())

    def test_move_peca_movel_para_baixo_casa_ocupada(self):
        tabuleiro = componentes.Tabuleiro(1, 2)
        peca = componentes.PecaMovel("COR", casa=tabuleiro.casas[0][1])
        componentes.PecaMovel("COR", casa=tabuleiro.casas[0][0])

        with self.assertRaises(componentes.MovimentoInvalidoError):
            peca.moverParaBaixo()

    def test_move_peca_movel_para_esquerda(self):
        tabuleiro = componentes.Tabuleiro(2, 1)
        peca = componentes.PecaMovel("COR", casa=tabuleiro.casas[1][0])
        self.assertEqual(peca.casa.posicaoX, 1)
        self.assertEqual(peca.casa.posicaoY, 0)
        self.assertFalse(tabuleiro.casas[0][0].ocupada())
        self.assertTrue(tabuleiro.casas[1][0].ocupada())
        peca.moverParaEsquerda()
        self.assertEqual(peca.casa.posicaoX, 0)
        self.assertEqual(peca.casa.posicaoY, 0)
        self.assertTrue(tabuleiro.casas[0][0].ocupada())
        self.assertFalse(tabuleiro.casas[1][0].ocupada())

    def test_move_peca_movel_para_esquerda_casa_ocupada(self):
        tabuleiro = componentes.Tabuleiro(2, 1)
        peca = componentes.PecaMovel("COR", casa=tabuleiro.casas[1][0])
        componentes.PecaMovel("COR", casa=tabuleiro.casas[0][0])

        with self.assertRaises(componentes.MovimentoInvalidoError):
            peca.moverParaEsquerda()

    def test_move_peca_movel_para_direita(self):
        tabuleiro = componentes.Tabuleiro(2, 1)
        peca = componentes.PecaMovel("COR", casa=tabuleiro.casas[0][0])
        self.assertEqual(peca.casa.posicaoX, 0)
        self.assertEqual(peca.casa.posicaoY, 0)
        self.assertFalse(tabuleiro.casas[1][0].ocupada())
        self.assertTrue(tabuleiro.casas[0][0].ocupada())
        peca.moverParaDireita()
        self.assertEqual(peca.casa.posicaoX, 1)
        self.assertEqual(peca.casa.posicaoY, 0)
        self.assertTrue(tabuleiro.casas[1][0].ocupada())
        self.assertFalse(tabuleiro.casas[0][0].ocupada())

    def test_move_peca_movel_para_esquerda_casa_ocupada(self):
        tabuleiro = componentes.Tabuleiro(2, 1)
        peca = componentes.PecaMovel("COR", casa=tabuleiro.casas[0][0])
        componentes.PecaMovel("COR", casa=tabuleiro.casas[1][0])

        with self.assertRaises(componentes.MovimentoInvalidoError):
            peca.moverParaDireita()


if __name__ == '__main__':
    unittest.main()
