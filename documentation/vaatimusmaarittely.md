# Vaatimusmäärittely

## Sovelluksen tarkoitus

Jumpman on tasohyppely peli joka on sivulle rullaavalla ruudulla toteutettu Pythonin pygame kirjastoa käyttävä peli. Peli sisältää kerättäviä kolikoita ja artifakteja. Pelin tavoitteena on päästä pelattavan kentän loppuun ottamatta osumaa vihollisista ja samalla keräten kolikoita ja artifakteja. Pelissä on kaksi moodia, tavallinen pelimoodi jossa kentät voi läpäistä omaan tahtiin ja nopeusmoodi jossa on aikaraja.   

## Käyttöliittymäluonnos

Sovelluksella on kolme eri näkymää, ensimmäinen on valikko josta voidaan siirtyä eri pelimoodeihin,toinen on itse peli ja kolmas on highscore näkymä jossa on esitetty kenttien parhaat läpäisyajat.

Ensimmäinen ja kolmas näkymä ovat PySimpleGUI kirjastolla toteutettuja näkymiä ja itse pelinäkymä on pygame kirjastolla toteutettu.

![aloitusruutu](https://github.com/JuhoSiitonen/ot-harjoitustyo/blob/master/documentation/graphs/Jumpman%20k%C3%A4ytt%C3%B6liittym%C3%A4luonnos1.PNG)

![kakkosruutu](https://github.com/JuhoSiitonen/ot-harjoitustyo/blob/master/documentation/graphs/Jumpman%20highscore%20k%C3%A4ytt%C3%B6liittym%C3%A4luonnos2.PNG)

## Toiminnallisuudet

- [x] Käyttöliittymä joka mahdollistaa pelattavan kentän valinnan
- [x] Pelihahmo joka liikkuu 2D kentissä vasemmalle, oikealle ja ylös ja alas. 
- [x] Peli on sivusta kuvattu ja se koostuu kentistä.
- [x] Pelihahmo voi kerätä kolikoita ja artifakteja ja niiden määärä näkyy ruudulla.
- [x] Peli sisältää vihollisia jotka liikkuvat ennaltamäärättyjä reittejä pitkin. 
- [x] Pelihahmon osuessa viholliseen pelattu kenttä alkaa alusta. 
- [x] Peli sisältää kaksi pelimoodia
	- [x] Normaali pelimoodi jossa aikaa ei ole rajoitettu
	- [x] Time attack moodi jossa kenttien läpäisyyn käytettävissä oleva aika on rajoitettu
- [x] Peli pitää kirjaa pelaajan parhaista läpäisyajoista tietokannan muodossa joka on tallennettu paikallisen koneen levylle.

## Jatkokehitysideat

Mikäli edellä mainittujen toiminnallisuuksien jälkeen on vielä aikaa kurssin puitteissa seuraavia toiminnallisuuksia voidaan lisätä:

- Kentillä olisi oma musiikki joka soi pelin aikana.
- Kaksinpeli mahdollisuus yhdellä näppäimistöllä.
- Pelihahmon ja vihollisten sprite animaatiot liikkuessa.
- Kaksi tai useampi valittavaa vaikeusastetta.
- WYSIWYG kenttäeditori