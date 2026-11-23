/* Cercador i filtres de l'inici. Generat per dashboard/genera_dashboard.py. Sense dependències. */
(function () {
  'use strict';
  var taula = document.getElementById('taula');
  if (!taula) return;
  var tbody = taula.tBodies[0];
  var files = Array.prototype.slice.call(tbody.rows);
  var camps = {
    q: document.getElementById('f-cerca'),
    e: document.getElementById('f-etiq'),
    c: document.getElementById('f-cert'),
    p: document.getElementById('f-pais'),
    s: document.getElementById('f-sector'),
    v: document.getElementById('f-proves')
  };
  var nVis = document.getElementById('n-visibles');
  var cap = document.getElementById('cap-resultat');
  var ordre = { clau: 'nom', dir: 1 };

  function norm(s) {
    return (s || '').normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase().replace(/\s+/g, ' ').trim();
  }
  function fmt(n) { return String(n).replace(/\B(?=(\d{3})+(?!\d))/g, '.'); }
  function conte(llista, valor) { return (' ' + (llista || '') + ' ').indexOf(' ' + valor + ' ') >= 0; }

  function aplica() {
    var termes = norm(camps.q.value).split(' ').filter(Boolean);
    var e = camps.e.value, c = camps.c.value, p = camps.p.value, v = camps.v.value;
    var s = camps.s ? camps.s.value : '';
    var n = 0;
    for (var i = 0; i < files.length; i++) {
      var tr = files[i], d = tr.dataset, ok = true;
      for (var j = 0; j < termes.length && ok; j++) { if (d.cerca.indexOf(termes[j]) < 0) ok = false; }
      if (ok && e && !conte(d.etiq, e)) ok = false;
      if (ok && c && !conte(d.cert, c)) ok = false;
      if (ok && p && d.pais !== p) ok = false;
      if (ok && v && d.proves !== v) ok = false;
      if (ok && s && d.sector !== s) ok = false;
      tr.hidden = !ok;
      if (ok) n++;
    }
    nVis.textContent = fmt(n);
    cap.hidden = n > 0;
    desa();
  }

  function ordena(clau) {
    if (ordre.clau === clau) { ordre.dir = -ordre.dir; } else { ordre.clau = clau; ordre.dir = (clau === 'nom' || clau === 'isin') ? 1 : -1; }
    var num = !(clau === 'nom' || clau === 'isin');
    files.sort(function (a, b) {
      var x = a.dataset[clau], y = b.dataset[clau], r;
      if (num) { r = (+x) - (+y); } else { r = x < y ? -1 : x > y ? 1 : 0; }
      if (r === 0) { r = a.dataset.nom < b.dataset.nom ? -1 : a.dataset.nom > b.dataset.nom ? 1 : 0; return r; }
      return r * ordre.dir;
    });
    var frag = document.createDocumentFragment();
    files.forEach(function (tr) { frag.appendChild(tr); });
    tbody.appendChild(frag);
    taula.querySelectorAll('thead button[data-ordre]').forEach(function (b) {
      if (b.getAttribute('data-ordre') === ordre.clau) { b.setAttribute('aria-sort', ordre.dir > 0 ? 'ascending' : 'descending'); }
      else { b.removeAttribute('aria-sort'); }
    });
  }

  function desa() {
    var params = [];
    ['q', 'e', 'c', 'p', 's', 'v'].forEach(function (k) {
      if (camps[k] && camps[k].value) params.push(k + '=' + encodeURIComponent(camps[k].value));
    });
    var hash = params.length ? '#' + params.join('&') : '';
    if (location.hash !== hash) {
      try { history.replaceState(null, '', hash || location.pathname + location.search); } catch (err) { /* res */ }
    }
  }
  function llegeix() {
    var h = location.hash.replace(/^#/, '');
    if (!h || h.indexOf('=') < 0) return;
    h.split('&').forEach(function (parell) {
      var kv = parell.split('='), k = kv[0], val = decodeURIComponent(kv[1] || '');
      if (camps[k]) camps[k].value = val;
    });
  }

  camps.q.addEventListener('input', aplica);
  ['e', 'c', 'p', 's', 'v'].forEach(function (k) { if (camps[k]) camps[k].addEventListener('change', aplica); });
  document.getElementById('f-reset').addEventListener('click', function () {
    ['q', 'e', 'c', 'p', 's', 'v'].forEach(function (k) { if (camps[k]) camps[k].value = ''; });
    aplica();
    camps.q.focus();
  });
  taula.querySelectorAll('thead button[data-ordre]').forEach(function (b) {
    b.addEventListener('click', function () { ordena(b.getAttribute('data-ordre')); });
  });
  llegeix();
  aplica();
})();
