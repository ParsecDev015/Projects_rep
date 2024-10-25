from newspaper import Article
import json
import os
from gtts import gTTS


class ArticleManager:
    def __init__(self):
        self.saved_articles = []

    def get_article(self, url):
        try:
            info_article = Article(url, language='es')
            print("Getting article....")
            info_article.download()
            info_article.parse()
            article = info_article.text

            if not article.strip():
                print("Error: The article is empty or could not be parsed.")
                return None

            self.saved_articles.append(article)
            return article
        except Exception as e:
            print(f"Error retrieving the article: {e}")
            return None

    def show_saved_articles(self):
        print("Articulos guardado: ")
        return print(self.saved_articles)

class AudioConverter:
    @staticmethod
    def transform_text_to_audio(article):
        if article:
            myobj = gTTS(text=article, lang="es", slow=False)
            myobj.save("articulo_a_texto.mp3")
            print("Reproduciendo audio....")
            os.system("start articulo_a_texto.mp3")
        else:
            print("No text available to convert to audio.")


def cargar_texto_desde_json(filename):
     with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data["Texto"]

print("--------Voice to text 0.01 by Will----------")

while True:
    entry = input("Dear user please select with the numbers"
                  " one of the two available options (1.Make voice from json file, 2.Make voice from url, 3.Saved articles, 4.Exit)\n")
    
    if entry == "1":
        json_input = input("Ingrese el nombre del archivo: \n")
        # Cargar texto desde el archivo JSON y convertirlo en audio
        texto_json = cargar_texto_desde_json(json_input)
        AudioConverter.transform_text_to_audio(texto_json)


    if entry == "2":
        url_input = input("Dear user please enter the url to format into voice: \n")
        
        # Crear una instancia de ArticleManager
        manager = ArticleManager()
        
        # Obtener el artículo de la URL
        articulo = manager.get_article(url_input)

        # Convertir el texto a audio
        if articulo:
            AudioConverter.transform_text_to_audio(articulo)
        else:
            print("No se pudo obtener el artículo para convertirlo a audio.")

    elif entry == "3":
         manager = ArticleManager()

         info = manager.show_saved_articles()
         
    elif entry == "4":
        print("Saliendo......")
        break
        
