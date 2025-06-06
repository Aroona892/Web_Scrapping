# 🎬 IMDb Review Scraper (Selenium)

This Python script uses **Selenium** to scrape user **ratings and reviews** from an IMDb movie's review page (specifically "The Mandalorian"). It automates browser interaction to repeatedly click the “Load More” button, extracting all available reviews.

---

## 🔍 Features

- 🔁 Automatically loads all review pages using the “Load More” button
- ⭐ Extracts **user ratings**
- 📝 Extracts full **review text**
- 🧾 Saves data into a structured `Pandas DataFrame`
- 📷 Captures a screenshot of the initial reviews page

---

## 🛠 Tech Stack

- `Python`
- `Selenium`
- `pandas`
- `Chromedriver`

---

## 🚀 How to Run

1. Make sure you have [ChromeDriver](https://chromedriver.chromium.org/downloads) installed and path set correctly.
2. Install dependencies:
```bash
pip install selenium pandas
