# My Django Books

A simple Django project that scrapes book information from [Books to Scrape](http://books.toscrape.com) and saves it into a MySQL database.

---

## Features

- Scrapes book details (title, price, rating, image URL)
- Stores data in MySQL database
- Displays books styled as cards using CSS
- Built with Django for easy data management and display

---

## Installation and Setup

1. Clone the repository

```bash
git clone https://github.com/Mani8217/my-django-books.git
cd my-django-books



python3 -m venv myvenv
source myvenv/bin/activate   # On Linux/Mac
myvenv\Scripts\activate      # On Windows



pip install -r requirements.txt


python scraper.py


python manage.py runserver


Notes
Make sure MySQL is installed and running on your system.

Update your database credentials accordingly in the Django settings.

To scrape more pages or add features, modify the scraper.py script.

License
This project is licensed under the MIT License.
