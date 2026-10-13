# Licenties en wat bewust niet gepubliceerd is

## Wat onder MIT valt

De MIT-licentie in `LICENSE` geldt voor:

- `index.html`, `assets/css/stijl.css`, `assets/js/filter.js`, `tools/`
- `demos/demo-begrippen-oefenen.html` — code én de voorbeeldinhoud over elektrische
  grootheden, die voor deze demo zelf geschreven is
- de zes overgenomen toepassingen in `demos/`, die in hun eigen bestand al een
  MIT-licentieblok met copyright Serge Hanssens dragen

De MIT-licentie is **niet** automatisch op alles toegepast. Ze staat alleen op eigen
code en eigen inhoud.

## Wat niet van mij is

- **Het SHiftEDMake-logo en de kubus** (`assets/img/`) zijn het beeldmerk van
  SHiftEDMake. Ze vallen niet onder de MIT-licentie en mogen niet gebruikt worden om
  ander werk als SHiftEDMake te presenteren.
- **Het logo van GO! KTA da Vinci** zit ingebakken in enkele van de overgenomen
  toepassingen, omdat die voor die school gemaakt zijn. Het blijft eigendom van de
  school. Wie de code hergebruikt, vervangt het door een eigen logo.
- **Atkinson Hyperlegible** is een lettertype van het Braille Institute of America,
  onder SIL Open Font License. Het wordt via Google Fonts geladen, niet meegeleverd.
- **KaTeX** zit ingebouwd in enkele toepassingen voor de formuleweergave, onder
  MIT-licentie (© Khan Academy).
- **Leerplandoelen** die in de planningstool voorkomen, komen van de
  onderwijsverstrekker. Die tool staat daarom niet in deze repo.

## Wat bewust niet gepubliceerd is

| Wat | Waarom |
|---|---|
| De studie-apps biologie, chemie, fysica en godsdienst | De inhoud volgt een handboek van een uitgeverij. Publiceren zou dat cursusmateriaal verspreiden. Alleen schermafbeeldingen staan op de site. |
| De hoofdstukbundels van de leerapp elektriciteit A1 | Bevatten overgenomen cursusbeelden. Bovendien tot 128 MB per bestand. |
| De hoofdstukbundels van het Leeratelier ET | Zelfde reden. |
| De planningstool Leerlijnen EMT | Interne planningstool met leerplantekst van de onderwijsverstrekker. |
| Het onderdeel "klaswerk naast de oplossing" | Bevat werk van een leerling zelf. |

## Privacycontrole op wat wél gepubliceerd is

Voor publicatie is elk bestand in `demos/` nagekeken op:

- namen van leerlingen, resultaten en voortgang — **geen gevonden**; in de
  schermafbeeldingen is de voornaam van de leerling vervangen door een neutrale
  aanduiding
- persoonlijke of medische informatie — **geen gevonden**, en diagnoses worden op de
  site bewust niet aan een persoon gekoppeld
- API-sleutels, tokens en wachtwoorden — **geen gevonden**
- interne schoollinks (Smartschool, gedeelde mappen) — **geen gevonden**
- uitgaande verbindingen — alleen `shiftedmake.com`, `ktadavinci.be`,
  `educationendowmentfoundation.org.uk`, `udlguidelines.cast.org` en `thomasmore.be`,
  allemaal als gewone link. Geen enkele toepassing stuurt tijdens het gebruik gegevens
  weg.

## Wat nog gecontroleerd moet worden

- De toepassingen zijn getest in Chromium. Safari op iPad en iPhone is niet getest;
  daar gedraagt de voorleesfunctie zich soms anders.
- Er is niet getest met een schermlezer door iemand die er dagelijks mee werkt.
