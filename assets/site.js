/* 山幸閣サイト 共通スクリプト（ヘッダー・メニュー・スクロール表示・計測フック）
   GA4は未接続。計測は dataLayer に積むだけで、個人情報・入力値は送らない。 */
(function () {
  var root = document.documentElement;
  root.classList.add('js');

  // ヘッダー：ヒーローの上では透明、スクロールしたら背景を付ける
  var header = document.getElementById('header');
  if (header) {
    var onScroll = function () { header.classList.toggle('is-scrolled', window.scrollY > 40); };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  // フルスクリーンメニュー
  var menu = document.getElementById('menu');
  var openBtn = document.getElementById('menuBtn');
  if (menu && openBtn) {
    var closeBtn = menu.querySelector('[data-menu-close]');
    var lastFocus = null;
    var setOpen = function (open) {
      menu.hidden = !open;
      if (open) lastFocus = document.activeElement;
      void menu.offsetWidth; // hidden を外した状態を確定させてから遷移させる
      menu.classList.toggle('is-open', open);
      if (open) (closeBtn || menu).focus();
      root.classList.toggle('menu-open', open);
      openBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
      if (!open && lastFocus) lastFocus.focus();
    };
    openBtn.addEventListener('click', function () { setOpen(true); });
    if (closeBtn) closeBtn.addEventListener('click', function () { setOpen(false); });
    menu.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () { setOpen(false); });
    });
    document.addEventListener('keydown', function (e) {
      if (menu.hidden) return;
      if (e.key === 'Escape') { setOpen(false); return; }
      if (e.key === 'Tab') { // メニュー内でフォーカスを循環させる
        var f = menu.querySelectorAll('a[href],button:not([disabled])');
        if (!f.length) return;
        var first = f[0], last = f[f.length - 1];
        if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
        else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
      }
    });
    window.addEventListener('resize', function () {
      if (window.innerWidth > 1280 && !menu.hidden) setOpen(false);
    });
  }

  // スクロールで静かに表示
  var items = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
      });
    }, { threshold: 0.08, rootMargin: '0px 0px -40px 0px' });
    items.forEach(function (el) { io.observe(el); });
  } else {
    items.forEach(function (el) { el.classList.add('in'); });
  }

  // 地図は押したときだけ読み込む（表示速度と、Googleへの通信を最小にするため）
  document.querySelectorAll('.map-facade').forEach(function (b) {
    b.addEventListener('click', function () {
      var f = document.createElement('iframe');
      f.src = b.dataset.src; f.title = b.dataset.title || '地図'; f.loading = 'lazy';
      f.referrerPolicy = 'no-referrer-when-downgrade'; f.allowFullscreen = true;
      b.replaceWith(f);
    });
  });

  // 横スクロールの写真列：前後ボタン
  document.querySelectorAll('[data-rail]').forEach(function (wrap) {
    var rail = wrap.querySelector('.rail');
    var prev = wrap.querySelector('[data-rail-prev]');
    var next = wrap.querySelector('[data-rail-next]');
    if (!rail) return;
    var step = function (dir) {
      var card = rail.firstElementChild;
      var w = card ? card.getBoundingClientRect().width + 24 : rail.clientWidth * 0.8;
      rail.scrollBy({ left: dir * w, behavior: 'smooth' });
    };
    if (prev) prev.addEventListener('click', function () { step(-1); });
    if (next) next.addEventListener('click', function () { step(1); });
  });

  // 計測フック（GA4未接続：dataLayerに積むだけ）
  window.dataLayer = window.dataLayer || [];
  document.addEventListener('click', function (e) {
    var el = e.target.closest && e.target.closest('[data-ev]');
    if (el) { window.dataLayer.push({ event: el.getAttribute('data-ev') }); }
  }, true);
})();
