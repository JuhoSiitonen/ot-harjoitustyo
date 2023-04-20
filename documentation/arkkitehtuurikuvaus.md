# Arkkitehtuurikuvaus

## Rakenne

```mermaid

classDiagram
    UI <|-- Game
    Game <|-- Clock
    Game <|-- Event_handling
    Game <|-- Level
    Game <|-- Renderer
    Player -- Level
    Cells -- Level
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
        +level_completion()
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
