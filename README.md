# Ohjelmistotekniikka

Repository for course **Ohjelmistotekniikka** weekly coding excercises and a **desktop application** made with *agile methods*.

# Harjoitustyö (Jumpman)

Jumpman on tasohyppely peli joka on sivulle rullaavalla ruudulla toteutettu Pythonin pygame ja PySimpleGUI kirjastoja käyttävä peli. Peli sisältää kerättäviä kolikoita ja artifakteja. Pelin tavoitteena on päästä pelattavan kentän loppuun ottamatta osumaa vihollisista ja samalla keräten kolikoita ja artifakteja. Pelissä on kaksi moodia, tavallinen pelimoodi jossa kentät voi läpäistä omaan tahtiin ja nopeusmoodi jossa on aikaraja.  

## Dokumentaatio

- [Käyttöohjeet](https://github.com/JuhoSiitonen/ot-harjoitustyo/blob/master/documentation/k%C3%A4ytt%C3%B6ohjeet.md)

- [Arkkitehtuurikuvaus](https://github.com/JuhoSiitonen/ot-harjoitustyo/blob/master/documentation/arkkitehtuurikuvaus.md)

- [Testausdokumentti](https://github.com/JuhoSiitonen/ot-harjoitustyo/blob/master/documentation/testausdokumentti.md)

- [Vaatimusmäärittely](https://github.com/JuhoSiitonen/ot-harjoitustyo/blob/master/documentation/vaatimusmaarittely.md)

- [Työaikakirjanpito](https://github.com/JuhoSiitonen/ot-harjoitustyo/blob/master/documentation/tyoaikakirjanpito.md)

- [Changelog](https://github.com/JuhoSiitonen/ot-harjoitustyo/blob/master/documentation/changelog.md)

- [Loppupalautus release](https://github.com/JuhoSiitonen/ot-harjoitustyo/releases/tag/Loppupalautus)

## Käyttöohjeet

### Asennus ja suoritus

Sovelluksen vaatimat kirjastot voi asentaa komennolla:

**poetry install** 

Sovellus tulee seuraavaksi alustaa komennolla:

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






