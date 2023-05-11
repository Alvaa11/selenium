from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

navegador.get('https://web.whatsapp.com/')
sleep(10)
navegador.find_element('xpath', '//*[@id="pane-side"]/div[1]/div/div/div[9]/div/div/div/div[2]/div[1]/div[1]/span').click()
sleep(20)
navegador.find_element('xpath', '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys('Bom dia! O sol já nasceu la na fazendinha, acorda o bezerro e a vaquinha. Que já cocoricou dona galinha. Levanta, que o pintinho já saiu da cama e o porquinho já caiu na lama. Lá na fazendinha é manhã e num sei mais oq tem lá... levanta ai na moral')
sleep(1)
navegador.find_elements('xpath', '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()