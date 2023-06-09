## Viikko 3

- Luotu main.py päämoduuliksi
- Luotu cells.py ja level.py luomaan pelinäkymä main.py sisältämästä level_map listasta
- Luotu player luokka ja sen mukaiset muutokset main, level ja cells luokkiin jotta pelaaja hahmo piirtyy ruudulle vihreänä
- Separation of concerns, alkuvedoksen jakoa moduuleihin jotta riippuvuudet voidaan injektoida ja level_test sekä player_test moduulien luonti
- Kolmannen viikon lopuksi saatu valmiiksi ensimmäinen testi joka testaa player luokan movement functiota

## Viikko 4

- Lisätty invoke komento autopep formatoinnille.
- Luotu moduulit: clock.py, event_handling, game.py ja renderer.py
- Riippuvuuksien injektointi game.py moduuliin. 
- Hahmon liike player.py moduulissa itsessään toteutettuna jotta liike on sulavaa pygame.key.get_pressed() funktion avulla. Liikkuminen oikealle ja vasemmalle sekä hyppääminen onnistuu. Myös painovoima arvo lisätty jotta hyppääminen onnistuisi. 
- Rullaava kamera toteutettu level.py moduulissa. 
- Inputtien tarkastus game.py moduulissa handle_inputs metodissa. 
- Törmäyksien tarkistus level.py moduulissa, ei vielä täysin varma siitä mihin pelaaja tulisi sijottaa törmäyksen jälkeen.
- Hahmon liikkeen törmäyksien tarkistuksen järjestys muutettu, ensin vertikaali liikkeen tarkistus ja sitten horisontaali liikkeen tarkistus törmäyksien varalta ja sen mukainen hahmon siirtäminen törmättävän spriten asianmukaiselle puolelle. 
- Kentän maalin lisäys moduulin level koodiin ja moduulin cell muokkaus jotta luokka ottaa parametrina vastaan spriten värin

## Viikko 5

- Lisätty uusi moduuli UI.py jossa on luokka UI.
- Lisätty aloitusruutu jossa voi valita pelattavan kentän tai poistua pelistä. Tämä ruutu on toteutettu PySimpleGUI kirjastolla.
- PySimpleGUI luo uuden säikeen pygame ikkunalle kun se käynnistetään valitsemalla pelattava kenttä
- Kentän maalin funktionaalisuus lisätty, maaliin pääseminen sulkee pygame ikkunan ja sen säikeen.
- Pelaajan hyppy korjattu toimimaan ainoastaan kun pelaaja koskee "maahan"
- Lisätty vihollisia (moduuli enemy.py) peliin jotka liikkuvat oikealle ja vasemmalle kunnes osuvat näkymättömään rajoittavaan soluun jolloin niiden liikensuunta muuttuu päinvastaiseksi
- Lisätty tarkistus sille mikäli pelaaja putoaa peliruudulta tai osuu viholliseen. Niiden seurauksena kenttä alkaa alusta.
- Moduulien asettaminen uusiin asianmukaisiin kansioihin, testikattavuuden nosto.
- Lisätty kolikko spritet peliin jotka tuhoutuvat törmätessään pelaajaan.

## Viikko 6

- Lisätty artifakti spritet jotka tuhoutuvat osuessaan pelaajan.
- Kolikoiden ja artifaktien laskuri oikeassa ylänurkassa pygame ikkunaa pelatessa, laskuri nollaantuu kun pelaaja osuu viholliseen tai tippuu kentältä pois.
- Korjattu pelaajan yhteentörmäys logiikka joka tarkastaa ettei pelaaja voi mennä seinistä tai lattioista läpi. Ensin tehdään vertikaali suunnassa törmäystarkistus, sitten horisontaali suunnassa ja pelaaja siirtyy seinän, lattian tai katon suhteen oikealle paikalle, eikä mene läpi tai siirry virheellisesti esteen yläpuolelle liikkuessaan. 
- Lisätty nappi Time Attack pysimplegui käyttöliittymään, jonka avulla voi valita eri pelimoodin jossa läpäisyaika on rajallinen.
- Time attack moodi valittuna lisätty vasempaan yläkulmaan ajastin joka näkyy pelatessa.
- Docstring dokumentaatio lisätty. 

## Viikko 7

- Lisätty data kansio projektiin jonka sisältönä on levels.txt, tekstitiedosto josta luetaan pelin kentät. 
- Päivitetty ui.py moduulin koodi jotta se lukee kentät tästä tiedostosta uuden helper_functions moduulin avulla joka sisältää tiedostojen lukemiseen ja kirjoittamiseen vaaditut funktiot. 
- Koodin refaktorointia, Render luokasta siirretty ajastimen logiikka Level moduuliin, Level moduulin setup funktiota kevennetty. 
- Highscore ikkunan esittäminen käyttöliittymässä pysimplegui ikkunana ja tämän vaatimat muutokset UI luokkaan, sekä oma apu funktio highscore tiedoston lukemiseksi ja kirjoittamiseksi.
- Highscore tiedon tallentaminen tiedoston sijasta sqlite tietokantaan, sen vaatimat muutokset ui ja game luokkiin sekä kansion repositories luominen. Myös moduulit database_connection.py, database_initialization.py ja build.py luotu tietokanta operaatioiden hallintaan. 
- Highscore PySImpleGUI ikkunaan lisätty erase scores painike jolla voi tyhjentää tietokannan sisällön. 
- Level luokan vastuiden pienentäminen siirtämällä spritejen luomisen uuteen SpriteHandler luokkaan.
- Level luokan pienentäminen siirtämällä time attack moodin logiikka game, clock ja render luokkiin. 
- .env ympäristömuuttujien käyttö sprite koon, näytön koon ja tiedostojen nimien parametrisoinnissa.
- .env ympäristömuuttujan käyttö time attack moodin aikarajan määrityksessä. 
- Apufunktion level_file_reader() logiikkaan lisätty try except rakenne jotta sovellus toimii siinäkin tilanteessa kun levels.txt tiedostoa ei löydy. 
- Level luokan level_completion() metodiin lisätty try except rakenne jotta sovellus toimii vaikka käyttäjä tekisi uuden kentän joka on täysin tyhjä. 

