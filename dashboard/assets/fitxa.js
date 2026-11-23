/* Filtre de proves per any a la fitxa. Generat per dashboard/genera_dashboard.py. Sense dependències. */
(function () {
  'use strict';
  var cont = document.getElementById('proves');
  if (!cont) return;
  var proves = cont.querySelectorAll('.prova[data-anys]');
  var grups = cont.querySelectorAll('.grup-proves');
  var xips = cont.querySelectorAll('.xip[data-filtre-any]');
  var estat = document.getElementById('estat-filtre');
  if (!proves.length) return;

  function filtra(any) {
    var n = 0;
    proves.forEach(function (p) {
      var ok = !any || (' ' + p.getAttribute('data-anys') + ' ').indexOf(' ' + any + ' ') >= 0;
      p.hidden = !ok;
      if (ok) n++;
    });
    grups.forEach(function (g) {
      var vis = g.querySelectorAll('.prova:not([hidden])').length;
      g.hidden = vis === 0;
      var comptador = g.querySelector('h3 .n');
      if (comptador) comptador.textContent = vis;
    });
    xips.forEach(function (x) { x.setAttribute('aria-pressed', x.getAttribute('data-filtre-any') === any ? 'true' : 'false'); });
    if (estat) {
      estat.textContent = any ? ('Es mostren ' + n + (n === 1 ? ' prova' : ' proves') + ' que cobreixen el ' + any + '.') : '';
    }
  }

  document.addEventListener('click', function (ev) {
    var el = ev.target.closest ? ev.target.closest('[data-filtre-any]') : null;
    if (!el) return;
    var any = el.getAttribute('data-filtre-any') || '';
    if (el.tagName !== 'A') ev.preventDefault();
    filtra(any);
  });
})();
