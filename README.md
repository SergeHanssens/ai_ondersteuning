# Leren met AI — overzichtswebsite

Een statische website die toont welke digitale leerhulpmiddelen Serge Hanssens met AI
ontwikkelde: voor zijn lessen elektriciteit en mechanica bij GO! KTA Da Vinci Edegem,
en voor een leerling thuis met specifieke ondersteuningsnoden.

De site is bedoeld voor directie, zorgteam, leerkrachten en ouders. Ze toont dertien
voorbeelden; zes daarvan staan er als werkende toepassing bij, de andere alleen als
schermafbeelding omdat ze cursusmateriaal van een uitgeverij volgen.

**Live:** https://sergehanssens.github.io/ai_ondersteuning/

## Lokaal bekijken

De site is volledig statisch en gebruikt relatieve paden. Dubbelklikken op `index.html`
werkt, maar met een lokale server is het gedrag identiek aan de gehoste versie:

```bash
python3 -m http.server 8000
# open daarna http://localhost:8000
```

Er is geen build-stap, geen package manager en geen afhankelijkheid buiten één
weblettertype (Atkinson Hyperlegible via Google Fonts). Zonder internet valt de site
terug op Verdana en blijft alles werken.

## Mapstructuur

```
index.html                     de overzichtspagina
assets/css/stijl.css           opmaak (licht en donker)
assets/js/filter.js            filters in de galerij; de site werkt ook zonder JavaScript
assets/img/                    SHiftEDMake-logo en kubus
assets/img/screenshots/        schermafbeeldingen, telkens groot en klein
demos/                         de werkende toepassingen, elk één standalone HTML-bestand
INVENTARIS.md                  welke bronbestanden geselecteerd zijn en waar ze vandaan komen
LICENTIES.md                   licenties en wat bewust niet gepubliceerd is
CNAME                          het eigen domein voor GitHub Pages
```

## Hosten

De site draait op GitHub Pages vanaf de `main`-branch, map `/ (root)`.

1. **Settings → Pages**: Source = *Deploy from a branch*, Branch = `main`, map `/ (root)`.
Dat is alles — de site draait op `https://sergehanssens.github.io/ai_ondersteuning/`.

### Later overzetten naar schoolondersteuning.shiftedmake.com

1. Bij OVH (daar staat de DNS van `shiftedmake.com`) een `CNAME`-record toevoegen in de
   zone `shiftedmake.com`:

   | Subdomein | Type | TTL | Doel |
   |---|---|---|---|
   | `schoolondersteuning` | `CNAME` | standaard | `sergehanssens.github.io.` (met het punt op het einde) |

2. In **Settings → Pages → Custom domain** `schoolondersteuning.shiftedmake.com` invullen
   en bewaren. GitHub maakt dan zelf een `CNAME`-bestand in deze repo aan.
3. Wachten tot de DNS-controle groen is (meestal tien minuten tot een uur) en daarna
   **Enforce HTTPS** aanzetten.

Alle paden in de site zijn relatief, dus ze werkt zowel onder een submap als op een
eigen domein. Er hoeft niets aan de inhoud te veranderen.

Bij een andere statische host (Netlify, Cloudflare Pages) volstaat het om deze map te
uploaden. Er is niets te bouwen.

## De website aanpassen

`index.html` is gegenereerd uit een datastructuur. De bronscripts (`data.py`, `bouw.py`)
staan in `tools/`. Een inhoudelijke wijziging doe je in `tools/data.py` en daarna:

```bash
python3 tools/bouw.py
```

Wie liever rechtstreeks in `index.html` werkt, kan dat ook — de generator is een
hulpmiddel, geen verplichting.

## Licentie

Code en zelf geschreven voorbeeldinhoud: MIT (zie `LICENSE`).
Bestaand cursusmateriaal, afbeeldingen en logo's van uitgeverijen en scholen vallen
hier niet onder en staan niet in deze repo. Zie `LICENTIES.md`.
