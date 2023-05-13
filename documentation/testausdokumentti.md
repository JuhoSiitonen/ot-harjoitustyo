# Testausdokumentti

Sovellusta on testattu yksikkö- ja integraatiotesteillä. Luokkaa player ja highscorerepository on testattu yksinään ja level sekä game luokkia on testattu muiden luokkien kanssa. Game ja level luokissa on huomattava osa sovelluslogiikasta ja erityisesti game luokan testauksessa on käytetty vale stub luokkia simuloimaan pygame kirjaston toimintoja mitä sovellus oikeasti kutsuu kyseisistä luokista. 

Sovelluslogiikkaa toteuttavia luokkia Game ja Level testataan TestGameLoop ja TestLevel luokilla. TestGameLoop luokkaan injektoidaan riippuvuuksiksi luokka Level ja valeluokat StubClock, StubKey_press, StubEvent,StubEvent_handling ja StubRenderer.StubKey_press luokka simuloi oikean ja vasemman nuolinäppäimen sekä välilyönnin painamista. StubEvent luokka simuloi vain pygameQUIT tapahtumaa joka syötetään StubEvent_handling valeluokalle. Game luokkaa testataan kolmella testillä jotka testaavat, kentän läpäisemistä, pygame ikkunan sulkemista ja pelaajan "kuolemaa" pelissä.

Level luokkaa testataan varta vasten luodulla level_map kentällä. Level luokalla on paljon metodeja joilla testata eri sprite olioiden törmäyksiä joita kaikkia testataan. Level luokka myös pitää huolta rullaavan kameran ominaisuuksista joita myös testataan.

Player luokalla on pelaaja spriten liikkeeseen liittyviä metodeja joita kaikkia testataan TestPlayer luokalla.


# Järjestelmätestaus

Järjestelmätestaus on suurimmilta osin toteutettu manuaalisesti, vain Game luokan testeissä on useamman initialisoidun luokan (Game ja Level) luokkien yhteistoimintaa.

Manuaalisessa testauksessa on otettu huomioon data kansiossa olevien tiedostojen sisältö, kuten mikäli levels.txt on tyhjä tai highscore tietokanta on tyhjä. On myös testattu että sovellus toimii vaikka levels.txt tiedostoon syötettäisiin virheellistä kenttätietoa. 

Sovellusta on testattu manuaalisesti sekä Linux että Windows järjestelmillä käyttäen käyttöohjeiden mukaisia asennusohjeita.


# Testikattavuus

![testikattavuus](https://github.com/JuhoSiitonen/ot-harjoitustyo/blob/master/documentation/graphs/testikattavuus.png)

Testien kattavuus luokkien renderer, clock, event_handling ja moduulin helper_function suhteen on nolla prosenttia. Tämä on koska mainittuja luokkia käytettiin game luokan testaukseen ainoastaan valeluokkina. Nämä luokat periaatteessa edustavat käyttöliittymää, mutta jätin ne testikattavuuteen.


# Tunnetut ongelmat
 
- SpriteHandler luokalla liikaa instanssimuuttujia.
- Käyttöliittymäluokka Ui voisi olla paremmin eriytetty sovelluslogiikasta.
- Tietokanta tiedosto alustetaan ennen pelin ensimmäistä käynnistystä komentorivikomennolla.
- Mikäli käyttäjä tekee uuden kentän olemassaolevien kenttien väliin levels.txt tiedostossa, viittaavat highscore tietokannan tiedot vääriin kenttiin sen jälkeen. Kunnes käyttäjä klikkaa painiketta "Erase scores" highscore ikkunassa. 
- Joissain tilanteissa pygame törmäyksentunnistus ja sovelluksen törmäyksentunnistuslogiikka siirtää pelaajan törmäyksen yhteydessä vahingossa törmätyn spriten yläpuolelle. Harvinainen vika jonka syntyy vaikuttavista olosuhteista ei ole tarpeeksi tietoa sen korjaamiseksi. 
- Testien kattavuus luokkien renderer, clock, event_handling ja moduulin helper_function suhteen on nolla prosenttia. Tämä on koska mainittuja luokkia käytettiin game luokan testaukseen ainoastaan valeluokkina. Nämä luokat periaatteessa edustavat käyttöliittymää, mutta jätin ne testikattavuuteen. 