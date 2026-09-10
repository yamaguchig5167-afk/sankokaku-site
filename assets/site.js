/* 山幸閣サイト 共通追加スクリプト（横断機能・GA4は未接続で計測フックのみ） */
(function () {
  // ハンバーガー a11y（既存のトグルは各ページのインラインJSが担当。ここではaria状態を同期）
  var ham = document.getElementById('ham');
  var nav = document.getElementById('nav');
  if (ham && nav) {
    ham.setAttribute('role', 'button');
    ham.setAttribute('tabindex', '0');
    ham.setAttribute('aria-controls', 'nav');
    ham.setAttribute('aria-label', 'メニューを開閉');
    ham.setAttribute('aria-expanded', 'false');
    var sync = function () { ham.setAttribute('aria-expanded', nav.classList.contains('open') ? 'true' : 'false'); };
    ham.addEventListener('click', function () { setTimeout(sync, 0); });
    ham.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); ham.click(); }
    });
    // Escapeでメニューを閉じる
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('open')) { nav.classList.remove('open'); sync(); ham.focus(); }
    });
  }

  // 計測フック（GA4未接続：dataLayerに積むだけ。個人情報・入力値は送らない）
  window.dataLayer = window.dataLayer || [];
  document.addEventListener('click', function (e) {
    var el = e.target.closest && e.target.closest('[data-ev]');
    if (el) { window.dataLayer.push({ event: el.getAttribute('data-ev') }); }
  }, true);
})();
