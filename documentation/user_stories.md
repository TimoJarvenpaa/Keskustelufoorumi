# Käyttötapauksia

## Käyttäjät ja kirjautuminen

* Kuka tahansa voi rekisteröidä käyttäjätunnuksen ja kirjautua sisään
* Rekisteröitymisen yhteydessä voi valita käyttäjätilin roolin \(User/Admin\). Todellisuudessa tämä on huono ratkaisu, mutta se helpottaa sovelluksen ominaisuuksien testaamista.
* Kun käyttäjätunnus luodaan, salasana tallennetaan tietokantaan bcryptin avulla salattuna
* Sisäänkirjautunut käyttäjä voi kirjautua ulos
* Etusivulla listataan rekisteröityjen käyttäjien nimet ja heidän kirjoittamiensa viestien lukumäärät seuraavan yhteenvetokyselyn mukaisesti: `SELECT Account.name AS name, COUNT(Message.id) AS count FROM Account LEFT JOIN Message ON Message.account_id = Account.id  GROUP BY name ORDER BY count DESC`
* Hieman samaan tapaan viestikejuissa, jokaisen viestin yhteydessä näytetään viestin kirjoittaneen käyttäjän nimi ja käyttäjän kirjoittamien viestien lukumäärä, joka saadaan seuraavalla yhteenvetokyselyllä: `(SELECT Account.name AS name, COUNT(Message.id) AS count FROM Account INNER JOIN Message ON Message.account_id = :id GROUP BY name).params(id=u_id)`, missä u_id on käyttäjään liittyvä pääavain

## Viestiketjut

* Kuka tahansa voi katsella viestikejuja kirjautumatta sisään
* Kirjautunut käyttäjä voi lisätä uusia viestiketjuja
* Viestiketjun luonnin yhteydessä sille on valittava vähintään yksi kategoria
* Tavallinen käyttäjä voi muokata itse luomiensa viestiketjujen otsikkoja ja viestikejuihin liittyviä kategorioita
* Tavallinen käyttäjä voi poistaa itse luomiaan viestiketjuja. Viestiketjun poistaminen johtaa myös kaikkien siinä olleiden viestien poistamiseen.
* Ylläpitäjä voi muokata ja poistaa kenen tahansa luomia viestikejuja
* Viestikejut järjestetään sen perusteella, milloin niitä on viimeksi muokattu tai niihin on lisätty uusia viestejä
* Oletusarvoisesti kaikki viestikejut listataan, mutta näytettäviä viestiketjuja voi myös suodattaa niiden kategorioiden perusteella. Tiettyyn kategoriaan kuuluvien viestiketjujen pääavaimet saadaan selville seuraavalla yhteenvetokyselyllä: `(SELECT Thread.id as id FROM Thread INNER JOIN thread_category tc ON Thread.id = tc.thread_id WHERE tc.category_id = :id).params(id=c_id)`, missä c_id on valittuun kategoriaan liittyvä pääavain

## Viestit

* Kirjautunut käyttäjä voi lisätä viestejä mihin tahansa viestiketjuun
* Tavallinen käyttäjä voi muokata tai poistaa itse kirjoittamiaan viestejä
* Ylläpitäjä voi muokata tai poistaa kenen tahansa kirjoittamia viestejä
* Viestin muokkaamisen seurauksena sen yhteyteen liitetään tieto muokkaamisajankohdasta

## Kategoriat

* Vain ylläpitäjät pääsevät kategorioiden hallintasivulle
* Hallintasivulla listataan kaikki luodut kategoriat ja lukumäärä viestiketjuista, jotka kuuluvat kyseiseen kategoriaan. Kategorioiden nimet ja niihin liittyvien viestikejujen lukumäärät saadaan selville seuraavalla yhteenvetokyselyllä: `SELECT Category.id as id, Category.name AS name, COUNT(thread_category.thread_id) AS count FROM Category LEFT JOIN thread_category ON Category.id = thread_category.category_id GROUP BY id ORDER BY count DESC`
* Ylläpitäjä voi lisätä uusia kategorioita, muokata olemassaolevien kategorioiden nimiä tai poistaa kategorioita

## Puuttuvia ominaisuuksia ja muita huomautuksia

* Alkuperäisessä suunnitelmassa mainitut peleihin liittyvät toiminnot kuten pelien lisääminen käyttäjien omiin pelikirjastoihin ja peleille annettavat arvosanat jäävät näillä näkymin puuttumaan lopullisesta sovelluksesta
* Viestiketjuja muokattaessa niiden muokkauslomake ei valitettavasti näytä, että mihin kategorioihin ko. viestiketju aiemmin kuului
* Käyttäjien tietojen muokkaus, kuten salasanan vaihtaminen tai käyttäjien poistaminen ei ole tällä hetkellä mahdollista.
* Yhdellä sivulla näytettävien viestiketjujen tai viestien määrää ei ole rajoitettu. Flask-paginate -kirjaston avulla asian voisi korjata, jos aika riittää.
* Viestiketjun viestit listataan nyt vain peräkkäin eikä sovelluksessa ole mahdollisuutta kirjoittaa vastausta yksittäisiin viesteihin