# Microblog
Microblog je spletni blog podoben Twitterju le da ni omejitve na 140 znakov. Objave so lahko poljubno dolge, vsebujejo lahko lokacijo, slike in zunanje povezave na druge strani.
Aplikacija omogoča sledenje drugim uporabnikom, tako da lahko spremljamo njihove objave ter omogoča tudi posebno obravnavanje ključnih besed, ki se začnejo z @ in #, podobno, kot to počne Twitter.
Spletna stran Microblog je podprta za delovanje tako na večjih zaslonih (osebni računalnik), kot na manjših (tablicah in mobilnih telefonih).

## Ciljna publika
Aplikacija je namenjena vsem ljudem, ki želijo deliti objave z drugimi ali le slediti objavam ostalih uporabnikov.

## Aplikacija je dostopna na spletni povezavi: [sp-microblog.herokuapp.com](https://sp-microblog.herokuapp.com)

## Delovanje in izgled strani v treh brskalnikih
Aplikacijo sem stestiral v treh brskalnikih in sicer Google Chrome, Mozilla Firefox in Opera.
Pri testiranju na Chromu in Operi sem imel težave, ko sem želel tesirati dostop do lokalne datoteke (.json) s funkcijo XMLHttpRequest, saj omenjena brkalnika tega ne dovoljujeta. Omenjeno funkcionalnost sem moral stestirati na Firefoxu, ki to omogoča.
Manjše razlike so se pojavile tudi pri dimenzijah nekaterih html elementov, zato sem moral dodatno popraviti css, da je izgled na vseh treh brskalnikih konsistenten.

## Najbolša dela aplikacije
Najbolj sem ponosen na prilagodljivost spletne strani, še posebej na dropdown gradnik, ki pri manjših ekranih skrije podatke o profilu in gumbe, tako da je stran bolj pregledna. Zadovoljen sem tudi z dizajnom in prikazom objav v aplikaciji.

## Nadaljno delo
Aplikacijo bi lahko še dodatno vizualno in funkcionalno izbolšal z uporabo dodatnih JavaScript knjižnic kot so jQuery, Bootstrap. 
