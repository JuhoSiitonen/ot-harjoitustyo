### Monopoli


```mermaid

classDiagram

    Pelilauta "1" <|-- "40" Ruutu
    Ruutu "1" <-- "8" Pelaaja
    class Pelaaja {
        +nopanheitto()
        +osto()
        +maksu()
        +int rahat
    }
    class Ruutu{
        +String omistaja
        +int arvo
        +String Kadunnimi
    }
