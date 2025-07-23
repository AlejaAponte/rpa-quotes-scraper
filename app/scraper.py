import requests
from bs4 import BeautifulSoup

from app.database import SessionLocal, init_db
from app.models import Quote, Tag

BASE_URL = "https://quotes.toscrape.com"

def scrape_and_save():
    init_db()
    db = SessionLocal()
    page = 1

    while True:
        print(f"Scraping page {page}...")
        url = f"{BASE_URL}/page/{page}/"
        response = requests.get(url)
        if response.status_code != 200:
            break

        soup = BeautifulSoup(response.text, 'html.parser')
        quote_elements = soup.find_all('div', class_='quote')
        if not quote_elements:
            break

        for elem in quote_elements:
            text = elem.find('span', class_='text').get_text(strip=True)
            author = elem.find('small', class_='author').get_text(strip=True)
            tag_names = [tag.get_text(strip=True) for tag in elem.find_all('a', class_='tag')]

            # Evitar duplicados
            if db.query(Quote).filter_by(text=text).first():
                continue

            quote = Quote(text=text, author=author)

            for tag_name in tag_names:
                tag = db.query(Tag).filter_by(name=tag_name).first()
                if not tag:
                    tag = Tag(name=tag_name)
                quote.tags.append(tag)

            db.add(quote)

        db.commit()
        page += 1

    db.close()
    print("Scraping y guardado completado.")

if __name__ == "__main__":
    scrape_and_save()
