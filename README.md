# projekt_3_ENGETO
Třetí projekt na Python Akademii od Engeta.

# Popis projektu
Tento projekt slouží k extrahování výsledků voleb v roce 2017.
Skript stahuje výsledky voleb v roce 2017.

# INSTALACE KNIHOVEN
Knihovny, které jsou použity v kódu jsou uložené v souboru requirements.txt. 
Pro instalaci použít virtuální prostředí a spustit

![image](https://github.com/user-attachments/assets/d15350c6-4161-430e-b69b-c082ef11b10e)

pip install -r requirements.txt

# Spuštění projektu
Skript main.py se spouští z příkazového řádku a očekává dva argumenty:
1. URL adresa s výběrem okrsku
2. Jméno výstupního .csv souboru

# Ukázka spuštění
![image](https://github.com/user-attachments/assets/ab5453d1-81c0-407a-af6b-6dd75fe624ed)

python main.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=8&xnumnuts=5203" vysledky_nachod.csv

Po spuštění se data uloží do zadaného CSV souboru.

# Ukázka projektu

1. Argument https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=8&xnumnuts=5203
2. Argument vysledky_nachod.csv

# Průběh skriptu
![image](https://github.com/user-attachments/assets/80e0c3f6-aea5-4721-9900-4f11ca8291c6)
![image](https://github.com/user-attachments/assets/58b64c7e-9b0c-4ff0-b49d-e12b14875233)


# Ukázka výstupu (CSV)
![image](https://github.com/user-attachments/assets/c34286b0-ab31-4d7f-ade7-4acce588b10b)








