# Automatizacion de un chat en Whatsapp

Herramienta que automatiza el envío de mensajes en WhatsApp utilizando Selenium. El codigo lee el archivo .txt y lo envia al nombre del CONTACTO que se especifica en el "target". Hay que anadir el numero a los contactos. 

## Tecnologías Utilizadas

Python
Selenium: Biblioteca de automatización de navegadores web.
ChromeDriver: Controlador específico para Google Chrome.


## Instalación

1. Python

2. ChromeDriver:
Descarga el archivo ejecutable de ChromeDriver compatible con tu versión de Google Chrome desde aquí.
Coloca el archivo chromedriver.exe en la misma carpeta que tu script main.py.

3. Dependencias:
Instala las dependencias necesarias ejecutando el siguiente comando en la terminal:
pip install selenium

## Uso

1. Abre el archivo main.py y configura las siguientes variables:
target: Número de teléfono del contacto de WhatsApp al que deseas enviar mensajes.
message: El mensaje que deseas enviar.
number_of_times: Número de veces que deseas enviar el mensaje.

2. Ejecuta el script:
python main.py

