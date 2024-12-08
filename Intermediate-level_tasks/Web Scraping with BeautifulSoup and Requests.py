import requests
from bs4 import BeautifulSoup

def scrape_news(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract news headlines (example: headlines within <h2> tags)
        headlines = soup.find_all('h2')

        print("Latest News Headlines:")
        for headline in headlines:
            print(headline.get_text())
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")

# Example usage
scrape_news('https://example.com/news')
