# Arkkitehtuurikuvaus

## Rakenne

```mermaid

classDiagram
    Game <|-- UI
    Game --|> Clock
    Game --|> Event_handling
    Game --|> Level
    Game --|> Renderer
    Player -- Level
    Cells -- Level
    Enemy -- Level
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
        +camera()
        +horizontal_collision()
        +vertical_collision()
        +coin_collision()
        +level_completion()
        +player_demise()
        +update()
    }
    class Renderer{
        +render()
    }
    class Event_handling{
        +get()
        +get_pressed()
    }
    class Clock{
        +tick()
    }
    class Cells{
        +update()
    }
    class Game{
        +handle_events()
        +handle_inputs()
        +start()
        +render()
    }
    class UI{
        +create_window()
        +run()
        +run_game()
    }
    class Enemy{
        +update()
    }

```

## Sovelluksen toiminnallisuudet

Kun sovellus käynnistyy se avaa PySimpleGUI ikkunan joka toimii käyttöliittymänä sovellukselle. Tästä ikkunasta voi siirtyä itse peliin valitsemalla jonkin level painikkeista. Sovellus luo uuden säikeen ja käynnistää pygame kirjaston avulla renderöidyn pelinäkymän. Mikäli klikkaat Time Attack painiketta, peli käynnistyy rajoitetulla ajalla joka näkyy ajastimena vasemmassa nurkassa pelinäkymää. 

![Aloitusruutu](https://github.com/JuhoSiitonen/ot-harjoitustyo/blob/master/documentation/graphs/jumpman_pysimplegui.png)

Pelin käynnistäminen sekvenssikaaviona

![Sekvenssikaavio](https://github.com/JuhoSiitonen/ot-harjoitustyo/blob/master/documentation/graphs/game_sequencediagram.png)

Yllä olevassa sekvenssikaaviossa kuvataan mitä tapahtuu sen jälkeen kun käyttäjä klikkaa jotain aloitus käyttöliittymän level painikkeista. Ui luokan metodi run_game() alustaa tarvittavat riippuvuudet game luokan olion luomiseksi. Riippuvuudet injektoidaan game luokan olioon sen konstruktorin kautta. Game luokassa start() metodi pyörittää pygame peliä ylläpitävää silmukkaa, joka tarkastaa pelinäkymän tapahtumat, käyttäjän syötteet ja level luokan metodeilla level_completion() ja player_demise, sen tulisiko pelinäkymä pysäyttää tai aloittaa valittu pelikenttä alusta. 

Level luokan toiminta sekvenssikaaviona

![Sekvenssikaavio](https://github.com/JuhoSiitonen/ot-harjoitustyo/blob/master/documentation/graphs/Levelclass%20sequence.png)

Level luokka initialisoi pygame pelinäkymän mukaiset spritet konfigurointi tiedostosta saamansa level_map listan mukaan. Level luokka sisältää metodit spritejen väliselle törmäystarkastelulle, jolla tarkastetaan pelaajan hahmon osuminen vihollisiin, kolikoihin, artifakteihin ja kaikkiin seiniin, kattoihin ja lattioihin. Level luokassa on myös metodi pelinäkymän rullaavan kameran toteutukseen, se tarkistaa mikäli pelaaja on siirtynyt pelinäkymän reunalle, mikäli pelaaja jatkaa liikettään kohti reunaa, metodi muuttaa pelaajan nopeuden nollaan ja siirtää nopeuden camera_shift muuttujaan jonka avulla kaikkia spriteja siirretään sprite luokan update metodilla sivuun. 
