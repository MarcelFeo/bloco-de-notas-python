import PySimpleGUI as sg

#Funções para editar

#Cria um novo arquivo
def novo_arquivo():
    window["_BLOCO_"].update(value="")
    filename = None
    return filename

#Abre um arquivo que já existe
def abrir_arquivo():
    try:
        filename: str = sg.popup_get_file("Open File", no_window=True)
    except:
        return
    if filename not in (None, "") and not isinstance(filename, tuple):
        with open(filename, "r") as f:
            window["_BLOCO_"].update(value=f.read())
    return filename

#Salva o arquivo
def salvar_arquivo(filename: str):
    if filename not in (None, ""):
        with open(filename, "w") as f:
            f.write(values.get("_BLOCO_"))
    else:
        save_file_as()

#Complementa a função salvar_arquivos colocando a extensão .txt
def save_file_as():
    try:
        filename: str = sg.popup_get_file(
            "Save File",
            save_as=True,
            no_window=True,
            default_extension=".txt",
            file_types=(("Text", ".txt"),),
        )
    except:
        return
    if filename not in (None, "") and not isinstance(filename, tuple):
        with open(filename, "w") as f:
            f.write(values.get("_BLOCO_"))
    return filename

#Coloca todas as letras em caixa baixa
def tornar_caixa_baixa():
    window["_BLOCO_"].update(value=str(values["_BLOCO_"]).lower())

#Coloca todas as letras em caixa alta
def tornar_caixa_alta():
    window["_BLOCO_"].update(value=str(values["_BLOCO_"]).upper())

#Coloca todas as primeiras letras em maiúsculo
def letras_maiusculas():
    window["_BLOCO_"].update(value=str(values["_BLOCO_"]).title())

#Coloca as palavras no centro
def centro():
    window["_BLOCO_"].update(value=str(values["_BLOCO_"]).center(98))


#Tema
sg.ChangeLookAndFeel("Black") 

#Tamanho
WIN_W = 95
WIN_H = 30

#Nome do arquivo
filename = None 

file_new = "Novo"
file_open = "Abrir"
file_save = "Salvar"

#Menu de opções
#sg.Text()
menu_layout = (
    ["Arquivo", [file_new, file_open, file_save]],
    ["Editar", ["Tornar caixa alta", "Tornar caixa baixa", 
    "Tornar a primeira letra de cada palavra maiúscula", 
    "Centralizar o texto"]],
)

layout = [
    [sg.MenuBar(menu_layout)],
    [
        sg.Multiline(
            font=("Consolas", 12), text_color="white", size=(WIN_W, WIN_H), key="_BLOCO_"
        )
    ],
]

window = sg.Window(
    "Notepad",
    layout=layout,
    margins=(0, 0),
)
window.read(timeout=1)

window["_BLOCO_"].expand(expand_x=True, expand_y=True)


while True:
    event, values = window.read()

    if event in (None, "Exit"):
        window.close()
        break
    if event in (file_new):
        filename = novo_arquivo()
    if event in (file_open):
        filename = abrir_arquivo()
    if event in (file_save):
        salvar_arquivo(filename)
    if event in ("Save As",):
        filename = save_file_as()
    if event == "Tornar caixa alta":
        tornar_caixa_alta()
    if event == "Tornar caixa baixa":
        tornar_caixa_baixa()
    if event == "Tornar a primeira letra de cada palavra maiúscula":
        letras_maiusculas()
    if event == "Centralizar o texto":
        centro()

Notepad = Notepad()
Notepad.Iniciar()