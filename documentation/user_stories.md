# Käyttötapauksia

## Toteutettu

* Foorumin käyttäjä voi luoda itselleen käyttäjätunnuksen ja kirjautua sisään
* Kuka tahansa voi lukea käyttäjien luomia viestiketjuja kirjautumatta sisään
* Sisäänkirjautunut käyttäjä voi luoda uuden viestiketjun
* Sisäänkirjautunut käyttäjä voi lisätä viestin mihin tahansa viestiketjuun
* Sisäänkirjautunut käyttäjä voi muokata viestiketjuihin lähetettyjä viestejä
* Sisäänkirjautunut käyttäjä voi poistaa kokonaisen viestiketjun ja sen mukana kaikki siihen lähetetyt viestit

## Työn alla

* Viestien muokkaaminen ja viestiketjujen poistaminen onnistuu vain, jos kyseessä on käyttäjän itsensä lisäämä viesti tai viestiketju. Tällä hetkellä kaikilla kirjautuneilla käyttäjillä on oikeus muokata ja poistaa.
* Käyttäjän rekisteröityessä sivustolle, salasana talletetaan tietokantaan salattuna hajautusarvona. Tällä hetkellä salasanat tallennetaan vielä selväkielisinä.
* Viestiketjua luodessa siihen voi liittää valmiiksi määriteltyjä tunnisteita, joiden avullla näytettävien viestiketjujen listaa voi rajata