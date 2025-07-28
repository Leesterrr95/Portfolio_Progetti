import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

# Simula una richiesta da browser per evitare blocchi dal sito
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    "Accept-Language": "it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Referer": "https://www.google.com/",
    "Connection": "keep-alive",
}

libri = []

# Loop attraverso 50 pagine del catalogo libri
for i in range(1, 51):
    print(f"Analizzo pagina {i}")
    response = requests.get(f"https://books.toscrape.com/catalogue/page-{i}.html")
    soup = bs(response.content, "lxml")

    # Trova tutti i contenitori dei link ai libri
    titoli = soup.find_all("div", class_="image_container")

    for titolo in titoli:
        # Costruzione URL completo della pagina del singolo libro
        relative_url = titolo.find("a")["href"].replace("../../../", "")
        book_url = f"https://books.toscrape.com/catalogue/{relative_url}"

        try:
            # Richiesta della pagina dettagliata del libro
            r2 = requests.get(book_url, headers=headers)
            soup_book = bs(r2.content, "lxml")

            product_page = soup_book.find("article", class_="product_page")
            if not product_page:
                raise ValueError("Nessun articolo trovato nella pagina del libro")

            # Estrazione delle informazioni principali
            titolo_libro = product_page.find("h1").get_text()
            price = product_page.find("p", class_="price_color").get_text()
            stock = product_page.find("p", class_="instock availability").get_text(
                strip=True
            )
            description = (
                product_page.find("div", class_="sub-header").find_next("p").get_text()
            )

            # Conversione del rating da parola a numero
            rating_classes = product_page.find("p", class_="star-rating")["class"]
            word_to_number = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
            numeric_rating = word_to_number.get(rating_classes[1], 0)

            # Estrazione della categoria (ultimo elemento nel breadcrumb)
            categoria = (
                soup_book.find("ul", class_="breadcrumb").find_all("a")[-1].get_text()
            )

            # Salvataggio dei dati in dizionario
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
            print(f"Errore pagina {i} - libro {book_url}: {e}")
            continue

# Esportazione dei dati in CSV
df = pd.DataFrame(libri)
print(df.head())
df.to_csv("Libri totali.CSV", index=False)
