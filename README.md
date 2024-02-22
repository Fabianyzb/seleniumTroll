
Automatización de un chat en WhatsApp
Herramienta que automatiza el envío de mensajes en WhatsApp utilizando Selenium. El código lee el archivo .txt y lo envía al número de teléfono que se especifica en el "target".

Tecnologías Utilizadas
Python: Lenguaje de programación utilizado para escribir el script.
Selenium: Biblioteca de automatización de navegadores web.
ChromeDriver: Controlador específico para Google Chrome.

Instalación
Python

ChromeDriver: Descarga el archivo ejecutable de ChromeDriver compatible con tu versión de Google Chrome desde aquí. Coloca el archivo chromedriver.exe en la misma carpeta que tu script main.py.

Dependencias: Instala las dependencias necesarias ejecutando el siguiente comando en la terminal: pip install selenium

Uso
Abre el archivo main.py y configura las siguientes variables: target: Número de teléfono del contacto de WhatsApp al que deseas enviar mensajes. message: El mensaje que deseas enviar. number_of_times: Número de veces que deseas enviar el mensaje.

Ejecuta el script: python main.py