from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time



options=webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:/Users/fabia/AppData/Local/Google/Chrome/User Data")
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
wait=WebDriverWait(driver,100)

target='"Estafa"'
message="hola como estas, esto es una prueba desde message"
number_of_times=20 #No. of times to send a message


#Lectura de archivo txt
# Abre el archivo en modo lectura
with open('text.txt', 'r') as archivo:
    contenido = archivo.read()

# Imprime el contenido (esto es opcional, solo para verificar)
print(contenido)

contact_path='//span[contains(@title,'+ target +')]'
contact=wait.until(EC.presence_of_element_located((By.XPATH,contact_path)))
contact.click()
message_box_path='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
message_box=wait.until(EC.presence_of_element_located((By.XPATH,message_box_path)))
for x in range(number_of_times):
    message_box.send_keys(contenido + Keys.ENTER)
    time.sleep(0.2)


input("Presiona Enter para cerrar el navegador...")
driver.quit()