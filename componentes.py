class Casa:

    def __init__(self, posicaoX, posicaoY, tabuleiro, peca=None):
        self.peca = peca
        self.posicaoX = posicaoX
        self.posicaoY = posicaoY
        self.tabuleiro = tabuleiro

    def __str__(self):
        print('('+self.posicaoX + ', '+self.posicaoY+'): '+self.peca)

    def ocupar(self, peca):
        self.peca = peca

    def desocupar(self):
        self.peca = None

    def ocupada(self):
        if self.peca is not None:
            return True
        else:
            return False

class Peca:

    def __init__(self, id = None, casa=None):
        self.id = id
        if casa.ocupada():
            raise MovimentoInvalidoError("A casa ja esta ocupada")
        else:
            self.casa = casa
            casa.ocupar(self)

    def __str__(self):
        return 'Peca Base'

class Tabuleiro:

    def __init__(self, linhas, colunas):
        self.casas = [[Casa(j, i, self) for i in range(0, colunas)] for j in range(0, linhas)]



class PecaMovel(Peca):
    def __init__(self, cor, id = None, casa = None):
        Peca.__init__(self, id, casa)
        self.cor = cor

    def _mover(self, deslocamento_x=0, deslocamento_y=0):
        if self.casa is None:
            raise MovimentoInvalidoError("A peca ainda nao esta no tabuleiro.")
        else:
            x = self.casa.posicaoX
            y = self.casa.posicaoY
            try:
                nova_casa = self.casa.tabuleiro.casas[x + deslocamento_x][y + deslocamento_y]
                if nova_casa.ocupada():
                    raise MovimentoInvalidoError("Casa de destino ja esta ocupada")
            except IndexError:
                raise MovimentoInvalidoError ("A peca nao pode ser movida para cima")

            self.casa.desocupar()
            nova_casa.ocupar(self)
            self.casa = nova_casa

    def moverParaCima(self):
        self._mover(deslocamento_y=1)

    def moverParaBaixo(self):
        self._mover(deslocamento_y=-1)

    def moverParaEsquerda(self):
        self._mover(deslocamento_x=-1)

    def moverParaDireita(self):
        self._mover(deslocamento_x=1)



class MovimentoInvalidoError(Exception):
    pass