# Gerichte toegankelijkheidscontrole

Scope: `demos/demo-begrippen-oefenen.html`, `index.html`, `assets/css/stijl.css`
en `assets/js/filter.js`. Basiscommit: `21a3bf8bfdf628a7a953eeb1ee875b9ec246ce64`.
Dit is een broncodecontrole met berekende contrasten en beperkte logische tests,
geen volledige WCAG-audit of praktijktest met ondersteunende technologie.

## Vastgesteld en aangepast

- Demo: een selectorlijst bevatte ten onrechte `@media`. De gewone linkkleur
  gebruikt nu `var(--focus)`, dat al correct wordt ingesteld voor automatisch donker,
  expliciet donker en expliciet licht. De afzonderlijke kleur van de teruglink in
  de donkere kop blijft gelden; de berekening hieronder betreft de algemene linkregel.
- Witte tekst op de lichtpaarse actieve knoppen/filters (2,36:1) wordt donkere tekst.
  Dit geldt ook voor de overslaanlink van het overzicht in donkere modus.
- De focusring krijgt in de blijvend donkere kop en overzichtsvoet een gele kleur.
- Twee kleine herkomstlabels en groene feedback in lichte modus hadden onvoldoende
  tekstcontrast. De kleuren zijn iets donkerder gemaakt.
- Demo: de feedbackregio blijft vanaf het laden aanwezig als `role="status"`;
  alleen tekst en opmaak veranderen. Dit biedt schermlezers een stabiele live-regio.
- De voorbeeldknop heeft `aria-controls` en een gesynchroniseerde `aria-expanded`.
  De themaknop heeft een vaste naam en `aria-pressed`, ook na systeemthemawijzigingen.
  De vraag is via `aria-describedby` gekoppeld aan het antwoordveld.
- Focus gaat na nakijken naar Volgende, na doorgaan naar de nieuwe begripskop en
  bij afronden/herstarten naar de passende kop. Bij filters wissen gaat focus naar
  de eerste filter voordat de wisknop verdwijnt. Het overzicht meldt ook het herstel
  van alle voorbeelden in de bestaande live-regio.
- Feedback beschrijft trefwoordherkenning in plaats van inhoudelijke juistheid te
  garanderen. Het label voor zelfcontrole belooft geen scorewijziging meer die de
  handler niet uitvoert.

## Contrastberekening (sRGB)

Voor gewone tekst is 4,5:1 als grens gebruikt; voor de focusindicator 3:1.

| Combinatie | Voor | Na |
|---|---:|---:|
| Algemene demolink op #131920 | 2,86 | 7,49 |
| Algemene demolink op kaart #1b232d | 2,56 | 6,71 |
| Actieve knop: tekst op #b79bea | 2,36 | 7,49 demo / 7,55 overzicht |
| Herkomst KTA-label op wit | 4,27 | 5,69 |
| Herkomst Demo-label op wit | 4,38 | 5,76 |
| Groene feedback op #e7f6f0 | 4,45 | 5,08 |
| Focusring op kop #2c3e50 | 1,78 | 7,22 |

Ook de reguliere tekst-, secundaire tekst-, hulpfeedback- en badgekleuren zijn
tegen hun opgegeven achtergronden berekend in beide thema's: minimaal 4,5:1.
De primaire demoknop behoudt wit op donkerpaars (6,18:1).

## Wat is gecontroleerd

- Broncode: taal, viewport, koppen, landmarks, expliciet invoerlabel, benoemde
  voorleesknoppen, native buttons/links/details/summary, filtergroepen met namen,
  filterstatus met aria-pressed en verborgen kaarten met hidden.
- Beide pagina's bevatten zichtbare focusregels; de demo respecteert reduced motion.
- JavaScript-syntaxis van demo en filterbestand en `git diff --check` slagen.
- Tijdelijke Node-test met een nagebootste DOM: thema- en voorbeeldstatus,
  lege invoer, focus na nakijken/doorgaan/afronden/herstarten slagen.
  Dit test de logica, niet rendering of werkelijk schermlezergedrag.
- Er is geen browsertest uitgevoerd: de lokale Chromium-binary ontbrak en de
  browserdownload mislukte. De bestaande testvermelding in LICENTIES.md is niet
  uitgebreid op basis van deze controle.

## Nog daadwerkelijk testen

1. Desktopbrowser, met alleen Tab, Shift+Tab, Enter en spatie: volledige oefening,
   voorbeeld tonen/verbergen, filters en wissen; controleer zichtbare/onbedekte focus
   en de leesvolgorde. Test automatisch licht/donker én beide handmatige overrides.
2. Safari op een echte iPhone en iPad: weergave bij grote tekst/zoom en smalle breedte,
   bediening met schermtoetsenbord, voorleesstem kiezen/laden, starten/stoppen,
   voortgang bewaren en hervatten. Controleer eventuele horizontale overloop.
3. VoiceOver op iOS en bijvoorbeeld NVDA op Windows: worden nieuwe feedback,
   filterresultaten, vraagbeschrijving, knopstatussen en de afronding begrijpelijk
   aangekondigd? Controleer of focusverplaatsing live-meldingen onderbreekt en of
   de ingebouwde spraakfunctie niet door de schermlezer heen praat.
4. Visueel: zoom 200–400%, navigatiebalk en focusranden bij scrollcontainers,
   hoogcontrastmodus en alle hover/focus-toestanden. Broncode alleen bewijst niet
   dat focus overal zichtbaar blijft of dat een pagina op mobiel goed herschikt.

Deze open punten blijven gelden; aanwezigheid van ARIA is geen bewijs dat een
schermlezer de melding correct uitspreekt.
