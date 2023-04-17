import requests
from bs4 import BeautifulSoup

contador = 0

# Abrir el archivo de texto para escribir la salida
with open('salida.txt', 'w') as file:

    # Leer los enlaces desde un archivo de texto
    with open('enlaces.txt', 'r') as f:
        enlaces = [line.strip() for line in f]

    for url in enlaces:

        contador += 1
        # Reemplazar 'peakd.com' por 'ecency.com' en el enlace si es necesario
        ecency_url = url.replace('peakd.com', 'ecency.com')
        response = requests.get(ecency_url)
        soup = BeautifulSoup(response.content, 'html.parser')

        try:
            # Obtener el nombre de usuario
            username = soup.find('span', class_='author-name').text.strip()

            # Obtener el título del artículo
            title = soup.find('meta', property='og:title')['content']

            # Obtener la URL de la imagen principal
            image_url = soup.find('meta', property='og:image')['content']

            # Escribir la salida en el archivo de texto
            file.write(f"""
#### Post #{contador}

---

{image_url}

---



[{title}]({url})
by @{username}

---

""")

            # Imprimir la salida en la consola
            print(f"""
#{contador}
Usuario: {username}
Título del Post: {title}
Url de la imagen: {image_url}
---
""")

            # Escribir el enlace original en la salida
            print(f"Original Link: {url}\n")

        except Exception as e:
            # Manejar los errores y escribirlos en el archivo de texto
            print(f"Error procesando el enlace {ecency_url}: {e}\n")

    print("La salida se ha generado exitosamente en el archivo 'salida.txt'")
