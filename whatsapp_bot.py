#whatsapp_bot
#name_tutorial:Como Criar Um Bot(Robô) No Whatsapp de mensagens P/ Grupos e Contatos
#link_tutorial:https:\www.youtube.com/watch?v=_ZDBVeqyK6g


#importar as bibliotecas
from selenium import webdriver
import time as t
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

#navegar até o whatsapp web
# driver = webdriver.Chrome(ChromeDriverManager().install())
# operadriver='C://Users//diego//OneDrive//Desktop//DESKTOP//PROGRAMAS//MOZILA//geckodriver.exe'
# operadriver='C:\Users\diego\OneDrive\Desktop\DESKTOP\PROGRAMAS\MOZILA\geckodriver.exe'
# chromedriver='C://Users//diego//OneDrive//Desktop//DESKTOP//PROGRAMAS//WEB_DRIVERS//CHROME_DRIVER//chromedriver.exe'
driver = webdriver.Firefox()
driver.get('https:\web.whatsapp.com')
driver.set_window_position(166,-700)
driver.maximize_window()
t.sleep(30)
# time.sleep(30)

#definir contatos, grupos e mensagem a ser enviada
contatos = ['Lucimar Brito','+55 62 9259-1138']
mensagem = 'Olá. Sou um robô. Essa mensagem é automatizada'
#buscar contatos/grupos
def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath(
        '//div[contains(@class,"copyable-text selectable-text")]')
    t.sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)

def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_elements_by_xpath(
        '//div[contains(@class,"copyable-text selectable-text")]')
    campo_mensagem[1].click()
    t.sleep(3)
    campo_mensagem[1].send_keys(mensagem)
    campo_mensagem[1].send_keys(Keys.ENTER)



for contato in contatos:
    buscar_contato(contato)
    enviar_mensagem(mensagem)
#campo de pesquisa 'copyable-text selectable-text'
#campo de mensagem privada 'copyable-text selectable-text'
#enviar mensagens para os contados/grupos



#test of alteration(problems in VSCode)
