# -*- coding: utf-8 -*-
import html, pathlib, sys
HIER = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HIER))
from data import ITEMS, SOORTEN, NODEN

E = lambda s: html.escape(s, quote=True)

VAKMAP = {
 "Elektriciteit en mechanica": ["Elektriciteit","Mechanica"],
 "Elektriciteit, mechanica": ["Elektriciteit","Mechanica"],
 "Elektriciteit (voorbeeldinhoud)": ["Elektriciteit"],
}
def vakken_van(v): return VAKMAP.get(v, [v])
OUT = HIER.parent / "index.html"

def ul(items, cls=""):
    return f'<ul class="{cls}">' + "".join(f"<li>{E(x)}</li>" for x in items) + "</ul>"

CTX = {"davinci":"KTA da Vinci", "thuis":"Individuele ondersteuning", "demo":"Demo"}

def kaart(it):
    chips = "".join(f'<span class="chip">{E(SOORTEN[s])}</span>' for s in it["soort"] if s in SOORTEN)
    nodenattr = " ".join(it["noden"])
    vakattr = "|" + "|".join(vakken_van(it["vak"])) + "|"
    soortattr = " ".join(it["soort"])
    shot = it.get("shot")
    beeld = (f'<a class="beeld" href="assets/img/screenshots/{shot}.jpg" target="_blank" rel="noopener">'
             f'<img src="assets/img/screenshots/{shot}-klein.jpg" alt="Schermafbeelding van {E(it["titel"])}" loading="lazy" width="760" height="510">'
             f'<span class="vergroot">Vergroot</span></a>') if shot else \
            '<div class="beeld geenbeeld"><span>Werkende demo — open ze hieronder</span></div>'
    knoppen = []
    if it.get("demo"):
        knoppen.append(f'<a class="knop hoofd" href="{it["demo"]}">Open de toepassing</a>')
        if it.get("demo2"):
            knoppen.append(f'<a class="knop" href="{it["demo2"]}">{E(it["demo2label"])}</a>')
    else:
        knoppen.append(f'<span class="niet" title="{E(it["demoreden"])}">Niet publiek te delen</span>')
        if "demo met eigen voorbeeldinhoud" in (it.get("demoreden") or ""):
            knoppen.append('<a class="knop" href="demos/demo-begrippen-oefenen.html">Open de demo in de plaats</a>')
    return f'''
<article class="kaart" data-vak="{E(vakattr)}" data-soort="{E(soortattr)}" data-noden="{E(nodenattr)}" data-context="{it["context"]}" id="{it["id"]}">
  {beeld}
  <div class="kaartlijf">
    <p class="herkomst herkomst-{it["context"]}">{E(CTX[it["context"]])}</p>
    <h3>{E(it["titel"])}</h3>
    <p class="meta">{E(it["vak"])} · {E(it["doelgroep"])}</p>
    <p class="kort">{E(it["kort"])}</p>
    <p class="chips">{chips}</p>
    <details>
      <summary>Meer over deze toepassing</summary>
      <div class="diep">
        <h4>Waarom ze gemaakt is</h4><p>{E(it["aanleiding"])}</p>
        <h4>De oorspronkelijke insteek</h4><p>{E(it["insteek"])}</p>
        <h4>Wat de leerling doet</h4><p>{E(it["doet"])}</p>
        <h4>Wat het oplevert voor het leren</h4><p>{E(it["waarde"])}</p>
        <h4>De rol van AI</h4><p>{E(it["ai"])}</p>
        <h4>Toegankelijkheid <span class="badge badge-ja">gecontroleerde functies</span></h4>
        {ul(it["toeg"], "vink")}
        <h4>Mogelijke ondersteuning <span class="badge badge-mss">mogelijke inzet</span></h4><p>{E(it["steun"])}</p>
        <h4>Beperkingen en aandachtspunten</h4><p>{E(it["beperk"])}</p>
      </div>
    </details>
    <p class="acties">{"".join(knoppen)}</p>
  </div>
</article>'''

kaarten = "\n".join(kaart(i) for i in ITEMS)
vakken = sorted({v for i in ITEMS for v in vakken_van(i["vak"])})
vakknoppen = "".join(f'<button class="filter" data-groep="vak" data-waarde="{E(v)}">{E(v)}</button>' for v in vakken)
soortknoppen = "".join(f'<button class="filter" data-groep="soort" data-waarde="{k}">{E(v)}</button>' for k,v in SOORTEN.items())
nodenknoppen = "".join(f'<button class="filter" data-groep="noden" data-waarde="{k}">{E(v)}</button>' for k,v in NODEN.items())

