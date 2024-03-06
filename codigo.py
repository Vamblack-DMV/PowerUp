# Passo a Passo do Projeto
# Passo 1: Entrar no sistema da Empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login
    # biblioteca de automação: pyautogui
        #instalação da biblioteca: pip install pyautogui

# Importando as bibliotecas
import pyautogui
import time

pyautogui.PAUSE = 2
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.write -> escrever um texto
# pyautogui.press -> pressionar 1 tecla do teclado

# pyaytogui.hotkey("ctrl","v")

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.write(link)
pyautogui.press("enter")

# Dar uma pausa esclusiva
time.sleep(5)

# Passo 2: Fazer Login

    # Acessar e digitar campo login
pyautogui.press("tab") 
pyautogui.write ("daluservicos@gmail.com")

    # Acessar e digitar campo senha
pyautogui.press("tab")
pyautogui.write("123456")

    # Acessar e clicar no botão de login
pyautogui.press("tab")
pyautogui.press("enter")

# Passo 3: Importar a base de dados
    # Instalando a biblioteca Pandas, para trabalho com base de dados
    # pip install pandas numpy openpyxl
import pandas
tabela = pandas.read_csv("produtos.csv")

# Imprime a tabela importada do arquivo no prompt
print (tabela)

# Passo 4: Cadastrar 1 produto

# Cadastrando cada linha da tabela
for linha in tabela.index:

    # Acessar o campo e escrever Código do Produto
    pyautogui.click(x=567, y=287)
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    
    # Acessar o campo e escrever Marca
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"marca"]))

    # Acessar o campo e escrever Tipo
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"tipo"]))

    # Acessar o campo e escrever Categoria
    pyautogui.press("tab")
    categoria = tabela.loc[linha,"categoria"]    
    pyautogui.write(str(categoria))

    # Acessar o campo e escrever Preço Unitário
    pyautogui.press("tab")   
    pyautogui.write(str(tabela.loc[linha,"preco_unitario"]))

    # Acessar o campo e escrever Custo
    pyautogui.press("tab")   
    pyautogui.write(str(tabela.loc[linha,"custo"]))

    # Acessar o campo e escrever Observação
    pyautogui.press("tab")
    obs = tabela.loc[linha,"obs"]
    # Verificando se o campo está vazio
    if not pandas.isna:
        pyautogui.write(str(obs))

    # Acessar o botão e enviar o cadastro
    pyautogui.press("tab")
    pyautogui.press("enter")
    # pyautogui.press("PgUp")
    pyautogui.scroll(10000)

# Passo 5: Repetir o processo de cadastro até acabar a base de dados