import requests
from bs4 import BeautifulSoup
import csv

# URL to scrape
url = 'https://example.com'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract data (example for extracting headings)
headings = soup.find_all('h2')

# Save data to CSV
with open('headings.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Heading'])
    for heading in headings:
        writer.writerow([heading.get_text()])

print("Data saved to headings.csv")
