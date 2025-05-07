"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie

author: Jakub Prajzler
email: prajzler25@gmail.com
"""

import sys
import requests
from bs4 import BeautifulSoup
import csv

def download_html(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Chyba při stahování: {response.status_code}")
        sys.exit(1)
    return BeautifulSoup(response.text, "html.parser")

def get_villages(soup):
    tables = soup.find_all("table", class_="table")
    rows = []
    for table in tables:
        rows += table.find_all("tr")[2:]

    villages = []
    for row in rows:
        cells = row.find_all("td")
        if len(cells) < 2:
            continue
        code = cells[0].text.strip()
        name = cells[1].text.strip()
        relative_link = cells[0].find("a")["href"]
        full_link = f"https://www.volby.cz/pls/ps2017nss/{relative_link}"
        villages.append((code, name, full_link))
    return villages

def process_village(code, name, url):
    soup = download_html(url)
    t1 = soup.find_all("table")[0]
    t2 = soup.find_all("table")[1]

    registered = t1.find_all("td")[3].text.replace('\xa0', '').strip()
    envelopes = t1.find_all("td")[6].text.replace('\xa0', '').strip()
    valid = t2.find_all("td")[6].text.replace('\xa0', '').strip()

    parties = {}
    for table in soup.find_all("table")[1:]:
        rows = table.find_all("tr")[2:]
        for row in rows:
            cells = row.find_all("td")
            if len(cells) >= 2:
                party = cells[1].text.strip()
                votes = cells[2].text.replace('\xa0', '').strip()
                parties[party] = votes

    return {
        "code": code,
        "name": name,
        "registered": registered,
        "envelopes": envelopes,
        "valid": valid,
        "parties": parties
    }

def save_to_csv(filename, data, all_parties):
    headers = ["code", "location", "registered", "envelopes", "valid"] + all_parties
    with open(filename, mode="w", newline='', encoding="utf-8-sig") as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(headers)
        for row in data:
            line = [row["code"], row["name"], row["registered"], row["envelopes"], row["valid"]]
            line += [row["parties"].get(party, "0") for party in all_parties]
            writer.writerow(line)

def main():
    if len(sys.argv) != 3:
        print("Chyba: Zadej 2 argumenty - odkaz a název výstupního souboru")
        print("Použití: python main.py <URL> <vystup.csv>")
        sys.exit(1)

    url = sys.argv[1]
    filename = sys.argv[2]

    print(f"Stahuji data z: {url}")
    soup = download_html(url)
    villages = get_villages(soup)

    print(f"\n Nalezeno obci: {len(villages)}\n")
    all_parties = set()
    village_data = []

    for i, (code, name, link) in enumerate(villages, start=1):
        print(f"({i}/{len(villages)}) Zpracovávám: {name}")
        result = process_village(code, name, link)
        all_parties.update(result["parties"].keys())
        village_data.append(result)

    save_to_csv(filename, village_data, sorted(all_parties))
    print(f"\n Hotovo! Data byla uložena do souboru: '{filename}'")

if __name__ == "__main__":
    main()