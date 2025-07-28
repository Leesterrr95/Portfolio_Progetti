# Book Scraper - books.toscrape.com

Uno script Python per raccogliere automaticamente informazioni da [Books to Scrape](https://books.toscrape.com), un sito dedicato al web scraping didattico. Il progetto estrae dati come titolo, prezzo, disponibilità, rating, descrizione e categoria per ciascun libro.

---

## Tecnologie usate

- `Python 3`
- `requests` – per inviare richieste HTTP
- `BeautifulSoup (bs4)` – per analizzare il contenuto HTML
- `pandas` – per gestire ed esportare i dati
- `lxml` – parser HTML veloce e compatibile

---

##  Cosa fa lo script

 Analizza **50 pagine** del catalogo  
 Accede alla **pagina dettagliata** di ciascun libro  
 Estrae:
- Titolo
- Prezzo
- Disponibilità
- Descrizione
- Rating (convertito da parole a numeri)
- Categoria

 Esporta i dati in un file CSV: `Libri totali.CSV`

---

##  Come usarlo

1. Clona la repo o copia il file `.py` nel tuo ambiente.
2. Installa i pacchetti richiesti (se non li hai già):


