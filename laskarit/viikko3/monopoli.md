### Monopoli


```mermaid

classDiagram

    Peli "1" -- "1" Pelilauta
    Peli "1" -- "8" Pelaaja
    Peli <.. Aloitus
    Peli <.. Vankila
    Pelilauta "1" <|-- "40" Ruutu
    Vankila "1" <.. "8" Pelaaja
    Mene_vankilaan "1" <.. "8" Pelaaja
    Aloitus "1" <.. "8" Pelaaja
    Yhteismaa "1" <.. "8" Pelaaja
    Sattuma "1" <.. "8" Pelaaja
    Asemat_ja_laitokset "1" <.. "8" Pelaaja
    Vapaa_pysäköinti "1" <.. "8" Pelaaja
    Lisä_vero "1" <.. "8" Pelaaja
    Normaalit_kadut "1" <.. "8" Pelaaja
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
    class Kortit {
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
    class Lisä_vero {
        +int verojen_maara
    }
    class Peli {
        +säännöt()
    }
    class Pelilauta {
        +linkedlist ruudut
    }