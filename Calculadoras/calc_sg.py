import PySimpleGUI as sg

class TelaPython:
    sg.theme('Default')
    # sg.change_look_and_feel('Default')
    def __init__(self):
        # layout
        layout = [
            [sg.Text('Primerio valor',size=(15,0)),sg.Input(size=(15,0),key='x')],
            [sg.Text('Segundo valor', size=(15,0)),sg.Input(size=(15,0),key='y')],
            [sg.Text('  OBS: Se você não digitar um número o programa fechará!')],
            [sg.Text('Escolha uma operação matemática:')],
            [sg.Radio('Adição','operacao',key='adicao'),sg.Radio('Subtração','operacao',key='subtracao'),sg.Radio('Multiplicação','operacao',key='multiplicacao'),sg.Radio('Divisão','operacao',key='divisao')],
            [sg.Button('Calcular')],
            [sg.Output(size=(50,10))]
        ]
        # janela
        self.janela = sg.Window("Calculadora simples").layout(layout)

    def Iniciar(self):
        while True:
            # extrair os dados da tela
            self.button, self.values = self.janela.Read()

            x = self.values['x']
            y = self.values['y']
            radicao = self.values['adicao']
            rsubtracao = self.values['subtracao']
            rmultiplicacao = self.values['multiplicacao']
            rdivisao = self.values['divisao']


            x = float(x)
            y = float(y)
            
            if (rdivisao == True and y == 0):
                print('[ERRO]: Não é possivel dividir por 0!')
            else: 
                if radicao == True:
                    res = x + y
                    print(f'A soma de de {x} + {y} é {res}')
                elif rsubtracao == True:
                    res = x - y
                    print(f'A subtração de de {x} - {y} é {res}')
                elif rmultiplicacao == True:
                    res = x * y
                    print(f'A multiplicação de de {x} x {y} é {res}')
                elif rdivisao == True:
                    res = x / y
                    print(f'A divição de de {x} / {y} é {res}')

tela = TelaPython()
tela.Iniciar()
