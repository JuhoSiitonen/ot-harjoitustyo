# Arkkitehtuurikuvaus

## Rakenne

Luokkien vastuut:

UI luokka initialisoi PySimpleGUI ikkunat joita on kaksi. Pääikkunasta voi katsoa highscore tietoja ja tämä aukaisee toisen PySimpleGUI ikkunan ja initialisoi luokan HighscoreRepository. Mikäli pääikkunassa valitaan pelattava kenttä Level painikkeilla, UI luokka initialisoi seuraavat luokat: Level, Clock, Renderer, EventHandling ja Game. Luokat Level, Clock, Renderer, EventHandling ja HighscoreRepository injektoidaan Game luokan riippuvuuksina sen konstruktoriin. 

- Clock luokka vastaa pelin pävitystaajuudesta Tick metodilla ja antaa Time attack moodin aloituksen yhteydessä tarvittavan aloitus aikaleiman metodilla time_now().

- Renderer luokka vastaa pelinäkymän renderöinnistä. 

- EventHandling vastaa tapahtumien hallinnasta pelissä, kuten näppäimistö komennot ja mikäli pelaaja sulkee ikkunan.

- HighscoreRepository luokka toteuttaa tietokantaoperaatiot joita tarvitaan kenttien parhaiden läpäisyaikojen pysyväistallennukseen.

- Level luokka initialisoi luokan SpriteHandler ja antaa sille initialisoitavaksi sprite olioita kenttädatan mukaan. Level luokka myös tekee kaiken törmäystarkastelun spritejen välillä. 

- SpriteHandler luokka initialisoi Cell, Player ja Enemy luokan olioita jotka perivät pygame.sprite.Sprites luokalta. SpriteHandler myös kerää luodut sprite oliot sprite group kokonaisuuksiksi jotta spriteja olisi helpompi käsitellä kokonaisuuksina. 

- Cell luokka luo yksinkertaisimmat sprite oliot jotka tarvitsevat vain yksinkertaisen päivitys metodin. 

- Player luokka luo pelaaja hahmon sprite olion jolla on useampi pelaajan liikkeeseen liittyvä metodi.

- Enemy luokka luo vihollis sprite olioita joilla on päivitys metodi ja suunta ja nopeus muuttujat.

- Game luokka kutsuu näiden luokkien metodeja run metodinsa silmukassa. Mikäli pelaaja pääsee kentän maaliin, tai Time attack moodissa aika loppuu kesken, tai pelaaja sulkee Pygame ikkunan, run metodin silmukka katkeaa ja palataan PySimpleGui päävalikkoon.


Sovelluksessa on myös muutamia moduuleja joissa ei ole luokkia vaan yksittäisiä metodeja. Nämä moduulit ja niiden vastuut ovat:

- build.py : Tässä moduulissa on sovelluksen tietokannan alustukseen tarvittava metodi.

- database_connection.py : Tämä moduuli luo tietokantayhteyden .env tiedostosta löytyvän nimiseen tietokantatiedostoon.

- database_initialization.py : Tässä moduulissa on metodit joilla varmistetaan että tietokantayhteyden avulla saatu tietokanta tiedosto on tyhjä ja siihen luodaan tarvittava taulu highscores. 

- settings.py : Tämä moduuli tarkistaa .env tiedoston mukaisen tietokantatiedoston olemassaolon ja jos sitä ei olemassa muodostaa sen nimisen tiedoston data kansioon. Tarkistaa myös levels.txt tiedoston olemassaolon ja isältää sprite koon ja pygame ikkunan koon määrittävät muuttujat jotka myös määritetään .env tiedostossa.

- helper_function.py : Tämä moduuli sisältää levels.txt tiedoston lukemiseen tarkoitetun funktion joka palauttaa kenttädatan listana.

- main.py : Tämä moduuli initialisoi UI luokan ja kutsuu sen run metodia joka käynnistää PySimpleGUI silmukan.

