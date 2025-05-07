# projekt_3_ENGETO
Třetí projekt na Python Akademii od Engeta.

# Popis projektu
Tento projekt slouží k extrahování výsledků voleb v roce 2017.
Skript stahuje výsledky voleb v roce 2017.

# INSTALACE KNIHOVEN
Knihovny, které jsou použity v kódu jsou uložené v souboru requirements.txt. 
Pro instalaci použít virtuální prostředí a spustit

![image](https://github.com/user-attachments/assets/a76b2758-a5d9-4bc5-9a6c-f154a5acbb01)


pip install -r requirements.txt

# Spuštění projektu
Skript main.py se spouští z příkazového řádku a očekává dva argumenty:
1. URL adresa s výběrem okrsku
2. Jméno výstupního .csv souboru

# Ukázka spuštění
![image](https://github.com/user-attachments/assets/1b4b7ae5-8245-4d03-9c8d-c52b7cc19813)

python main.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=8&xnumnuts=5203" vysledky_nachod.csv

Po spuštění se data uloží do zadaného CSV souboru.

# Ukázka projektu

1. Argument https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=8&xnumnuts=5203
2. Argument vysledky_nachod.csv

# Průběh skriptu
![image](https://github.com/user-attachments/assets/a6347669-dcf0-415d-a41e-33dc3b048ffd)
![image](https://github.com/user-attachments/assets/58b64c7e-9b0c-4ff0-b49d-e12b14875233)


# Ukázka výstupu (CSV)
![image](https://github.com/user-attachments/assets/2e6842db-7135-4029-93e3-36ccb9b14864)









