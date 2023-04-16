# Arkkitehtuurikuvaus

## Rakenne

```mermaid

classDiagram

    Game <|-- Clock
    Game <|-- Event_handling
    Game <|-- Level
    Game <|-- Renderer
    Player -- Level
    Cells -- Level
    Game -- Main

    class Player{
        +input()
        +movement()
        +get_player_x()
        +get_direction()
    }
    class Level{
        +setup()
        +camera()
    }
    class Renderer{
        +render()
    }
    class Event_handling{
        +get()
    }
    class Clock{
        +tick()
    }
    class Cells{
        +update()
    }
    class Game{
        +handle_events()
        +start()
        +render()
    }
