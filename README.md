# Ohjelmistotekniikka

Repository for course **Ohjelmistotekniikka** weekly coding excercises and a **desktop application** made with *agile methods*.

# Harjoitustyö (Jumpman)

Jumpman on tasohyppely peli joka on sivulle rullaavalla ruudulla toteutettu Pythonin pygame ja PySimpleGUI kirjastoja käyttävä peli. Peli sisältää kerättäviä kolikoita ja artifakteja. Pelin tavoitteena on päästä pelattavan kentän loppuun ottamatta osumaa vihollisista ja samalla keräten kolikoita ja artifakteja. Pelissä on kaksi moodia, tavallinen pelimoodi jossa kentät voi läpäistä omaan tahtiin ja nopeusmoodi jossa on aikaraja.  

## Dokumentaatio

- [Arkkitehtuurikuvaus](https://github.com/JuhoSiitonen/ot-harjoitustyo/blob/master/documentation/arkkitehtuurikuvaus.md)

- [Vaatimusmäärittely](https://github.com/JuhoSiitonen/ot-harjoitustyo/blob/master/documentation/vaatimusmaarittely.md)

- [Työaikakirjanpito](https://github.com/JuhoSiitonen/ot-harjoitustyo/blob/master/documentation/tyoaikakirjanpito.md)

- [Changelog](https://github.com/JuhoSiitonen/ot-harjoitustyo/blob/master/documentation/changelog.md)

## Käyttöohjeet

### Asennus ja suoritus

Sovelluksen vaatimat kirjastot voi asentaa komennolla:

**poetry install** 

Jonka jälkeen sovelluksen alustus komennolla:

**poetry run invoke build**

Sovelluksen voi sen jälkeen käynnistää komennolla:

**poetry run invoke start**

### Testaus

Sovelluksen yksikkötestit voi ajaa komennolla:

**poetry run invoke test**

Sovelluksen testikattavuuden saa html tiedostoksi seuraavalla komennolla:

**poetry run invoke coverage-report**

### Pylint

Sovelluksen Pylint tuloksen saa komennolla:

**poetry run invoke lint**

## Pelin pelaus

Pelin ohjaus tapahtuu nuolinäppäimillä oikealle ja vasemmalle ja välilyönnistä hahmo hyppää. Punaiset hahmot ovat vihollisia joihin osuttaessa kenttä alkaa alusta, samoin käy myös kun pelaajahahmo putoaa pois kentältä. Keltaiset neliöt ovat kolikkoja ja sininen suorakulmio on maali. Pelaajahahmo voi roikkua "katosta" hyppynappi painettuna pohjaan. 

## Tunnetut ongelmat

- Pelin collision detection on vielä hieman buginen, hahmo siirtyy joskus esteiden päälle
- Kolikoiden kerätty määrä ei vielä näytöllä
- Uusien kenttien lisäys vaatii "napin" lisäämisen käyttöliittymään, ei vielä parametrisoitu




