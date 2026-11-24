/* Fitxa d'empresa: franja d'anys (fletxes ←/→), obertura de l'any i de les proves
   segons el hash i filtre de proves per any. Generat per dashboard/genera_dashboard.py. Sense dependències. */
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

  /* Franja d'anys: una sola parada de tabulació i fletxes per passar d'any. */
  var rail = document.querySelector('.rail');
  var anys = rail ? Array.prototype.slice.call(rail.querySelectorAll('a.rl')) : [];
  function marcaAny(any) {
    var actual = null;
    anys.forEach(function (a) {
      var on = a.getAttribute('href') === '#any-' + any;
      if (on) { a.setAttribute('aria-current', 'true'); actual = a; } else { a.removeAttribute('aria-current'); }
    });
    anys.forEach(function (a) { a.tabIndex = a === (actual || anys[anys.length - 1]) ? 0 : -1; });
  }
  if (anys.length) {
    var cur = rail.querySelector('a.rl[aria-current]');
    anys.forEach(function (a) { a.tabIndex = a === (cur || anys[anys.length - 1]) ? 0 : -1; });
    rail.addEventListener('keydown', function (ev) {
      var i = anys.indexOf(document.activeElement);
      if (i < 0) return;
      var j = ev.key === 'ArrowRight' || ev.key === 'ArrowDown' ? i + 1 : ev.key === 'ArrowLeft' || ev.key === 'ArrowUp' ? i - 1 :
        ev.key === 'Home' ? 0 : ev.key === 'End' ? anys.length - 1 : null;
      if (j === null) return;
      ev.preventDefault();
      j = Math.max(0, Math.min(anys.length - 1, j));
      anys.forEach(function (a, k) { a.tabIndex = k === j ? 0 : -1; });
      anys[j].focus();
    });
  }

  var inici = true;
  function obre() {
    var id = '';
    try { id = decodeURIComponent(location.hash.replace(/^#/, '')); } catch (e) { id = ''; }
    var el = id ? document.getElementById(id) : null;
    if (!el) { inici = false; return; }
    if (/^any-\d{4}$/.test(id)) {
      var plegable = el.querySelector('details.tl-evid');
      if (plegable) plegable.open = true;
      // En obrir la pàgina amb un any, es tanca l'any obert per defecte (l'últim).
      if (inici) {
        var def = document.querySelector('details.tl-evid[data-defecte]');
        if (def && def !== plegable) def.open = false;
      }
      marcaAny(id.slice(4));
    } else {
      if (el.tagName === 'DETAILS') { el.open = true; }
      var pare = el.parentElement;
      while (pare) {
        if (pare.tagName === 'DETAILS') { pare.open = true; }
        if (pare.hidden && pare.classList.contains('grup-proves')) { filtra(''); }
        pare = pare.parentElement;
      }
      if (el.hidden) { filtra(''); }
    }
    inici = false;
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
