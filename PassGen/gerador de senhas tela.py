import random
import PySimpleGUI as sg

class TelaPassGen:
    sg.theme('Default')
    def __init__(self):
        layout = [
                [sg.Text('Quantidade de Caracteres'),sg.Input(size=(15,0),key='caractere')],
                [sg.Button('Gerar senha')],
                [sg.Output(size=(40,10))]
            ]
        self.janela = sg.Window("PASSWORD GENERATOR").layout(layout)

    def Iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()
            num = self.values['caractere']
            num = int(num)

            def passGen(num):
                c=0
                password = []
                i = ''
                lista = ['1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
                while c<num:
                    password.append(random.choice(lista))
                    i+=random.choice(lista)
                    c+=1
                print(f'Password: {i}\n{"-" * 70}')
            passGen(num)

tela = TelaPassGen()
tela.Iniciar()
