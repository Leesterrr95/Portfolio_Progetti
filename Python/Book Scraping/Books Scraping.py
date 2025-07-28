# Librerie per fare scraping, parsing HTML e salvare dati in CSV
import requests
from bs4 import BeautifulSoup as bs
import re
import pandas as pd

# Intestazioni HTTP per simulare un browser reale ed evitare blocchi dal sito
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    "Accept-Language": "it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Referer": "https://www.google.com/",
    "Connection": "keep-alive",
}

# Lista per raccogliere i dati di tutti i libri
libri = []

# Loop attraverso le 50 pagine del catalogo
for i in range(1, 51):
    print(f"Analizzo pagina {i}")

    # Scarica il contenuto HTML della pagina corrente
    pagina_iniziale = requests.get(
        f"https://books.toscrape.com/catalogue/page-{i}.html"
    )
    # Parsing del contenuto HTML della pagina
    soup = bs(pagina_iniziale.content, features="lxml")
    # Ricava il link relativo alla pagina del libro e costruisci l'URL completo
    titoli = soup.find_all("div", class_="image_container")
    for titolo in titoli:
        relative_url = titolo.find("a")["href"]
        relative_url = relative_url.replace("../../../", "")
        book_url = f"https://books.toscrape.com/catalogue/{relative_url}"
        # Richiedi la pagina dettagliata del libro
        r2 = requests.get(book_url, headers=headers)
        soup_book = bs(r2.content, "lxml")
        # Ricavare le informazioni di tutti i libri
        try:
            # Trova la sezione principale con le info del libro
            product_page = soup_book.find("article", class_="product_page")
            if not product_page:
                raise ValueError("Nessun articolo trovato nella pagina del libro")
            # Estrai le informazioni principali: titolo, prezzo, disponibilità, descrizione
            titolo_tag = product_page.find("h1")
            price_tag = product_page.find("p", class_="price_color")
            stock_tag = product_page.find("p", class_="instock availability")
            description_tag = product_page.find("div", class_="sub-header")
            rating_tag = rating = product_page.find("p", class_="star-rating")
            categoria_tag = soup_book.find("ul", class_="breadcrumb")

            # Verifica che tutte le info siano presenti
            if not all([titolo_tag, price_tag, stock_tag, description_tag]):
                raise ValueError("Alcuni elementi chiave non trovati nella pagina")

            # Estrai i testi da ogni tag
            titolo_libro = titolo_tag.get_text()
            price = price_tag.get_text()
            stock = stock_tag.get_text().strip()

            description = description_tag.find_next("p").get_text()
            classes = rating["class"]
            rating = classes[1]
            word_to_number = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
            numeric_rating = word_to_number[rating]
            categoria = categoria_tag.find_all("a")[-1].get_text()

            # Salva le informazioni in un dizionario
            prodotto_info = {
                "Titolo": titolo_libro,
                "Prezzo": price,
                "Stock": stock,
                "Descrizione": description,
                "Rating": numeric_rating,
                "Categoria": categoria,
            }
            libri.append(prodotto_info)

        except Exception as e:
            print(f"Errore di pagina {i} - libro {book_url}: {e}")
            continue  # Passa al libro successivo se c'è un errore

        # Crea un DataFrame con tutti i dati raccolti e salvalo in CSV
df = pd.DataFrame(libri)
print(df.head())
df.to_csv("Libri totali.CSV", index=False)
