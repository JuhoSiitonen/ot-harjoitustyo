### Monopoli


```mermaid

classDiagram

    Pelilauta "1" <|-- "40" Ruutu
    Ruutu "1" <-- "8" Pelaaja
    Ruutu "1" <|-- "1" Vankila
    Ruutu "1" <|-- "1" Mene_vankilaan
    Vankila "1" -- "1" Mene_vankilaan
    Ruutu "1" <|-- "1" Aloitus
    Ruutu "1" <|-- "3" Yhteismaa
    Ruutu "1" <|-- "3" Sattuma
    Ruutu "1" <|-- "5" Asemat_ja_laitokset
    Ruutu "1" <|-- "1" Vapaa_pysäköinti
    Ruutu "1" <|-- "2" Lisä_vero
    Ruutu "1" <|-- "22" Normaalit_kadut
    Kortit "1" --> "1" Sattuma
    Kortit "1" --> "1" Yhteismaa

    class Pelaaja {
        +nopanheitto()
        +osto()
        +maksu()
        +int rahat
        +list kiinnitykset
    }
    class Ruutu{
        +String nimi
    }
    class Kortti {
        +funktio()
    }
    class Vapaa_pysäköinti {
        +saldo
    }
    class Vankila {
        +vuorolaskuri()
        +int vakuus
    }
    class Normaalit_kadut {
        +arvo()
        +String omistaja
        +int talojen_maara
        +int vuokra
        +bool kiinnitetty
    }
