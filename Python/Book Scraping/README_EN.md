#  Book Scraper – books.toscrape.com

A Python script to automatically collect book data from [Books to Scrape](https://books.toscrape.com), a website built for educational web scraping.  
The project extracts details such as title, price, availability, rating, description, and category for each book.

---

##  Technologies Used

- `Python 3`
- `requests` – to send HTTP requests
- `BeautifulSoup (bs4)` – to parse the HTML content
- `pandas` – to manage and export data
- `lxml` – fast and compatible HTML parser

---

##  What the Script Does

 Scans **50 pages** of the book catalog  
 Accesses the **detail page** of each book  
 Extracts:
- Title  
- Price  
- Availability  
- Description  
- Rating (converted from words to numbers)  
- Category  

 Exports all data into a CSV file: `Libri totali.CSV`

---

##  How to Use

1. Clone the repo or copy the `.py` file to your environment  
2. Install the required packages (if you haven’t already):

```bash
pip install requests beautifulsoup4 pandas lxml
