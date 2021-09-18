import PySimpleGUI as sg

# CONFIGS DO GUI
settings = sg.UserSettings()

# LAYOUTS
sg.theme("Default1")

def JanelaLogin():
    estilo = [
        [sg.Text("Usuário"), sg.Input(key='usuario', size=(20, 1))],
        [sg.Text("Senha"), sg.Input(key='senha', password_char='*', size=(20, 1))],
        [sg.Button("Entrar")]
    ]
    return sg.Window("Login", layout=estilo, finalize=True)


def JanelaMenu():
    menu = [
        [sg.Button ("Configuracoes", size=(15, 5)), sg.Button("Relatorio", size=(15, 5))],
        [sg.Button("Logs", size=(15, 5)), sg.Button("Status dos Processos", size=(15, 5))],
        [sg.Combo(["Automático", "Manual"], default_value="Automático", size=10), sg.Button("Deslogar", size=(15, 5)),
         sg.Button("Enviar e Receber", size=(15, 5))]
    ]
    return sg.Window("Meunu", layout=menu, finalize=True)

    #Botões do Menu
def JanelaConfig():
    config = [
        [sg.Text("Arquivo de Remessa"),sg.InputText("Caminho"), sg.Button("Salvar")],
        [sg.Text("Arquivo de Retorno"),sg.InputText("Caminho"), sg.Button("Salvar")],
        [sg.Text("Pasta de Logs     "),sg.InputText("Caminho"), sg.Button("Salvar")],
        [sg.Button("Voltar", size=(15,5))]
    ]
    return sg.Window("Configuraçoes", layout=config, finalize=True)

def JanelaEnvRet():
    EnvRet = [
        [sg.Button("Enviar", size= (15,7))],
        [sg.Button("Receber", size= (15,7))],
        [sg.Button("Extrato", size= (15,7))],
        [sg.Button("Voltar")],

    ]
    return sg.Window("Enviar e Receber", layout=EnvRet, finalize=True)

def JanelaLogs():
    Logs = [
        [sg.Button("Log diario", size=(15,9)),sg.Button("Log semanal", size=(15,9))],
        [sg.Button("log Mensal", size=(15,9)),sg.Button("Pasta de Logs", size=(15,9))],
        [sg.Button("Voltar")]
    ]
    return sg.Window("Janela de Logs", layout=Logs, finalize=True)
#cromtab
def JanelaStatus():
    Status = [
    ]
    return sg.Window("Janela de Status", layout=Status, finalize=True)

# JANELA
janela1, janela2, janela_con, janela_env_ret, janela_logs = JanelaLogin(), None, None, None, None


# LER OS EVENTOS

while True:
    janela, eventos, valores = sg.read_all_windows()
    # Quando fechar a janela
    if janela == janela1 and eventos == sg.WIN_CLOSED:
        break
    if janela == janela2 and eventos == sg.WIN_CLOSED:
        break
    if janela == janela_con and eventos == sg.WIN_CLOSED:
        break
    if janela == janela_env_ret and eventos == sg.WINDOW_CLOSED:
        break
    if janela == janela_logs and eventos == sg.WINDOW_CLOSED:
        break
    # Quando ir para a proxima janela
    if janela == janela1 and eventos == "Entrar":
        if valores["usuario"] == "eduardo" and valores["senha"] == "unigloves":
            janela2 = JanelaMenu()
            janela1.hide()

        elif valores["usuario"] != "eduardo" or valores["senha"] != "unigloves":
            sg.Popup("Nome de usuario e/ou senha incorretos")

 # Caminho entre as janelas
    #Voltando para a tela de login
    if janela == janela2 and eventos == "Deslogar":
        janela2.hide()
        janela1.un_hide()
    if janela == janela_con and eventos == "Voltar":
        janela_con.hide()
        janela2.un_hide()

    # Indo para as Configs
    if janela == janela2 and eventos == "Configuracoes":
        janela_con = JanelaConfig()
        janela_con.un_hide()
        janela2.hide()

    # Indo para Enviar e Receber
    if janela == janela2 and eventos == "Enviar e Receber":
        janela_env_ret = JanelaEnvRet()
        janela_env_ret.un_hide()
        janela2.hide()

    # Entrando na janela de Logs
    if janela == janela2 and eventos == "Logs":
        janela_logs = JanelaLogs()
        janela_logs.un_hide()
        janela2.hide()






    # Enviando um arquivo Manualmente
    if janela == janela_env_ret and eventos == "Enviar":
        Env = [
            [sg.popup_get_file(title="Arquivo", message=("Qual seria o arquivo?"))],
            [sg.popup_get_folder(title="Banco", message=("Para qual banco deseja enviar?"))]
        ]
    # Recebendo um arquvi Manualmente

    # Solicitando um Extrato

    # Selecionando a data dos Logs

