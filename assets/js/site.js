/* Michelle Yun · Index
   Character art, the Chicago clock, the phone menu, tabs, section highlighting,
   photo reveal, and the working prototype in case 04. No libraries. */
(() => {
  const RM = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const CHARS = ' .,:;-=+*#%@';
  const $ = (s, el = document) => el.querySelector(s);
  const $$ = (s, el = document) => [...el.querySelectorAll(s)];

  /* ---------- Character art engine ---------- */
  const fontReady = (document.fonts && document.fonts.load('12px "Geist Mono"').catch(() => {})) || Promise.resolve();

  function size(cv) {
    const r = cv.getBoundingClientRect();
    const d = Math.min(2, window.devicePixelRatio || 1);
    const w = Math.max(1, Math.round(r.width)), h = Math.max(1, Math.round(r.height));
    if (cv.width !== w * d || cv.height !== h * d) { cv.width = w * d; cv.height = h * d; }
    return { w, h, d };
  }

  // sampler(x, y, w, h) returns 0..1, where 1 is the densest character
  function draw(cv, sampler, { ink, bg, fs = 12 }) {
    const { w, h, d } = size(cv);
    const ctx = cv.getContext('2d');
    ctx.setTransform(d, 0, 0, d, 0, 0);
    ctx.fillStyle = bg; ctx.fillRect(0, 0, w, h);
    ctx.font = `${fs}px "Geist Mono", ui-monospace, monospace`;
    ctx.textBaseline = 'top';
    ctx.fillStyle = ink;
    const cw = ctx.measureText('0').width || fs * 0.6;
    const cols = Math.floor(w / cw), rows = Math.floor(h / fs);
    const ox = (w - cols * cw) / 2, oy = (h - rows * fs) / 2;
    const last = CHARS.length - 1;
    for (let y = 0; y < rows; y++) {
      let line = '';
      for (let x = 0; x < cols; x++) {
        const v = sampler(ox + (x + 0.5) * cw, oy + (y + 0.5) * fs, w, h);
        line += CHARS[Math.max(0, Math.min(last, Math.round(v * last)))];
      }
      ctx.fillText(line, ox, oy + y * fs);
    }
  }

  // Read pixels from something drawn at the canvas's size
  function maskSampler(w, h, paint, invert, stretch) {
    const off = document.createElement('canvas');
    off.width = w; off.height = h;
    const c = off.getContext('2d', { willReadFrequently: true });
    paint(c, w, h);
    let data;
    try { data = c.getImageData(0, 0, w, h).data; } catch (e) { return null; }
    const lum = (i) => (0.299 * data[i] + 0.587 * data[i + 1] + 0.114 * data[i + 2]) / 255;
    let lo = 0, hi = 1;
    if (stretch) {
      const xs = [];
      for (let i = 0; i < data.length; i += 4 * 37) xs.push(lum(i));
      xs.sort((a, b) => a - b);
      lo = xs[Math.floor(xs.length * 0.02)]; hi = xs[Math.floor(xs.length * 0.98)];
      if (hi - lo < 0.05) { lo = 0; hi = 1; }
    }
    return (x, y) => {
      const i = ((Math.min(h - 1, y | 0) * w) + Math.min(w - 1, x | 0)) * 4;
      const l = Math.max(0, Math.min(1, (lum(i) - lo) / (hi - lo)));
      return invert ? 1 - l : l;
    };
  }

  // The name, written in characters
  function nameArt(cv, text, ink, bg) {
    const { w, h } = size(cv);
    const s = maskSampler(w, h, (c) => {
      c.fillStyle = '#000'; c.fillRect(0, 0, w, h);
      c.fillStyle = '#fff'; c.textAlign = 'center'; c.textBaseline = 'middle';
      c.font = `600 400px Geist, system-ui, sans-serif`;
      const fit = (ls) => Math.min(400 * (w * 0.88) / Math.max(...ls.map((l) => c.measureText(l).width)), (h * 0.8) / (ls.length * 0.92));
      const one = [text], two = text.split(' ');
      const lines = fit(two) > fit(one) * 1.15 ? two : one;
      const fsz = fit(lines);
      c.font = `600 ${fsz}px Geist, system-ui, sans-serif`;
      c.strokeStyle = '#fff'; c.lineWidth = fsz * 0.03; c.lineJoin = 'round'; try { c.letterSpacing = (fsz * 0.05) + 'px'; } catch (e) {}
      lines.forEach((l, i) => {
        const y = h / 2 + (i - (lines.length - 1) / 2) * fsz * 0.92;
        c.fillText(l, w / 2, y); c.strokeText(l, w / 2, y);
      });
    });
    if (!s) return;
    draw(cv, (x, y) => {
      const v = s(x, y);
      return v > 0.5 ? (Math.sin(x * 0.21 + y * 0.13) > -0.2 ? 1 : 0.82) : (Math.sin(x * 0.031 + y * 0.047) * Math.sin(x * 0.017 - y * 0.023) > 0.8 ? 0.09 : 0);
    }, { ink, bg, fs: w < 500 ? 6 : 9 });
  }

  // One slow-moving pattern per case study
  const PATTERNS = [
    (u, v, t) => { const r = Math.hypot(u - .5, (v - .5) * .75); return (0.5 + 0.5 * Math.sin(r * 34 - t * 1.2)) * Math.max(0, 1.15 - r * 1.7); },
    (u, v, t) => { const a = Math.hypot(u - .3, v - .4), b = Math.hypot(u - .72, v - .62); return 0.5 + 0.25 * Math.sin(a * 40 - t) + 0.25 * Math.sin(b * 40 - t * 1.1); },
    (u, v, t) => { const band = [0.25, 0.5, 0.75].reduce((m, c, i) => Math.max(m, Math.exp(-Math.pow((v - c - 0.03 * Math.sin(u * 7 + t + i)) * 16, 2))), 0); return band * (0.65 + 0.35 * Math.sin(u * 30 - t * 2)); },
    (u, v, t) => 0.5 + 0.5 * Math.sin((u * 1.4 + v) * 18 - t * 1.4) * Math.cos((u - v) * 6 + t * 0.6),
    (u, v, t) => { const col = Math.floor(u * 9), hgt = 0.25 + 0.6 * (0.5 + 0.5 * Math.sin(col * 1.7 + t * 0.5)); const inside = (1 - v) < hgt && (u * 9 - col) > 0.18 && (u * 9 - col) < 0.82; return inside ? 0.75 + 0.2 * Math.sin(v * 40 + t) : 0.06; },
    (u, v, t) => { const a = Math.hypot(u - .18, v - .5), b = Math.hypot(u - .82, v - .5); return Math.max(0, Math.min(1, 0.5 + 0.35 * Math.sin(a * 30 - t * 1.3) * Math.max(0, 1 - a) + 0.35 * Math.sin(b * 30 - t * 1.3) * Math.max(0, 1 - b))); }
  ];
  function patternArt(cv, i, ink, bg, t) {
    const f = PATTERNS[i % PATTERNS.length];
    draw(cv, (x, y, w, h) => f(x / w, y / h, t), { ink, bg, fs: 12 });
  }

  // A photograph, written in characters (bright parts get dense characters)
  function photoArt(cv, img) {
    const { w, h } = size(cv);
    const s = maskSampler(w, h, (c) => c.drawImage(img, 0, 0, w, h), false, true);
    if (!s) { cv.closest('.frame')?.classList.add('noart'); return; }
    draw(cv, (x, y) => Math.pow(s(x, y), 1.1), { ink: '#ece9e1', bg: '#1d1c1a', fs: w < 500 ? 7 : 9 });
  }

  // Animate gently; stop when off screen or when the visitor prefers less motion
  function loop(fn) {
    let t = 0, last = 0, raf = 0, visible = true;
    const tick = (now) => {
      raf = requestAnimationFrame(tick);
      if (!visible || document.hidden || now - last < 110) return;
      last = now; t += 0.06; fn(t);
    };
    fn(0);
    if (!RM) raf = requestAnimationFrame(tick);
    return { setVisible: (v) => { visible = v; } };
  }

  const css = getComputedStyle(document.documentElement);
  const cvar = (n) => css.getPropertyValue(n).trim();

  /* ---------- Home: hover a case to preview it ---------- */
  function home() {
    const pane = $('#pane');
    if (!pane) return;
    const cv = $('canvas', pane);
    const rows = $$('.rows a[data-i]');
    const cap = $('#cap'), meta = $('#meta');
    let active = -1;
    const ink = () => active < 0 ? '#3a3936' : cvar(`--d0${active + 1}`);
    const bg = () => active < 0 ? cvar('--surf-2') : cvar(`--c0${active + 1}`);
    const anim = loop((t) => {
      if (active < 0) return;
      patternArt(cv, active, ink(), bg(), t);
    });
    const drawName = () => { if (active < 0) nameArt(cv, 'Michelle Yun', ink(), bg()); };

    function set(i) {
      if (i === active) return;
      active = i;
      const r = rows[i];
      pane.style.background = bg();
      cap.classList.add('out');
      setTimeout(() => {
        $('#cap-tag').textContent = r.dataset.tag;
        $('#cap-tag').style.setProperty('--c', bg());
        $('#cap-tag').hidden = false;
        $('#cap-title').textContent = r.dataset.title;
        $('#cap-line').textContent = r.dataset.line;
        $('#cap-link').href = r.getAttribute('href');
        $('#cap-link').textContent = 'Read case study →';
        meta.firstElementChild.textContent = `${r.dataset.n} / 06 · ${r.dataset.tag}`;
        cap.classList.remove('out');
      }, 180);
      rows.forEach((x, j) => x.classList.toggle('on', j === i));
      patternArt(cv, i, ink(), bg(), 0);
    }
    rows.forEach((r, i) => {
      r.addEventListener('mouseenter', () => set(i));
      r.addEventListener('focus', () => set(i));
    });
    fontReady.then(drawName);
    new ResizeObserver(() => { if (active < 0) drawName(); else patternArt(cv, active, ink(), bg(), 0); }).observe(pane);

    const mp = $('.mpanel canvas');
    if (mp) {
      const go = () => nameArt(mp, 'Michelle Yun', '#3a3936', cvar('--surf-2'));
      fontReady.then(go);
      new ResizeObserver(go).observe(mp);
    }
  }

  /* ---------- Bands at the top of About and the case studies ---------- */
  function bands() {
    $$('canvas[data-band]').forEach((cv) => {
      const i = +cv.dataset.band;
      const ink = i >= 0 ? cvar(`--d0${i + 1}`) : '#a19e96';
      const bg = i >= 0 ? cvar(`--c0${i + 1}`) : cvar('--surf-2');
      const idx = i >= 0 ? i : 3;
      let t0 = 0;
      const a = loop((t) => { t0 = t; patternArt(cv, idx, ink, bg, t); });
      new IntersectionObserver(([e]) => a.setVisible(e.isIntersecting)).observe(cv);
      new ResizeObserver(() => patternArt(cv, idx, ink, bg, t0)).observe(cv);
      fontReady.then(() => patternArt(cv, idx, ink, bg, t0));
    });
  }

  /* ---------- Photography ---------- */
  function frames() {
    const io = new IntersectionObserver((es) => es.forEach((e) => {
      if (!e.isIntersecting) return;
      io.unobserve(e.target);
      render(e.target);
    }), { rootMargin: '300px' });
    function render(fr) {
      const img = $('img', fr), cv = $('canvas', fr);
      const go = () => fontReady.then(() => photoArt(cv, img));
      if (img.complete && img.naturalWidth) go(); else img.addEventListener('load', go, { once: true });
    }
    $$('.frame').forEach((fr) => {
      fr.addEventListener('click', () => fr.classList.toggle('on'));
      fr.addEventListener('keydown', (e) => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); fr.classList.toggle('on'); } });
      if (fr.closest('.stack')) io.observe(fr);
    });

    const stage = $('#stage');
    if (!stage) return;
    const items = $$('.plist a[data-i]');
    const fr = $('.frame', stage), img = $('img', fr);
    let cur = 0;
    function show(i) {
      cur = (i + items.length) % items.length;
      const a = items[cur];
      items.forEach((x, j) => x.setAttribute('aria-current', j === cur ? 'true' : 'false'));
      fr.classList.remove('on', 'noart');
      fr.style.aspectRatio = a.dataset.ratio;
      img.src = a.dataset.src;
      img.alt = a.dataset.alt;
      $('#ph-n').textContent = `${String(cur + 1).padStart(2, '0')} / ${String(items.length).padStart(2, '0')}`;
      $('#ph-where').textContent = `${a.dataset.place} · ${a.dataset.lens}`;
      $('#ph-name').textContent = a.dataset.name;
      $('#ph-desc').textContent = a.dataset.alt;
      render(fr);
    }
    items.forEach((a, i) => a.addEventListener('click', (e) => { e.preventDefault(); show(i); }));
    $('#ph-prev').addEventListener('click', () => show(cur - 1));
    $('#ph-next').addEventListener('click', () => show(cur + 1));
    new ResizeObserver(() => render(fr)).observe(stage);
    show(0);
  }

  /* ---------- Chicago clock ---------- */
  function clock() {
    const els = $$('[data-clock]');
    if (!els.length) return;
    const f = new Intl.DateTimeFormat('en-US', { timeZone: 'America/Chicago', hour: 'numeric', minute: '2-digit' });
    const tick = () => els.forEach((el) => { el.textContent = `${f.format(new Date()).toLowerCase()} in Chicago`; });
    tick(); setInterval(tick, 20000);
  }

  /* ---------- Phone menu and sticky bar ---------- */
  function menu() {
    const btn = $('.menu-btn'), m = $('#menu'), top = $('.top');
    if (btn && m) btn.addEventListener('click', () => {
      const open = m.classList.toggle('open');
      btn.setAttribute('aria-expanded', open);
      btn.textContent = open ? 'Close' : 'Menu';
    });
    if (m) $$('a', m).forEach((a) => a.addEventListener('click', () => { m.classList.remove('open'); btn.setAttribute('aria-expanded', 'false'); btn.textContent = 'Menu'; }));
    if (top) addEventListener('scroll', () => top.classList.toggle('sc', scrollY > 4), { passive: true });
  }

  /* ---------- Section highlighting in the side menu ---------- */
  function spy() {
    const links = $$('.side-nav a[href^="#"]');
    if (!links.length) return;
    const map = new Map(links.map((a) => [a.getAttribute('href').slice(1), a]));
    const io = new IntersectionObserver((es) => {
      es.forEach((e) => {
        if (!e.isIntersecting) return;
        links.forEach((a) => a.classList.remove('on'));
        map.get(e.target.id)?.classList.add('on');
      });
    }, { rootMargin: '-30% 0px -60% 0px' });
    links[0].classList.add('on');
    map.forEach((_, id) => { const s = document.getElementById(id); if (s) io.observe(s); });
  }

  /* ---------- Tabs ---------- */
  function tabs() {
    $$('.tabs').forEach((box) => {
      const tl = $$('[role="tab"]', box);
      const pick = (t, focus) => {
        tl.forEach((x) => {
          const on = x === t;
          x.setAttribute('aria-selected', on); x.tabIndex = on ? 0 : -1;
          document.getElementById(x.getAttribute('aria-controls')).hidden = !on;
        });
        if (focus) t.focus();
      };
      tl.forEach((t, i) => {
        t.addEventListener('click', () => pick(t));
        t.addEventListener('keydown', (e) => {
          const k = { ArrowRight: 1, ArrowLeft: -1 }[e.key];
          if (k) { e.preventDefault(); pick(tl[(i + k + tl.length) % tl.length], true); }
        });
      });
    });
  }

  /* ---------- Copy email ---------- */
  function copy() {
    $$('[data-copy]').forEach((b) => b.addEventListener('click', async () => {
      try { await navigator.clipboard.writeText(b.dataset.copy); b.textContent = 'Copied'; }
      catch (e) { b.textContent = 'Press ⌘C'; }
      setTimeout(() => { b.textContent = 'Copy'; }, 1800);
    }));
  }

  /* ---------- Intro: KJ runs while the page loads ---------- */
  function intro() {
    const el = $('#intro');
    if (!el) return;
    if (RM) { el.remove(); return; }
    document.documentElement.classList.add('lock');
    const n = $('#intro-n');
    const start = performance.now(), dur = 1700;
    let done = false;
    const end = () => {
      if (done) return; done = true;
      el.classList.add('out');
      document.documentElement.classList.remove('lock');
      setTimeout(() => el.remove(), 800);
    };
    const step = (now) => {
      const p = Math.min(1, (now - start) / dur);
      n.textContent = String(Math.round(p * 100)).padStart(3, '0');
      if (p < 1 && !done) requestAnimationFrame(step); else end();
    };
    requestAnimationFrame(step);
    $('#intro-skip').addEventListener('click', end);
  }

  /* ---------- Case 04: the working prototype ---------- */
  function demo() {
    const root = $('#demo');
    if (!root) return;
    // Synthetic data. 30-day campaign totals are fixed; channels and the last 7 days are derived from them.
    const camps = [
      { name: 'Spring awareness', imp: 1989765, v: 70.7, b: 96.2, i: 1.2, mix: [.46, .31, .23], wk: .228 },
      { name: 'Product launch', imp: 2495226, v: 71.3, b: 96.3, i: 1.2, mix: [.41, .37, .22], wk: .241 },
      { name: 'Retargeting', imp: 3071527, v: 73.0, b: 96.0, i: 1.2, mix: [.52, .18, .30], wk: .236 },
      { name: 'Holiday promo', imp: 3724416, v: 73.6, b: 96.2, i: 1.2, mix: [.39, .34, .27], wk: .252 }
    ];
    const ch = ['Display', 'Video', 'Mobile app'];
    const dv = [-2.1, 4.4, -2.6], db = [-0.5, 0.6, 0.1], di = [0.2, -0.3, 0.1];
    camps.forEach((c) => {
      c.ch30 = c.mix.map((m) => Math.round(c.imp * m));
      c.ch30[2] = c.imp - c.ch30[0] - c.ch30[1];
    });
    function cell(c, k, range) {
      const imp = range === 7 ? Math.round(c.ch30[k] * c.wk) : c.ch30[k];
      const adj = (arr) => arr[k] - c.mix.reduce((s, m, j) => s + m * arr[j], 0);
      const wkShift = range === 7 ? 0.3 : 0;
      return { imp, v: imp * (c.v + adj(dv) + wkShift) / 100, b: imp * (c.b + adj(db)) / 100, i: imp * (c.i + adj(di) - wkShift / 10) / 100 };
    }
    const fmt = (n) => Math.round(n).toLocaleString('en-US');
    const pct = (a, b) => b ? (a / b * 100).toFixed(1) + '%' : '–';
    const sel = { range: $('#f-range', root), chan: $('#f-chan', root), camp: $('#f-camp', root) };
    function run() {
      const range = +sel.range.value, chan = sel.chan.value, camp = sel.camp.value;
      const tot = { imp: 0, v: 0, b: 0, i: 0 };
      const body = [];
      camps.forEach((c) => {
        if (camp !== 'all' && camp !== c.name) return;
        const row = { imp: 0, v: 0, b: 0, i: 0 };
        ch.forEach((name, k) => {
          if (chan !== 'all' && chan !== name) return;
          const x = cell(c, k, range);
          for (const key in row) row[key] += x[key];
        });
        for (const key in tot) tot[key] += row[key];
        body.push(`<tr><td>${c.name}</td><td>${fmt(row.imp)}</td><td>${pct(row.v, row.imp)}</td><td>${pct(row.b, row.imp)}</td><td>${pct(row.i, row.imp)}</td></tr>`);
      });
      $('#k-imp', root).textContent = fmt(tot.imp);
      $('#k-v', root).textContent = pct(tot.v, tot.imp);
      $('#k-b', root).textContent = pct(tot.b, tot.imp);
      $('#k-i', root).textContent = pct(tot.i, tot.imp);
      $('#d-body', root).innerHTML = body.join('');
    }
    Object.values(sel).forEach((s) => s.addEventListener('change', run));
    run();
  }

  intro(); menu(); clock(); copy(); tabs(); spy(); home(); bands(); frames(); demo();
})();