HTML = f'''<!doctype html>
<html lang="nl-BE">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Leren met AI — toepassingen voor de klas en voor thuis</title>
<meta name="description" content="Een overzicht van digitale leerhulpmiddelen die Serge Hanssens met AI ontwikkelde voor zijn leerlingen en voor thuis, met werkende voorbeelden, toegankelijkheidsfuncties en eerlijke beperkingen.">
<meta name="author" content="Serge Hanssens — SHiftEDMake">
<meta name="color-scheme" content="light dark">
<meta property="og:title" content="Leren met AI — toepassingen voor de klas en voor thuis">
<meta property="og:description" content="Werkende voorbeelden van leerapps, simulaties en oefenmodules, met uitleg over toegankelijkheid en over wat AI wel en niet doet.">
<meta property="og:type" content="website">
<link rel="icon" href="assets/img/shiftedmake-kubus.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400;1,700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/stijl.css">
</head>
<body>
<a class="overslaan" href="#galerij">Ga meteen naar de voorbeelden</a>

<header class="kop">
  <div class="omhulsel kopbinnen">
    <p class="merkplaat"><img class="merk" src="assets/img/shiftedmake-logo.png" alt="SHiftEDMake — van Droom naar Werkelijkheid" width="900" height="212"></p>
    <div>
      <p class="bovenkop">Leermateriaal maken met AI</p>
      <h1>Wat ik gemaakt heb, en waarom</h1>
      <p class="onderkop">Digitale leerhulpmiddelen voor mijn eigen lessen elektriciteit en mechanica, en voor een leerling thuis met specifieke ondersteuningsnoden. Hieronder staan dertien voorbeelden. Zes ervan kun je meteen openen en uitproberen.</p>
      <p class="acties">
        <a class="knop hoofd" href="#galerij">Bekijk de voorbeelden</a>
        <a class="knop" href="demos/demo-begrippen-oefenen.html">Probeer meteen een oefening</a>
      </p>
    </div>
  </div>
</header>

<nav class="kruimels" aria-label="Op deze pagina">
  <div class="omhulsel">
    <a href="#waarom">Waarom</a>
    <a href="#galerij">De voorbeelden</a>
    <a href="#noden">Ondersteuningsnoden</a>
    <a href="#werkwijze">Mijn werkwijze</a>
    <a href="#grenzen">Grenzen</a>
    <a href="#meer">Meer</a>
  </div>
</nav>

<main>

<section id="waarom" class="omhulsel vak">
  <h2>Waarom ik hieraan begon</h2>
  <div class="tweekolom">
    <div>
      <p>Ik geef elektriciteit en mechanica in de derde graad elektromechanische technieken bij GO! KTA Da Vinci in Edegem. Daarnaast maak ik leermateriaal voor mijn zoon, die schoolloopt in het buitengewoon secundair onderwijs. Dat zijn twee heel verschillende scholen en twee heel verschillende vragen, en ik hou ze op deze pagina ook uit elkaar.</p>
      <p>Wat ze gemeen hebben: een handboek is geschreven voor de gemiddelde lezer. Wie trager leest, nieuwe woorden moeilijk onthoudt of de draad kwijtraakt in een lange tekst, komt er niet zelfstandig door. Dan blijft er maar één oplossing over — iemand die er elke avond naast gaat zitten. Dat is wat ik wilde verminderen.</p>
    </div>
    <div>
      <p>Met AI kan ik lesmateriaal in een paar avonden omzetten naar iets wat een leerling alleen aankan: opgesplitst in korte sessies, met begrippen apart, met voorlezen overal en met oefeningen die feedback geven in plaats van alleen een punt. Vroeger was dat werk van maanden en deed niemand het.</p>
      <p>Ik deel dit omdat de vraag op de schoolraad kwam wat er mogelijk is. Ik ben geen leverancier en verkoop niets. Wie het interessant vindt, mag alles vrij gebruiken; de code staat onder een open licentie.</p>
    </div>
  </div>
  <div class="legende">
    <p class="legendekop">Hoe je deze pagina leest</p>
    <ul>
      <li><span class="badge badge-ja">gecontroleerde functie</span> Ik heb ze zelf in de toepassing nagekeken.</li>
      <li><span class="badge badge-mss">mogelijke inzet</span> Een plausibel verband tussen een functie en een drempel. Geen gemeten effect.</li>
      <li><span class="badge badge-tk">nog te doen</span> Een verbetering die er nog niet is.</li>
    </ul>
  </div>
</section>

<section id="galerij" class="omhulsel vak">
  <h2>De voorbeelden</h2>
  <p class="inleiding">Dertien toepassingen, van een hele cursus tot één oefenmodule. Zes ervan staan hier live en kun je openen; de andere volgen een handboek van een uitgeverij of bevatten overgenomen cursusbeelden, en daarvan staat alleen een schermafbeelding. Dat staat telkens bij het voorbeeld zelf.</p>

  <div class="filters" id="filters">
    <div class="filtergroep">
      <p class="filterkop" id="k-context">Context</p>
      <div role="group" aria-labelledby="k-context">
        <button class="filter" data-groep="context" data-waarde="davinci">Mijn lespraktijk — KTA da Vinci</button>
        <button class="filter" data-groep="context" data-waarde="thuis">Individuele ondersteuning thuis</button>
        <button class="filter" data-groep="context" data-waarde="demo">Werkende demo</button>
      </div>
    </div>
    <div class="filtergroep">
      <p class="filterkop" id="k-vak">Vak</p>
      <div role="group" aria-labelledby="k-vak">{vakknoppen}</div>
    </div>
    <div class="filtergroep">
      <p class="filterkop" id="k-soort">Soort toepassing</p>
      <div role="group" aria-labelledby="k-soort">{soortknoppen}</div>
    </div>
    <div class="filtergroep">
      <p class="filterkop" id="k-noden">Waarbij het kan helpen</p>
      <div role="group" aria-labelledby="k-noden">{nodenknoppen}</div>
    </div>
    <p class="filteractie"><button class="knop" id="wis" hidden>Wis alle filters</button> <span id="telling" aria-live="polite"></span></p>
  </div>

  <div class="galerij" id="rooster">
{kaarten}
  </div>
  <p id="leeg" class="leeg" hidden>Geen enkel voorbeeld voldoet aan deze combinatie. Wis een filter om verder te kijken.</p>
</section>

<section id="noden" class="vlak">
  <div class="omhulsel vak">
    <h2>Welke functie kan welke drempel verlagen?</h2>
    <p class="inleiding">Hieronder staat per functie wat ze ondersteunt en voor wie ze relevant kán zijn. Let op drie dingen. Deze begrippen zijn niet allemaal leerstoornissen — autisme en ADHD zijn ontwikkelingsstoornissen, een auditief verwerkingsprobleem is iets anders dan dyslexie. Dezelfde diagnose betekent niet dezelfde ondersteuningsbehoefte. En dit zijn geen gemeten effecten van mijn toepassingen: ik heb daar geen onderzoek naar gedaan.</p>
    <div class="tabelwikkel">
    <table>
      <caption>Van concrete functie naar ondersteunde vaardigheid naar mogelijke doelgroep</caption>
      <thead><tr><th scope="col">Functie in de toepassing</th><th scope="col">Wat ze ondersteunt</th><th scope="col">Voor wie dit relevant kan zijn</th></tr></thead>
      <tbody>
        <tr><td>Voorlezen met een Vlaamse stem, op elk tekstblok</td><td>Vermindert de leesdrempel: de leerling hoeft niet eerst te decoderen om bij de inhoud te komen.</td><td>Dyslexie en dysorthografie; leerlingen die traag lezen. Niet vanzelfsprekend bruikbaar bij auditieve verwerkingsproblemen — daar kan geluid net storen.</td></tr>
        <tr><td>Instelbare leessnelheid, pauzeren en hervatten</td><td>Geeft controle over het tempo van de uitleg.</td><td>Leerlingen die informatie trager verwerken, en leerlingen die vaak moeten terugspoelen.</td></tr>
        <tr><td>Eén kaart per scherm (focus-modus)</td><td>Neemt visuele afleiding weg en maakt zichtbaar wat de volgende stap is.</td><td>ADHD en aandachtsproblemen; leerlingen die vastlopen op een volle bladzijde.</td></tr>
        <tr><td>Vaste structuur en volgorde over alle vakken heen</td><td>Maakt het verloop voorspelbaar, zodat de aandacht naar de leerstof gaat en niet naar de bediening.</td><td>Autismespectrumstoornis; leerlingen die moeite hebben met wisselende werkvormen.</td></tr>
        <tr><td>Sessies van maximaal 20 tot 25 minuten met pauze</td><td>Houdt de taak afgebakend en voorzienbaar in tijd.</td><td>Leerlingen met een korte volgehouden aandacht, en leerlingen die snel vermoeid raken.</td></tr>
        <tr><td>Begrippenkaarten met herhaling op basis van gebruikte hulp</td><td>Ondersteunt het inslijpen van vaktaal: wat met hulp lukte, komt terug.</td><td>Automatiserings- en woordvindingsproblemen; taalontwikkelingsstoornis (STOS).</td></tr>
        <tr><td>Uitgewerkt voorbeeldantwoord, opvraagbaar en voorleesbaar</td><td>Toont niet alleen dát het fout was, maar hoe het antwoord eruitziet.</td><td>Leerlingen die vastlopen en afhaken bij een foutmelding zonder model.</td></tr>
        <tr><td>Simulatie waarin de leerling zelf een parameter verandert</td><td>Vult gesproken en geschreven uitleg aan met een beeld dat meebeweegt.</td><td>Leerlingen bij wie taal de flessenhals is, en wie abstracte verbanden moeilijk vasthoudt.</td></tr>
        <tr><td>Formules in echte wetenschappelijke notatie</td><td>Houdt de notatie consequent, zodat eenzelfde grootheid er overal hetzelfde uitziet.</td><td>Alle leerlingen; in het bijzonder wie moeite heeft met wisselende schrijfwijzen.</td></tr>
        <tr><td>Voortgang bewaard in het toestel zelf, zonder account</td><td>Geen aanmelding, geen gegevens die de school uit moeten.</td><td>Iedereen. Dit is een privacykeuze, geen ondersteuningsfunctie.</td></tr>
      </tbody>
    </table>
    </div>
    <p class="voetnoot">Onderbouwing bij de algemene principes, niet bij mijn toepassingen: de <a href="https://udlguidelines.cast.org/" target="_blank" rel="noopener">UDL-richtlijnen van CAST</a> over meerdere representatievormen, en de <a href="https://educationendowmentfoundation.org.uk/education-evidence/teaching-learning-toolkit" target="_blank" rel="noopener">Teaching and Learning Toolkit</a> van de Education Endowment Foundation over feedback en metacognitie. Voor het Vlaamse kader rond leerstoornissen en redelijke aanpassingen is <a href="https://onderwijs.vlaanderen.be/" target="_blank" rel="noopener">onderwijs.vlaanderen.be</a> het vertrekpunt. Wat ik <em>niet</em> kan onderbouwen, is of mijn apps leerwinst opleveren. Dat zou een opzet met een vergelijking vragen, en die is er niet.</p>
  </div>
</section>

<section id="werkwijze" class="omhulsel vak">
  <h2>Hoe ik met AI werk</h2>
  <div class="stappen">
    <div class="stap"><p class="stapnr">1</p><h3>De cursus is het vertrekpunt</h3><p>Ik vertrek altijd van het bestaande lesmateriaal, niet van wat een AI-model zelf over het onderwerp denkt. De leerstof, de volgorde en de terminologie komen uit de cursus.</p></div>
    <div class="stap"><p class="stapnr">2</p><h3>Eén vast sjabloon per soort app</h3><p>Elke app vertrekt van hetzelfde sjabloon. Daardoor werkt biologie exact zoals chemie, en moet een leerling de bediening maar één keer leren.</p></div>
    <div class="stap"><p class="stapnr">3</p><h3>Ik laat het nalezen, en lees daarna zelf na</h3><p>Een tweede AI-sessie controleert de app tegen de cursus: ontbreekt er een onderdeel, klopt elke berekening, zit er een fout in de oplossingen. Daarna ga ik er zelf door. Dat laatste blijft nodig — er zitten telkens fouten in.</p></div>
    <div class="stap"><p class="stapnr">4</p><h3>Eén bestand, offline, zonder account</h3><p>Elke toepassing is één HTML-bestand. Geen installatie, geen server, geen aanmelding, geen gegevens die weggaan. Je kunt het op een stick zetten en het werkt.</p></div>
    <div class="stap"><p class="stapnr">5</p><h3>Geen leerlinggegevens in een AI-tool</h3><p>Namen, resultaten, verslagen en diagnoses gaan niet in een AI-tool. Als ik een vraag stel over een leerling, dan functioneel beschreven en zonder naam.</p></div>
    <div class="stap"><p class="stapnr">6</p><h3>Tijdens het gebruik draait er geen AI</h3><p>In geen enkele toepassing hieronder staat AI aan terwijl de leerling werkt. Het nakijken gebeurt met antwoorden die ik vooraf heb ingesteld. Dat is bewust: het is voorspelbaar, het kost niets en er vertrekt geen enkel gegeven.</p></div>
  </div>
</section>

<section id="grenzen" class="vlak">
  <div class="omhulsel vak">
    <h2>Waar dit stopt</h2>
    <div class="tweekolom">
      <div>
        <h3>Vakinhoud en didactiek blijven mensenwerk</h3>
        <p>AI schrijft vlot en overtuigend, ook als het fout is. In elke app die ik gemaakt heb, zaten fouten: een verkeerde tussenstap, een begrip dat net naast de cursusdefinitie zat, een oefening met een onmogelijk antwoord. Die haal je er alleen uit door het vak te kennen en er zelf door te gaan. Een leerkracht die dit materiaal gebruikt, moet het dus eerst zelf nalezen.</p>
        <h3>Een app behandelt geen stoornis</h3>
        <p>Deze toepassingen verlagen drempels. Ze vervangen geen leerkracht, geen logopedist, geen leerondersteuner en geen handelingsplan. Ze zijn ook geen vervanging voor redelijke aanpassingen waar een leerling recht op heeft.</p>
      </div>
      <div>
        <h3>Wat ik niet weet</h3>
        <p>Ik heb geen metingen. Ik weet dat mijn zoon nu zelfstandig studeert waar dat vroeger niet lukte, en ik zie dat leerlingen de apps gebruiken. Dat is een observatie van één ouder en één leerkracht, geen bewijs. Of dit bij andere leerlingen werkt, moet blijken.</p>
        <h3>Wat nog te doen is <span class="badge badge-tk">nog te doen</span></h3>
        <ul class="vink nee">
          <li>Een versie die niet aan één handboek vasthangt, zodat ze wel gedeeld kan worden.</li>
          <li>Testen met een schermlezer door iemand die er dagelijks mee werkt.</li>
          <li>Een manier om te zien of een leerling vastloopt, zonder persoonsgegevens te verzamelen.</li>
          <li>Nakijken van open antwoorden dat verder gaat dan trefwoorden.</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section id="meer" class="omhulsel vak">
  <h2>Meer van hetzelfde werk</h2>
  <div class="links">
    <a class="linkkaart" href="https://onderwijsai.shiftedmake.com" target="_blank" rel="noopener">
      <h3>onderwijsai.shiftedmake.com</h3>
      <p>Handleidingen om AI didactisch in te zetten, per onderwijsniveau, vak, doelgroep en ondersteuningsbehoefte. Met kant-en-klare prompts. Gratis, onder CC BY-SA.</p>
    </a>
    <a class="linkkaart" href="https://linkbank.shiftedmake.com" target="_blank" rel="noopener">
      <h3>linkbank.shiftedmake.com</h3>
      <p>Een doorzoekbare verzameling onderwijs- en STEM-bronnen, met filters op niveau, vak en doel.</p>
    </a>
    <a class="linkkaart" href="https://stem-at-davinci.shiftedmake.com" target="_blank" rel="noopener">
      <h3>stem-at-davinci.shiftedmake.com</h3>
      <p>De leerlijnen van de eerste tot de derde graad bij KTA da Vinci, met de leerplandoelen per vak en jaar.</p>
    </a>
  </div>
  <p class="voetnoot">Het adres <strong>stem-at-davici</strong> met één n bestaat niet; de werkende versie is <strong>stem-at-davinci</strong>.</p>
</section>

</main>

<footer class="voet">
  <div class="omhulsel">
    <img class="kubus" src="assets/img/shiftedmake-kubus.png" alt="" width="120" height="129">
    <p><strong>Serge Hanssens</strong> — leerkracht elektriciteit en mechanica, GO! KTA Da Vinci Edegem. Maker onder de naam SHiftEDMake.</p>
    <p>Het werk voor KTA da Vinci staat hier als voorbeeld uit mijn eigen lespraktijk. Het materiaal voor thuis is ontstaan uit één individuele ondersteuningsvraag en is geen schoolproject.</p>
    <p>Code en zelf geschreven voorbeeldinhoud onder MIT-licentie. Bestaand cursusmateriaal, afbeeldingen en logo's van uitgeverijen en scholen blijven van hun rechthebbenden en staan niet op deze site.</p>
    <p class="klein">Laatst bijgewerkt op 13 oktober 2026 · <a href="https://github.com/SergeHanssens/ai_ondersteuning" target="_blank" rel="noopener">broncode op GitHub</a></p>
  </div>
</footer>

<script src="assets/js/filter.js"></script>
</body>
</html>
'''
OUT.write_text(HTML, encoding="utf-8")
print("geschreven:", OUT, len(HTML), "tekens")
