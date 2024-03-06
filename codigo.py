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

pyautogui.press("tab") 
pyautogui.write ("daluservicos@gmail.com")
pyautogui.press("tab")
pyautogui.write("123456")
pyautogui.press("tab")
pyautogui.press("enter")

# Passo 3: Importar a base de dados
# Passo 4: Cadastrar 1 produto
# Passo 5: Repetir o processo de cadastro até acabar a base de dados