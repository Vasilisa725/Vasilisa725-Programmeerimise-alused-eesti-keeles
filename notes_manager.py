from bs4 import BeautifulSoup
import requests

url = input('Sisesta URL (sisesta http:// või https://): ')
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")
headings = []

for i in range(1, 7):
    for heading in soup.find_all(f"h{i}"):
        headings.append(heading.text.strip())
        print(f"Leitud H{i}: {heading.text.strip()}")

print("Leitud kokku {} pealkirja.".format(len(headings)))







