# Käyttöohje

Sovelluksen käynnistyessä aukeaa PySimpleGUI ikkuna jossa voi valita pelattavan kentän ja mikäli haluaa pelata Time Attack moodissa jossa on 15 sekuntia aikaa läpäistä kenttä. Tässä päävalikko ikkunassa voi myös valita Highscores painikkeen joka aukaisee uuden 
ikkunan jossa on esitettynä kaikkien kenttien kolme parasta läpäisyaikaa (mikäli niitä on).

Pelin ohjaus tapahtuu nuolinäppäimillä oikealle ja vasemmalle ja välilyönnistä hahmo hyppää. Punaiset hahmot ovat vihollisia joihin osuttaessa kenttä alkaa alusta, samoin käy myös kun pelaajahahmo putoaa pois kentältä. Keltaiset neliöt ovat kolikkoja, punaiset neliöt artifakteja ja sininen suorakulmio on maali. Pelaajahahmo voi roikkua "katosta" hyppynappi painettuna pohjaan. 

Pelin voi sulkea Pygame ikkunan oikean yläkulman x painikkeesta. PySimpleGUI ikkuna jää vielä auki ja sen voi sulkea joko Exit painikkeesta tai ikkunan oikean ylänurkan x painikkeesta. 

Peliä voi konfiguroida levels.txt tiedoston kautta josta voi manipuloida pelin kenttiä. Oman kentän voi kasata tekstitiedostoon jossa x kirjaimella merkitään seinä/lattia/katto spriteja, P on pelaajan aloituspositio (useampi P kenttätiedostossa aiheuttaa virheen), C on kolikko spriten merkki, A on artifakti spriten merkki, E on vihollisspriten merkki. Viholliset liikkuvat oikealle ja vasemmalle B spritejen välissä, osuma B spriteen saa vihollisen vaihtamaan suuntaa, B spritet ovat pelissä näkymättömiä pelaajalle. G kirjaimella merkitty sprite on maali. Väliviiva tulee olla tekstitiedostossa ennen ensimmäistä riviä ja kentän viimeisen rivin jälkeen, jotta ohjelma tunnistaa sen kentäksi. 

## Konfiguraatiot

Pelin kenttien parhaiden läpäisyaikojen tallentamiseen käytetään tietokanta tiedostoa, jonka nimeä voi halutessaan
muuttaa sovelluksen päähakemiston .env tiedoston kautta. Tämä tietokanta tiedosto luodaan sovelluksen data-hakemistoon
sovelluksen alustamisen yhteydessä (komentorivi komento "poetry run invoke build").

**DATABASE_FILENAME=database.sqlite**

Sovelluksen data-hakemistossa on levels.txt tiedosto joka sisältää pelin pelattavat kentät. Voit luoda oman kentän
kyseiseen tekstitiedostoon merkin "-" jälkeen ja kentän tietojen loppuun tulee myös laittaa väliviiva merkitsemään 
kenttätietojen loppua. Ilman tätä tiedostoa pelaaminen ei onnistu, mutta sen modifikaatiot ovat mahdollisia. Tiedoston nimeä voi myös muuttaa halutessaan päähakemiston .env tiedoston kautta.

**LEVELS_FILENAME=levels.txt**

Kenttädatan merkkien selitykset:

**x = Harmaa seinä/lattia/katto sprite, useita per kenttä.**
**P = Vihreä pelaaja sprite, vain yksi per kenttä.**
**C = Keltainen kolikko sprite, voi olla useita per kenttä.**
**A = Punainen artifakti sprite, voi olla useita per kenttä.**
**E = Punainen vihollis sprite, voi olla useita per kenttä.**
**B = Näkymätön sprite johon osuessaan vihollinen muuttaa suuntaa.**
**G = Pelin maali sprite, vain yksi per kenttä.**