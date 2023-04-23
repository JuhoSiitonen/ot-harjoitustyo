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

