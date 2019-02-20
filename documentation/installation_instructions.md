# Asennusohjeet

Seuraavat työvälineet tulee olla asennettuna:
* python (versio 3.5 tai uudempi)
* pip
* pythonin venv-kirjasto (virtuaaliympäristöjen luomiseen)

## Sovelluksen käyttöönotto paikallisesti

* Lataa sovellus projektin GitHub-repositorion etusivulta painamalla **Clone or download** ja valitsemalla **Download ZIP**
* Pura tiedosto haluamaasi kansioon
* Luo virtuaaliympäristö navigoimalla komentorivillä projektin juurikansioon ja syöttämällä komento `python3 -m venv venv`
* Käynnistä virtuaaliympäristö asennusympäristöstä riippuen joko komennolla `source venv/bin/activate` tai `source venv/Scripts/activate`
* Lataa ja asenna sovelluksen riippuvuudet virtuaaliympäristöön komennolla `pip install -r requirements.txt`
* Käynnistä sovellus komennolla `python3 run.py`

## Sovelluksen siirtäminen verkkoon

Seuraavat työvälineet tulee olla asennettuna:
* git
* heroku-cli
* PostgreSQL

Oletetaan myös, että sovellukselle on tehty etärepositorio GitHubiin ja että Herokuun on luotu käyttäjätunnus

* Luo sovellukselle osoite Herokuun komennolla `heroku create`
* Lisää versionhallintaan tieto sovelluksen Heroku-osoitteesta komennolla `git remote add heroku https://git.heroku.com/<HEROKUN_LUOMA_NIMI>.git`
* Lisää Herokuun ympäristömuuttuja HEROKU=1 komennolla `heroku config:set HEROKU=1`
* Luo sovellukselle uusi tietokanta komennolla `heroku addons:add heroku-postgresql:hobby-dev`
* Lähetä projekti Herokuun komennoilla `git add .` ja `git commit -m "Initial commit"` sekä `git push heroku master`
* Sovelluksen pitäisi olla nyt käytettävissä Herokun aiemmin luomassa osoitteessa