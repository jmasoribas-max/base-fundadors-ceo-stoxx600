/* Cercador i filtres d'Empreses. Generat per dashboard/genera_dashboard.py. Sense dependències. */
(function () {
  'use strict';
  var taula = document.getElementById('taula');
  if (!taula) return;
  var tbody = taula.tBodies[0];
  var files = Array.prototype.slice.call(tbody.rows);
  var camps = {
    q: document.getElementById('f-q'),
    e: document.getElementById('f-e'),
    t: document.getElementById('f-t'),
    p: document.getElementById('f-p'),
    m: document.getElementById('f-m')
  };
  var campM = document.getElementById('camp-m');
  var nVis = document.getElementById('n-visibles');
  var cap = document.getElementById('cap-resultat');
  var ordre = { clau: 'n', dir: 1 };
  var IDX = { acabada: 0, arxiu: 1, dubte: 2, falta: 3 };

  function norm(s) {
    return (s || '').normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase().replace(/\s+/g, ' ').trim();
  }
  function fmt(n) { return String(n).replace(/\B(?=(\d{3})+(?!\d))/g, '.'); }
  function conte(llista, valor) { return (' ' + (llista || '') + ' ').indexOf(' ' + valor + ' ') >= 0; }
  function st(tr) { return (tr.dataset.st || '0 0 0 0').split(' ').map(Number); }
  // Claus d'ordre: el nom normalitzat i el % de files acabades (no van a l'HTML).
  files.forEach(function (tr) {
    var a = tr.querySelector('.emp-nom'), s = st(tr), n = s[0] + s[1] + s[2] + s[3];
    tr._ordre = { n: norm(a ? a.textContent : ''), pa: n ? Math.round(100 * s[0] / n) : 0 };
  });
  function clauOrdre(tr, clau) { return clau === 'f' ? +tr.dataset.f : tr._ordre[clau]; }

  function aplica() {
    var termes = norm(camps.q.value).split(' ').filter(Boolean);
    var e = camps.e.value, t = camps.t.value, p = camps.p.value, m = camps.m.value;
    campM.hidden = !m;
    var n = 0;
    for (var i = 0; i < files.length; i++) {
      var tr = files[i], d = tr.dataset, ok = true;
      for (var j = 0; j < termes.length && ok; j++) { if (d.c.indexOf(termes[j]) < 0) ok = false; }
      if (ok && e && !conte(d.e, e)) ok = false;
      if (ok && p && d.p !== p) ok = false;
      if (ok && m && !conte(d.m, m)) ok = false;
      if (ok && t) {
        var s = st(tr);
        if (t === 'totes') { ok = s[0] === s[0] + s[1] + s[2] + s[3]; }
        else if (t in IDX) { ok = s[IDX[t]] > 0; }
      }
      tr.hidden = !ok;
      if (ok) n++;
    }
    nVis.textContent = fmt(n);
    cap.hidden = n > 0;
    desa();
  }

  function ordena(clau) {
    if (ordre.clau === clau) { ordre.dir = -ordre.dir; } else { ordre.clau = clau; ordre.dir = clau === 'n' ? 1 : -1; }
    var num = clau !== 'n';
    files.sort(function (a, b) {
      var x = clauOrdre(a, clau), y = clauOrdre(b, clau), r;
      if (num) { r = x - y; } else { r = x < y ? -1 : x > y ? 1 : 0; }
      if (r === 0) { return a._ordre.n < b._ordre.n ? -1 : a._ordre.n > b._ordre.n ? 1 : 0; }
      return r * ordre.dir;
    });
    var frag = document.createDocumentFragment();
    files.forEach(function (tr) { frag.appendChild(tr); });
    tbody.appendChild(frag);
    taula.querySelectorAll('thead button[data-ordre]').forEach(function (b) {
      var th = b.parentElement;
      if (b.getAttribute('data-ordre') === ordre.clau) { th.setAttribute('aria-sort', ordre.dir > 0 ? 'ascending' : 'descending'); }
      else { th.removeAttribute('aria-sort'); }
    });
  }

  function desa() {
    var params = [];
    ['q', 'e', 't', 'p', 'm'].forEach(function (k) {
      if (camps[k] && camps[k].value) params.push(k + '=' + encodeURIComponent(camps[k].value));
    });
    var hash = params.length ? '#' + params.join('&') : '';
    if (location.hash !== hash || location.search) {
      try { history.replaceState(null, '', location.pathname + hash); } catch (err) { /* res */ }
    }
  }
  function llegeix(text) {
    var h = (text || '').replace(/^[#?]/, '');
    if (!h || h.indexOf('=') < 0) return false;
    var trobat = false;
    h.split('&').forEach(function (parell) {
      var kv = parell.split('='), k = kv[0], val = '';
      try { val = decodeURIComponent((kv[1] || '').replace(/\+/g, ' ')); } catch (err) { val = ''; }
      if (camps[k]) { camps[k].value = val; trobat = true; }
    });
    return trobat;
  }
  function esborra() {
    ['q', 'e', 't', 'p', 'm'].forEach(function (k) { if (camps[k]) camps[k].value = ''; });
    aplica();
    camps.q.focus();
  }

  camps.q.addEventListener('input', aplica);
  ['e', 't', 'p', 'm'].forEach(function (k) { camps[k].addEventListener('change', aplica); });
  document.getElementById('f-reset').addEventListener('click', esborra);
  document.getElementById('f-reset-2').addEventListener('click', esborra);
  taula.querySelectorAll('thead button[data-ordre]').forEach(function (b) {
    b.addEventListener('click', function () { ordena(b.getAttribute('data-ordre')); });
  });
  var deQ = llegeix(location.search);
  llegeix(location.hash);
  window.addEventListener('hashchange', function () {
    ['q', 'e', 't', 'p', 'm'].forEach(function (k) { camps[k].value = ''; });
    llegeix(location.hash); aplica();
  });
  aplica();
  if (deQ && camps.q.value) { camps.q.focus(); }
})();
