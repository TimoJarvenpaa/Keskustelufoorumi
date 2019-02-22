# Keskustelufoorumi

[Linkki sovellukseen](https://blooming-reef-61522.herokuapp.com/)

Sovelluksen käyttäminen vaatii käyttäjätunnuksen, jonka voi halutessaan luoda sivulta löytyvän rekisteröitymislomakkeen kautta.

Vaihtoehtoisesti voi myös käyttää alla olevaa valmiiksi luotua käyttäjätunnusta:
```
username: test
password: user
```

[Linkki sovelluksen asennusohjeeseen](documentation/installation_instructions.md)

[Linkki sovelluksen tietokantakaaviohahmotelmaan](documentation/forum_diagram.png)

[Linkki sovelluksen käyttötapausesimerkkeihin](documentation/user_stories.md)

Harjoitustyöni tavoitteena on tehdä keskustelufoorumi videopeliharrastajien käyttöön. Foorumin käyttäjä voi mm. luoda itselleen käyttäjätunnuksen, lukea muiden käyttäjien kirjoituksia, luoda uusia viestiketjuja tai lisätä viestejä olemassa oleviin ketjuihin. Viestiketjujen luonnin yhteydessä niihin liitetään kategorioita, joiden perusteella näytettävien viestiketjujen listaa voi rajata.

Järjestelmän ylläpitäjällä on oikeus muokata ja poistaa käyttäjien luomia viestejä tai viestiketjuja. Lisäksi ylläpitäjä voi lisätä uusia kategorioita sekä muokata tai poistaa olemassa olevia kategorioita.

Toimintoja:

* Käyttäjätunnuksen luominen ja sisäänkirjautuminen
* Viestiketjujen luominen ja viestien kirjoittaminen
* Viestien ja viestiketjujen muokkaaminen ja poistaminen
* Kategorioiden lisääminen, muokkaaminen ja poistaminen
* Näytettävien viestiketjujen rajaaminen kategorioiden perusteella
