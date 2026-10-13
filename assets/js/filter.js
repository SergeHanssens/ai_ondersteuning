/* Filters voor de galerij. Werkt progressief: zonder JS staan alle kaarten er gewoon. */
(function () {
  "use strict";
  var actief = { context: [], vak: [], soort: [], noden: [] };
  var kaarten = Array.prototype.slice.call(document.querySelectorAll("#rooster .kaart"));
  var knoppen = Array.prototype.slice.call(document.querySelectorAll(".filter"));
  var wis = document.getElementById("wis");
  var telling = document.getElementById("telling");
  var leeg = document.getElementById("leeg");

  knoppen.forEach(function (b) {
    b.setAttribute("aria-pressed", "false");
    b.addEventListener("click", function () {
      var g = b.dataset.groep, w = b.dataset.waarde, i = actief[g].indexOf(w);
      if (i === -1) { actief[g].push(w); b.setAttribute("aria-pressed", "true"); }
      else { actief[g].splice(i, 1); b.setAttribute("aria-pressed", "false"); }
      pas();
    });
  });

  function raak(kaart, groep) {
    if (!actief[groep].length) return true;
    var veld = kaart.dataset[groep] || "";
    if (groep === "context") return actief[groep].indexOf(veld) !== -1;
    if (groep === "vak") return actief[groep].some(function (w) { return veld.indexOf("|" + w + "|") !== -1; });
    var heeft = veld.split(" ");
    return actief[groep].some(function (w) { return heeft.indexOf(w) !== -1; });
  }

  function pas() {
    var n = 0;
    kaarten.forEach(function (k) {
      var toon = raak(k, "context") && raak(k, "vak") && raak(k, "soort") && raak(k, "noden");
      k.hidden = !toon;
      if (toon) n++;
    });
    var totaal = Object.keys(actief).reduce(function (s, g) { return s + actief[g].length; }, 0);
    wis.hidden = totaal === 0;
    telling.textContent = totaal === 0
      ? ""
      : (n === 1 ? "1 voorbeeld past bij je keuze." : n + " voorbeelden passen bij je keuze.");
    leeg.hidden = n !== 0;
  }

  wis.addEventListener("click", function () {
    Object.keys(actief).forEach(function (g) { actief[g] = []; });
    knoppen.forEach(function (b) { b.setAttribute("aria-pressed", "false"); });
    pas();
    document.getElementById("filters").scrollIntoView({ block: "nearest" });
  });

  pas();
})();
