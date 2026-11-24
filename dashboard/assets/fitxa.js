/* Fitxa d'empresa: filtre de proves per any i obertura dels plegables segons el hash.
   Generat per dashboard/genera_dashboard.py. Sense dependències. */
(function () {
  'use strict';
  var cont = document.getElementById('proves');
  var proves = cont ? cont.querySelectorAll('.prova[data-anys]') : [];
  var grups = cont ? cont.querySelectorAll('.grup-proves') : [];
  var xips = cont ? cont.querySelectorAll('.xip[data-filtre-any]') : [];
  var estat = document.getElementById('estat-filtre');

  function filtra(any) {
    var n = 0;
    Array.prototype.forEach.call(proves, function (p) {
      var ok = !any || (' ' + p.getAttribute('data-anys') + ' ').indexOf(' ' + any + ' ') >= 0;
      p.hidden = !ok;
      if (ok) n++;
    });
    Array.prototype.forEach.call(grups, function (g) {
      var vis = g.querySelectorAll('.prova:not([hidden])').length;
      g.hidden = vis === 0;
      if (any && vis) g.open = true;
      var comptador = g.querySelector('summary .n');
      if (comptador) comptador.textContent = vis;
    });
    Array.prototype.forEach.call(xips, function (x) { x.setAttribute('aria-pressed', x.getAttribute('data-filtre-any') === any ? 'true' : 'false'); });
    if (estat) {
      estat.textContent = any ? ('Es mostren ' + n + (n === 1 ? ' prova' : ' proves') + ' que cobreixen el ' + any + '.') : '';
    }
  }

  function obre() {
    var id = decodeURIComponent(location.hash.replace(/^#/, ''));
    if (!id) return;
    var el = document.getElementById(id);
    if (!el) return;
    if (el.tagName === 'DETAILS') { el.open = true; }
    var pare = el.parentElement;
    while (pare) {
      if (pare.tagName === 'DETAILS') { pare.open = true; }
      if (pare.hidden && pare.classList.contains('grup-proves')) { filtra(''); }
      pare = pare.parentElement;
    }
    if (el.hidden) { filtra(''); }
    el.scrollIntoView();
  }

  document.addEventListener('click', function (ev) {
    var el = ev.target.closest ? ev.target.closest('[data-filtre-any]') : null;
    if (!el || !proves.length) return;
    var any = el.getAttribute('data-filtre-any') || '';
    if (el.tagName !== 'A') ev.preventDefault();
    filtra(any);
  });
  // Un enllaç al mateix hash no dispara «hashchange»: es torna a obrir a mà.
  document.addEventListener('click', function (ev) {
    var a = ev.target.closest ? ev.target.closest('a[href^="#any-"], a[href^="#p-"]') : null;
    if (a && a.hash && a.hash === location.hash) { obre(); }
  });
  window.addEventListener('hashchange', obre);
  obre();
})();
