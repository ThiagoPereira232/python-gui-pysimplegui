import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        # layout
        layout = [
            [sg.Text('Nome'),sg.Input()],
            [sg.Text('Idade'),sg.Input()],
            [sg.Button('Enviar Dados')]
        ]
        # janela
        janela = sg.Window("Dados do Usuário").layout(layout)
        # extrair os dados da tela
        self.button, self.values = janela.Read()

    def Iniciar(self):
        print(self.values)

tela = TelaPython()
tela.Iniciar()
