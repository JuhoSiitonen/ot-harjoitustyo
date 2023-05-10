# Käyttöohje

Sovelluksen käynnistyessä aukeaa PySimpleGUI ikkuna jossa voi valita pelattavan kentän ja mikäli haluaa pelata Time Attack moodissa jossa on 15 sekuntia aikaa läpäistä kenttä. 

Pelin ohjaus tapahtuu nuolinäppäimillä oikealle ja vasemmalle ja välilyönnistä hahmo hyppää. Punaiset hahmot ovat vihollisia joihin osuttaessa kenttä alkaa alusta, samoin käy myös kun pelaajahahmo putoaa pois kentältä. Keltaiset neliöt ovat kolikkoja, punaiset neliöt artifakteja ja sininen suorakulmio on maali. Pelaajahahmo voi roikkua "katosta" hyppynappi painettuna pohjaan. 

Pelin voi sulkea Pygame ikkunan oikean yläkulman x painikkeesta. PySimpleGUI ikkuna jää vielä auki ja sen voi sulkea joko Exit painikkeesta tai ikkunan oikean ylänurkan x painikkeesta. 

Pelin konfiguraatiotiedosto on vielä toistaiseksi settings.py moduulissa, sen kautta voi manipuloida pelin kenttiä, spritejen kokoa ja Pygame ikkunan kokoa. Oman kentän voi kasata luomalla nested list tyyppisen tietorakenteen jossa x kirjaimella merkitään seinä/lattia/katto spriteja, P on pelaajan aloituspositio (useampi P kenttätiedostossa aiheuttaa virheen), C on kolikko spriten merkki, A on artifakti spriten merkki, E on vihollisspriten merkki. Viholliset liikkuvat oikealle ja vasemmalle B spritejen välissä, osuma B spriteen saa vihollisen vaihtamaan suuntaa, B spritet ovat pelissä näkymättömiä pelaajalle. G kirjaimella merkitty sprite on maali. 