```mermaid

classDiagram
    Game <|-- UI
    Game --|> Clock
    Game --|> Event_handling
    Game --|> Level
    Game --|> Renderer
    Game --|> HighscoreRepository
    Player -- SpriteHandler
    Cells -- SpriteHandler
    Enemy -- SpriteHandler
    Level -- SpriteHandler
    HighscoreRepository -- UI
    UI -- Main

    class Player{
        +input()
        +apply_gravity()
        +move()
        +jump()
        +movement()
        +get_player_x()
        +get_direction()
    }
    class Level{
        +setup()
        +re_initialize()
        +camera()
        +horizontal_collision()
        +vertical_collision()
        +coin_collision()
        +artifact_collision
        +level_completion()
        +player_demise()
        +enemy_movement()
        +update()
    }
    class Renderer{
        +counter_text()
        +time_counter()
        +update()
        +render()
    }
    class Event_handling{
        +get()
        +get_pressed()
    }
    class Clock{
        +tick()
        +time_now()
    }
    class Cells{
        +update()
    }
    class Game{
        +handle_events()
        +handle_inputs()
        +start()
        +update()
        +render()
        +time_counter()
        +write_highscore_to_db()
    }
    class UI{
        +check_levels_file()
        +check_highscores_file()
        +create_window()
        +check_time_attack()
        +create_highscore_window()
        +run_highscore_window()
        +main_menu_window_events()
        +run()
        +run_game()
    }
    class Enemy{
        +update()
    }
    class SpriteHandler{
        +sprite_creator()
        +player_sprite_creator()
        +enemy_sprite_creator()
        +collect_sprites_to_all_sprites()
    }
    class HighscoreRepository{
        +highscores_list()
        +insert_into_highscores()
        +erase_highscores()
    }

```

## Sovelluksen toiminnallisuudet

### Käyttöliittymä

Sovelluksen käyttöliittymässä on kolme näkymää. Kaksi näkymää tuottaa PySimpleGUI kirjasto ja itse pelinäkymän tuottaa Pygame kirjasto. Ensimmäinen näkymä mikä aukeaa sovelluksen käynnistyksen yhteydessä on PySimpleGUI ikkuna jossa käyttäjä voi valita kentän mitä pelata (kenttien määrä ja siten kenttäpainikkeiden määrä määräytyy levels.txt tiedostossa olevien kenttien määrän mukaan).

Käyttäjä voi myös valita Time attack moodin sen nimisestä painikkeesta tai katsoa parhaita Time attack moodin läpäisyaikoja highscores painiketta painamalla. Highscores painike aukaisee toisen PySimpleGUI ikkunan jossa kolme parasta läpäisyaikaa on per kenttä esitettynä, tämä tieto saadaan sqlite tietokanta tiedostosta. Kolmas näkymä on pygame kirjastolla tuotettu pelinäkymä jonka leveys on vakio ja korkeus on riippuvainen kentän korkeudesta.

PySimpleGUI näkymät on toteutettu samassa UI luokassa ja pygame näkymää pyörittää Render luokka game luokan ohjastamana. 

![Main_menu](https://github.com/JuhoSiitonen/ot-harjoitustyo/blob/master/documentation/graphs/jumpman_main_menu.png)

![highscore_menu](https://github.com/JuhoSiitonen/ot-harjoitustyo/blob/master/documentation/graphs/jumpman_highscore_menu.png)

Pelin käynnistäminen sekvenssikaaviona

![Sekvenssikaavio](https://github.com/JuhoSiitonen/ot-harjoitustyo/blob/master/documentation/graphs/game_sequencediagram.png)

Yllä olevassa sekvenssikaaviossa kuvataan mitä tapahtuu sen jälkeen kun käyttäjä klikkaa jotain aloitus käyttöliittymän level painikkeista. Ui luokan metodi run_game() alustaa tarvittavat riippuvuudet game luokan olion luomiseksi. Riippuvuudet injektoidaan game luokan olioon sen konstruktorin kautta. Game luokassa start() metodi pyörittää pygame peliä ylläpitävää silmukkaa, joka tarkastaa pelinäkymän tapahtumat, käyttäjän syötteet ja level luokan metodeilla level_completion() ja player_demise, sen tulisiko pelinäkymä pysäyttää tai aloittaa valittu pelikenttä alusta. 

Level luokan toiminta sekvenssikaaviona

![Sekvenssikaavio](https://github.com/JuhoSiitonen/ot-harjoitustyo/blob/master/documentation/graphs/Levelclass%20sequence.png)

Level luokka initialisoi pygame pelinäkymän mukaiset spritet konfigurointi tiedostosta saamansa level_map listan mukaan. Level luokka sisältää metodit spritejen väliselle törmäystarkastelulle, jolla tarkastetaan pelaajan hahmon osuminen vihollisiin, kolikoihin, artifakteihin ja kaikkiin seiniin, kattoihin ja lattioihin. Level luokassa on myös metodi pelinäkymän rullaavan kameran toteutukseen, se tarkistaa mikäli pelaaja on siirtynyt pelinäkymän reunalle, mikäli pelaaja jatkaa liikettään kohti reunaa, metodi muuttaa pelaajan nopeuden nollaan ja siirtää nopeuden camera_shift muuttujaan jonka avulla kaikkia spriteja siirretään sprite luokan update metodilla sivuun. 

