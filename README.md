 -- Engeto-pa-3-projekt
	Třetí projekt na python Akademii od Engeta

 -- POPIS PROJEKTU
	Tento projekt slouží k extrahování výsledků z parlamentních voleb v roce 2017.
	Skript stahuje výsledky voleb v roce 2017.

 -- INSTALACE KNIHOVEN
	Knihovny, které jsou použity v kódu jsou uložené v souboru requirements.txt. 
	Pro instalaci knihoven použít virtuální prostředí a spustit

	### 	pip install -r requirements.txt 	###

 -- SPUŠTĚNÍ PROJEKTU
	Skript main.py se spouští z příkazového řádku a očekává argumenty
		1. URL adresa s výběrem okrsku
		2. Jméno výstupního .csv souboru

 -- UKÁZKA SPUŠTĚNÍ

	### 	python main.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=8&xnumnuts=5203" vysledky_nachod.csv	###

	Po spuštění se data uloží do zadaného CSV souboru.

 -- ARGUMENTY 
	1. argument https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=8&xnumnuts=5203
	2. argument vysledky_nachod.csv


