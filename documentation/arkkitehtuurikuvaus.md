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

Level luokan toiminta sekvenssikaaviona

![Sekvenssikaavio](https://github.com/JuhoSiitonen/ot-harjoitustyo/blob/master/documentation/graphs/Levelclass%20sequence.png)
