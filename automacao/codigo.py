import pyautogui
import time
import pandas

# Define uma pausa padrão entre cada comando do PyAutoGUI
pyautogui.PAUSE = 0.4

# --- Abrindo o navegador e acessando o site de login ---

pyautogui.press('win')  # Pressiona a tecla Windows para abrir o menu iniciar
pyautogui.write('chrome')  # Digita 'chrome' para buscar o navegador
time.sleep(1)  # Aguarda o carregamento da busca
pyautogui.press("enter")  # Pressiona Enter para abrir o Chrome

# Aguarda o navegador abrir e clica na barra de endereços (ajuste a coordenada conforme sua tela)
pyautogui.click(x=883, y=609)

# Digita a URL do sistema
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")  # Pressiona Enter para acessar o site

time.sleep(1)  # Aguarda o site carregar

# --- Preenchendo login e senha ---

pyautogui.click(x=806, y=411)  # Clica no campo de e-mail (ajust

pyautogui.write("elielidniz@gomal.com")  # Escreve o e-mail

pyautogui.press("tab")  # Vai para o campo de senha

pyautogui.write("elieldiniz")  # Escreve a senha

pyautogui.press("tab")  # Vai para o botão de login
pyautogui.press("enter")  # Pressiona Enter para logar

time.sleep(3)  # Aguarda o login e o carregamento da próxima página

# --- Lendo os dados do arquivo CSV com pandas ---

tabela = pandas.read_csv("produto.csv")  # Lê o arquivo CSV com os produtos

# --- Preenchendo o formulário com os dados do CSV ---

for linha in tabela.index:
    # Clica no primeiro campo do formulário para iniciar o preenchimento (ajuste a coordenada se necessário)
    pyautogui.click(x=847, y=292)

    # Preenche os campos um por um usando os dados da linha atual da tabela

    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    # Verifica se existe alguma observação na célula e escreve, se houver
    obs = str(tabela.loc[linha, "obs"])
    if obs.lower() != "nan":  # Verifica se não está vazio
        pyautogui.write(obs)

    # Envia o formulário
    pyautogui.press("tab")
    pyautogui.press("enter")

    # Sobe a página para ver o topo do formulário novamente
    pyautogui.scroll(10000)

    129.9   