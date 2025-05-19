from bs4 import BeautifulSoup
import requests
from colorama import Fore
import emoji

url = input('Sisesta URL (sisesta http:// või https://): ')
print(Fore.CYAN + "Tere tulemast, kasutaja!" + Fore.RESET)

response = requests.get(url)
html = response.text

meeleolud = {
    'rahulik': (Fore.GREEN, emoji.emojize(":deciduous_tree:")),
    'närviline': (Fore.RED, emoji.emojize(":face_with_symbols_on_mouth:")),
    'uudishimulik': (Fore.YELLOW, emoji.emojize(":magnifying_glass_tilted_left:")),
    'unine': (Fore.BLUE, emoji.emojize(":zzz:"))
}

soup = BeautifulSoup(html, "html.parser")

print("Vali oma meeleolu järgmiste valikute hulgast:")
for idx, mood in enumerate(meeleolud.keys(), start=1):
    print(f"{idx}. {mood.capitalize()}")

valik = int(input("Sisesta oma meeleolu number (1-4): "))
headings = []

for i in range(1, 7):
    for heading in soup.find_all(f"h{i}"):
        headings.append(heading.text.strip())
        print(f"Leitud H{i}: {heading.text.strip()}")

if 1 <= valik <= 4:
    meeleolu = list(meeleolud.keys())[valik - 1]
    color, emoticon = meeleolud[meeleolu]
    print(color + f"Sa oled {meeleolu}!" + Fore.RESET)
    print(f"Sõnum: {emoticon}")
else:
    print(Fore.RED + "Tundub, et sisestasite vale numbri! Palun valige number vahemikus 1-4." + Fore.RESET)

print("Leitud kokku {} pealkirja.".format(len(headings)))




