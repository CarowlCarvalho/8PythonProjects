#Projeto 3 - Chute um número
#Objetivo: Criar um algoritimo que gera um valor aleatório e o usuário precisa acertar qual é
#Projeto 4 - Gerar tela de interação
import random
import PySimpleGUI as sg

class ChuteONumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 10
        self.tentar_novamente = True

    def Iniciar(self):
        #Layout
        layout = [
            [sg.Text('Seu chute', size=(20,0))],
            [sg.Input(size=(18,0), key='ValorChute')],
            [sg.Button('Chutar')],
            [sg.Output(size=(20,10))]
        ]
        #Criar uma tela
        self.janela = sg.Window('Chute um número!', Layout=layout)

        self.GerarNumAleatorio()
        try:
            while True:
                #Receber os valores
                self.evento, self.valores = self.janela.Read()
                #Fazer alguma coisa com esses valores
                if self.evento == 'Chutar':
                    self.valor_do_chute = self.valores['ValorChute']
                    while self.tentar_novamente == True:
                        if int(self.valor_do_chute) > self.valor_aleatorio:
                            print('Chute um número menor!')
                            self.LerValoresDaTela()
                            break
                        elif int(self.valor_do_chute) < self.valor_aleatorio:
                            print('Chute um número maior!')
                            break
                        if int(self.valor_do_chute) == self.valor_aleatorio:
                            self.tentar_novamente = False 
                            print('Parabéns você acertou!!!')
        except:
            print('Favor digitar apenas números!')
            self.Iniciar()



    def GerarNumAleatorio(self):
        self.valor_aleatorio = random.randint(self.valor_minimo, self.valor_maximo)


chute = ChuteONumero()
chute.Iniciar()