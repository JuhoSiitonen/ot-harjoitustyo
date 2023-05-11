# Käyttöohje

Sovelluksen käynnistyessä aukeaa PySimpleGUI ikkuna jossa voi valita pelattavan kentän ja mikäli haluaa pelata Time Attack moodissa jossa on 15 sekuntia aikaa läpäistä kenttä. Tässä päävalikko ikkunassa voi myös valita Highscores painikkeen joka aukaisee uuden 
ikkunan jossa on esitettynä kaikkien kenttien kolme parasta läpäisyaikaa (mikäli niitä on).

Pelin ohjaus tapahtuu nuolinäppäimillä oikealle ja vasemmalle ja välilyönnistä hahmo hyppää. Punaiset hahmot ovat vihollisia joihin osuttaessa kenttä alkaa alusta, samoin käy myös kun pelaajahahmo putoaa pois kentältä. Keltaiset neliöt ovat kolikkoja, punaiset neliöt artifakteja ja sininen suorakulmio on maali. Pelaajahahmo voi roikkua "katosta" hyppynappi painettuna pohjaan. 

Pelin voi sulkea Pygame ikkunan oikean yläkulman x painikkeesta. PySimpleGUI ikkuna jää vielä auki ja sen voi sulkea joko Exit painikkeesta tai ikkunan oikean ylänurkan x painikkeesta. 

Peliä voi konfiguroida levels.txt tiedoston kautta josta voi manipuloida pelin kenttiä. Oman kentän voi kasata tekstitiedostoon jossa x kirjaimella merkitään seinä/lattia/katto spriteja, P on pelaajan aloituspositio (useampi P kenttätiedostossa aiheuttaa virheen), C on kolikko spriten merkki, A on artifakti spriten merkki, E on vihollisspriten merkki. Viholliset liikkuvat oikealle ja vasemmalle B spritejen välissä, osuma B spriteen saa vihollisen vaihtamaan suuntaa, B spritet ovat pelissä näkymättömiä pelaajalle. G kirjaimella merkitty sprite on maali. Väliviiva tulee olla tekstitiedostossa ennen ensimmäistä riviä ja kentän viimeisen rivin jälkeen, jotta ohjelma tunnistaa sen kentäksi. 