/* Comú a totes les pàgines: mode clar/fosc, cercador amb suggeriments (combobox)
   i botons de copiar. Generat per dashboard/genera_dashboard.py. Sense dependències. */
(function () {
  'use strict';
  var doc = document.documentElement;

  /* ---------- Mode clar / fosc ---------- */
  var SOL = '<svg viewBox="0 0 20 20" focusable="false"><circle cx="10" cy="10" r="3.6" fill="none" stroke="currentColor" stroke-width="1.7"/><path d="M10 2v2.2M10 15.8V18M2 10h2.2M15.8 10H18M4.3 4.3l1.6 1.6M14.1 14.1l1.6 1.6M4.3 15.7l1.6-1.6M14.1 5.9l1.6-1.6" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>';
  var LLUNA = '<svg viewBox="0 0 20 20" focusable="false"><path d="M15.5 12.6A6.5 6.5 0 0 1 7.4 4.5a6.5 6.5 0 1 0 8.1 8.1z" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>';
  var botoTema = document.querySelector('.tema');
  var mq = window.matchMedia ? window.matchMedia('(prefers-color-scheme: dark)') : null;
  function esFosc() {
    var t = doc.getAttribute('data-theme');
    return t ? t === 'dark' : !!(mq && mq.matches);
  }
  function pintaTema() {
    if (!botoTema) return;
    var f = esFosc();
    botoTema.setAttribute('aria-pressed', f ? 'true' : 'false');
    botoTema.title = f ? 'Passa al mode clar' : 'Passa al mode fosc';
    botoTema.querySelector('.tema-i').innerHTML = f ? SOL : LLUNA;
  }
  if (botoTema) {
    botoTema.addEventListener('click', function () {
      var nou = esFosc() ? 'light' : 'dark';
      doc.setAttribute('data-theme', nou);
      try { localStorage.setItem('fc-tema', nou); } catch (e) { /* sense emmagatzematge: només aquesta pàgina */ }
      pintaTema();
    });
    if (mq) {
      if (mq.addEventListener) mq.addEventListener('change', pintaTema);
      else if (mq.addListener) mq.addListener(pintaTema);
    }
    pintaTema();
  }

  /* ---------- Cercador amb suggeriments ---------- */
  function norm(s) {
    return (s || '').normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase().replace(/\s+/g, ' ').trim();
  }
  function esc(s) {
    return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; });
  }
  var NOM_ETQ = { F: 'F', P: 'P', D: 'ND', N: 'NA' };
  var IDX = null, carregant = false, esperen = [];
  function prepara(llista) {
    return llista.map(function (r) {
      var ceos = r[3] ? r[3].split('|') : [];
      var darrer = 0;
      for (var i = 0; i < 10; i++) { if (r[5].substr(2 * i, 2) !== '--') darrer = 2016 + i; }
      return { isin: r[0], nom: r[1], nomN: norm(r[1]), ceos: ceos, ultim: (r[4] || '').split('|').join(' · '), serie: r[5], darrer: darrer,
               tot: norm(r[1]) + ' ' + r[2] + ' ' + r[0].toLowerCase() + ' ' + norm(ceos.join(' ')) };
    });
  }
  function ambIndex(prefix, fet) {
    if (IDX) { fet(); return; }
    if (window.CERCA_IDX) { IDX = prepara(window.CERCA_IDX); fet(); return; }
    esperen.push(fet);
    if (carregant) return;
    carregant = true;
    var s = document.createElement('script');
    s.src = prefix + 'assets/index_cerca.js';
    s.onload = function () { IDX = prepara(window.CERCA_IDX || []); var f = esperen; esperen = []; f.forEach(function (x) { x(); }); };
    s.onerror = function () { carregant = false; esperen = []; };
    document.head.appendChild(s);
  }
  function busca(q) {
    var qn = norm(q), termes = qn.split(' ').filter(Boolean);
    if (!termes.length || !IDX) return [];
    var r = [];
    IDX.forEach(function (e) {
      for (var j = 0; j < termes.length; j++) { if (e.tot.indexOf(termes[j]) < 0) return; }
      var p = e.nomN.indexOf(qn) === 0 ? 0 : (' ' + e.nomN).indexOf(' ' + qn) >= 0 ? 1 : e.nomN.indexOf(qn) >= 0 ? 2 :
        e.isin.toLowerCase().indexOf(qn) === 0 ? 3 : 4;
      r.push([p, e]);
    });
    r.sort(function (a, b) { return a[0] - b[0] || (a[1].nomN < b[1].nomN ? -1 : a[1].nomN > b[1].nomN ? 1 : 0); });
    return r.slice(0, 7).map(function (x) { return x[1]; });
  }
  function resalta(text, termes) {
    var n = norm(text), marques = [];
    if (n.length !== text.length) return esc(text);
    termes.forEach(function (t) { var i = n.indexOf(t); if (i >= 0) marques.push([i, i + t.length]); });
    marques.sort(function (a, b) { return a[0] - b[0]; });
    var out = '', pos = 0;
    marques.forEach(function (m) {
      if (m[0] < pos) return;
      out += esc(text.slice(pos, m[0])) + '<mark>' + esc(text.slice(m[0], m[1])) + '</mark>';
      pos = m[1];
    });
    return out + esc(text.slice(pos));
  }
  function serie(e) {
    var h = '<span class="sr" aria-hidden="true">';
    for (var i = 0; i < 10; i++) {
      var c = e.serie.substr(2 * i, 2);
      h += c === '--' ? '<i></i>' : '<i class="' + NOM_ETQ[c[0]] + ' ' + c[1] + '">' + NOM_ETQ[c[0]] + '</i>';
    }
    return h + '</span>';
  }

  Array.prototype.forEach.call(document.querySelectorAll('[data-combobox]'), function (form, nForm) {
    var input = form.querySelector('input');
    var llista = form.querySelector('[role="listbox"]');
    var viu = form.querySelector('.cb-viu');
    var local = form.hasAttribute('data-local');
    var prefix = form.getAttribute('data-prefix') || '';
    var pop = document.createElement('div');
    pop.className = 'cb-pop';
    pop.hidden = true;
    llista.parentNode.insertBefore(pop, llista);
    pop.appendChild(llista);
    llista.hidden = false;
    var peu = document.createElement('p');
    peu.className = 'cb-peu';
    pop.appendChild(peu);
    var opcions = [], actiu = -1;

    function tanca() {
      pop.hidden = true;
      input.setAttribute('aria-expanded', 'false');
      input.removeAttribute('aria-activedescendant');
      actiu = -1;
    }
    function mou(i) {
      opcions.forEach(function (o, k) { o.setAttribute('aria-selected', k === i ? 'true' : 'false'); });
      actiu = i;
      if (i >= 0) {
        input.setAttribute('aria-activedescendant', opcions[i].id);
        if (opcions[i].scrollIntoView) opcions[i].scrollIntoView({ block: 'nearest' });
      } else {
        input.removeAttribute('aria-activedescendant');
      }
    }
    function pinta() {
      var q = input.value.trim();
      if (!q) { tanca(); if (viu) viu.textContent = ''; return; }
      ambIndex(prefix, function () {
        if (input.value.trim() !== q) return;
        var termes = norm(q).split(' ').filter(Boolean);
        var r = busca(q), h = '';
        r.forEach(function (e, k) {
          var ceosQ = e.ceos.filter(function (c) { var n = norm(c); return termes.some(function (t) { return t.length > 1 && n.indexOf(t) >= 0; }); });
          var sub = '<code>' + resalta(e.isin, termes) + '</code> · ' +
            (ceosQ.length ? 'CEO: ' + ceosQ.map(function (c) { return resalta(c, termes); }).join(', ')
              : 'CEO ' + e.darrer + ': ' + esc(e.ultim || 'sense CEO'));
          h += '<li role="option" class="sug" id="' + llista.id + '-o' + k + '" aria-selected="false" data-href="' + prefix + 'empreses/' + e.isin + '.html">' +
            '<span class="sug-nom">' + resalta(e.nom, termes) + '</span>' + serie(e) + '<span class="sug-sub">' + sub + '</span></li>';
        });
        llista.innerHTML = h;
        llista.hidden = !r.length;
        peu.innerHTML = (r.length ? '' : '<span class="cb-buit">Cap empresa no coincideix. Prova amb part del nom, l\'ISIN o el cognom del CEO.</span>') +
          (local ? '' : '<a href="' + prefix + 'empreses.html?q=' + encodeURIComponent(q) + '">Veure tots els resultats a Empreses <span aria-hidden="true">→</span></a>');
        peu.hidden = !peu.innerHTML;
        opcions = Array.prototype.slice.call(llista.querySelectorAll('.sug'));
        opcions.forEach(function (o, k) {
          o.addEventListener('mousedown', function (ev) { ev.preventDefault(); location.href = o.getAttribute('data-href'); });
          o.addEventListener('mousemove', function () { if (actiu !== k) mou(k); });
        });
        actiu = -1;
        input.removeAttribute('aria-activedescendant');
        pop.hidden = false;
        input.setAttribute('aria-expanded', 'true');
        if (viu) viu.textContent = r.length ? (r.length === 1 ? '1 suggeriment' : r.length + ' suggeriments') + '. Fes servir les fletxes per triar-ne un.' : 'Cap suggeriment.';
      });
    }
    input.addEventListener('input', pinta);
    input.addEventListener('focus', function () { ambIndex(prefix, function () {}); if (input.value.trim() && input.getAttribute('aria-expanded') !== 'true' && !local) pinta(); });
    input.addEventListener('blur', function () { setTimeout(tanca, 150); });
    input.addEventListener('keydown', function (ev) {
      if (ev.key === 'ArrowDown' || ev.key === 'ArrowUp') {
        ev.preventDefault();
        if (pop.hidden) { pinta(); return; }
        if (!opcions.length) return;
        if (ev.key === 'ArrowDown') mou(actiu + 1 >= opcions.length ? 0 : actiu + 1);
        else mou(actiu <= 0 ? opcions.length - 1 : actiu - 1);
      } else if (ev.key === 'Escape') {
        if (!pop.hidden) { ev.preventDefault(); tanca(); }
      } else if (ev.key === 'Enter') {
        if (!pop.hidden && actiu >= 0) { ev.preventDefault(); location.href = opcions[actiu].getAttribute('data-href'); }
        else if (local) { ev.preventDefault(); tanca(); }
      } else if (ev.key === 'Tab') {
        tanca();
      }
    });
  });

  /* Drecera «/»: porta al cercador (a Empreses, al de la llista). */
  document.addEventListener('keydown', function (ev) {
    if (ev.key !== '/' || ev.ctrlKey || ev.metaKey || ev.altKey) return;
    var a = document.activeElement;
    if (a && (/^(input|textarea|select)$/i.test(a.tagName) || a.isContentEditable)) return;
    var camps = Array.prototype.slice.call(document.querySelectorAll('[data-combobox][data-local] input'))
      .concat(Array.prototype.slice.call(document.querySelectorAll('[data-combobox]:not([data-local]) input')));
    for (var i = 0; i < camps.length; i++) {
      if (camps[i].offsetParent !== null) { ev.preventDefault(); camps[i].focus(); return; }
    }
  });

  /* ---------- Botons de copiar ---------- */
  var viuCopia = document.createElement('div');
  viuCopia.className = 'vh';
  viuCopia.setAttribute('aria-live', 'polite');
  document.body.appendChild(viuCopia);
  function copiaAntic(text) {
    var t = document.createElement('textarea');
    t.value = text;
    t.setAttribute('readonly', '');
    t.style.position = 'fixed';
    t.style.opacity = '0';
    document.body.appendChild(t);
    t.select();
    var ok = false;
    try { ok = document.execCommand('copy'); } catch (e) { ok = false; }
    document.body.removeChild(t);
    return ok;
  }
  function copia(text, boto, que) {
    var original = boto.getAttribute('data-original') || boto.textContent;
    boto.setAttribute('data-original', original);
    function fet(ok) {
      boto.textContent = ok ? 'Copiat ✓' : 'No s\'ha pogut copiar';
      viuCopia.textContent = ok ? que + ' copiat al porta-retalls.' : 'No s\'ha pogut copiar.';
      setTimeout(function () { boto.textContent = original; }, 1600);
    }
    if (navigator.clipboard && window.isSecureContext) {
      navigator.clipboard.writeText(text).then(function () { fet(true); }, function () { fet(copiaAntic(text)); });
    } else {
      fet(copiaAntic(text));
    }
  }
  document.addEventListener('click', function (ev) {
    var b = ev.target.closest ? ev.target.closest('[data-copia], [data-copia-cita]') : null;
    if (!b) return;
    if (b.hasAttribute('data-copia')) { copia(b.getAttribute('data-copia'), b, 'Text'); return; }
    var bloc = b.closest('.ev-ext') || b.closest('.ev');
    var p = bloc ? bloc.querySelector('.cita p') : null;
    if (p) copia(p.textContent.replace(/\s*\[…\]$/, ''), b, 'Cita');
  });
})();
