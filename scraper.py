import requests
from bs4 import BeautifulSoup
import pymysql
import os
import django
from urllib.parse import urljoin

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

# ------------------ بخش ۱: Scraping ------------------
base_url = 'http://books.toscrape.com/catalogue/page-1.html'
response = requests.get(base_url)
soup = BeautifulSoup(response.text, 'html.parser')

books = []

for article in soup.find_all('article', class_='product_pod'):
    title = article.h3.a['title']
    price = article.find('p', class_='price_color').text.strip().replace('£', '').replace('Â', '')
    price = float(price)
    rating = article.p.get('class')[1]
    image_relative_url = article.find('img')['src']
    image_url = urljoin('http://books.toscrape.com/', image_relative_url)
    books.append((title, price, rating, image_url))

# ------------------ بخش ۲: ذخیره در MySQL ------------------

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='Mani5530',     # رمز MySQL خودت
    database='mybookstore',
    charset='utf8mb4'
)

try:
    with connection.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(255),
                price DECIMAL(10, 2),
                rating VARCHAR(10),
                image_url TEXT
            )
        """)

        for book in books:
            try:
                cursor.execute(
                   "INSERT INTO books (title, price, rating, image_url) VALUES (%s, %s, %s, %s)",
                    book
                )
            except Exception as e:
                print(f"Error inserting {book}: {e}")

    connection.commit()
    print("✅ اطلاعات با موفقیت ذخیره شد.")
finally:
    connection.close()
