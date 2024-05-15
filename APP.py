import PySimpleGUI as sg  # type: ignore

# Criando o layout
def criar_janela_inicial():
    sg.theme('Reddit')
    linha = [
        [sg.Checkbox(''), sg.Input('')]
    ]
    layout = [
        [sg.Frame('TAREFAS', layout= linha, key= 'container')],
        [sg.Button('Nova Tarefa'), sg.Button('Resetar')]
    ]

    return sg.Window('Todo List', layout= layout, finalize= True)

# Criar a janela 
janela = criar_janela_inicial()

# Criar as regras dessa janela
while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Nova Tarefa':
        janela.extend_layout(janela['container'], [[sg.Checkbox(''), sg.Input('')]])
    elif event == 'Resetar':
        janela.close()
        janela = criar_janela_inicial()
