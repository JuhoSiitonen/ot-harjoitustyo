# Testausdokumentti

Sovellusta on testattu yksikkö- ja integraatiotesteillä. Luokkaa player on testattu yksikkötestein ja level sekä game luokkia on testattu muiden luokkien kanssa. Game ja level luokissa on huomattava osa sovelluslogiikasta ja erityisesti game luokan testauksessa on käytetty stub luokkia simuloimaan pygame kirjaston toimintoja mitä sovellus oikeasti kutsuu kyseisistä luokista. 

Sovelluslogiikkaa toteuttavia luokkia Game ja Level testataan TestGameLoop ja TestLevel luokilla. TestGameLoop luokkaan injektoidaan riippuvuuksiksi luokka Level ja valeluokat StubClock, StubKey_press, StubEvent,StubEvent_handling ja StubRenderer.StubKey_press luokka simuloi oikean ja vasemman nuolinäppäimen sekä välilyönnin painamista. StubEvent luokka simuloi vain pygameQUIT tapahtumaa joka syötetään StubEvent_handling valeluokalle. Game luokkaa testataan kolmella testillä jotka testaavat, kentän läpäisemistä, pygame ikkunan sulkemista ja pelaajan "kuolemaa" pelissä.

Level luokkaa testataan varta vasten luodulla level_map kentällä. Level luokalla on paljon metodeja joilla testata eri sprite olioiden törmäyksiä joita kaikkia testataan. Level luokka myös pitää huolta rullaavan kameran ominaisuuksista joita myös testataan.

Player luokalla on pelaaja spriten liikkeeseen liittyviä metodeja joita kaikkia testataan TestPlayer luokalla.


# Järjestelmätestaus

Järjestelmätestaus on suurimmilta osin toteutettu manuaalisesti, vain Game luokan testeissä on useamman initialisoidun luokan (Game ja Level) luokkien yhteistoimintaa.

Manuaalisessa testauksessa on otettu huomioon data kansiossa olevien tekstitiedostojen sisältö, kuten mikäli levels.txt on tyhjä tai highscores on tyhjä.

Sovellusta on testattu manuaalisesti sekä Linux että Windows järjestelmillä käyttäen käyttöohjeiden mukaisia asennusohjeita.


# Tunnetut ongelmat
 
- SpriteHandler luokalla liikaa instanssimuuttujia.
- Käyttöliittymäluokka Ui voisi olla paremmin eriytetty sovelluslogiikasta.
- Tietokanta tiedosto alustetaan ennen pelin ensimmäistä käynnistystä, mutta jos tiedosto poistetaan data kansiosta tai se siirretään sovellus ei siitä itse tokene. 
- Sovellus lukee pelin kenttien tiedot tekstitiedostosta johon käyttäjä voi itse lisätä kenttiä. Jos käyttäjä ei noudata kentän teko-ohjeita sovellus ajautuu virhetilanteeseen. 
- Mikäli käyttäjä tekee uuden kentän olemassaolevien kenttien väliin levels.txt tiedostossa, viittaavat highscore tietokannan tiedot vääriin kenttiin sen jälkeen. Kunnes käyttäjä klikkaa painiketta "Erase scores" highscore ikkunassa. 
- Joissain tilanteissa pygame törmäyksentunnistus ja sovelluksen törmäyksentunnistuslogiikka siirtää pelaajan törmäyksen yhteydessä vahingossa törmätyn spriten yläpuolelle. Harvinainen vika jonka syntyy vaikuttavista olosuhteista ei ole tarpeeksi tietoa sen korjaamiseksi. 
- Testien kattavuus on hieman liian alhainen.