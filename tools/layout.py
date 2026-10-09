# -*- coding: utf-8 -*-
"""
共通レイアウト（ヘッダー・メニュー・フッター・スマホ固定CTA）を全ページへ流し込む。

  python tools/layout.py

・<!-- LB:HEADER -->〜<!-- /LB:HEADER --> と <!-- LB:FOOTER -->〜<!-- /LB:FOOTER -->
  の間を毎回置き換えるので、何度実行しても同じ結果になる。
・初回は旧ヘッダー（topbar＋header）と旧フッターを見つけて置き換える。
・色・書体の読み込み（brand.css・Googleフォント）もここで揃える。
ナビやフッターのリンクを変えるときは、このファイルを直して再実行する。
"""
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
TEL = "0266-68-2021"

FONTS = ("https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;1,400"
         "&amp;family=Shippori+Mincho:wght@500;600&amp;family=DM+Sans:wght@400;500&amp;display=swap")

NAV = [
    ("travel-agent.html", "旅行会社の方", "AGENTS"),
    ("guide.html", "幹事・引率の方", "ORGANIZERS"),
    ("index.html#group", "目的別", "PLANS"),
    ("rooms.html", "客室・施設", "STAY"),
    ("access.html", "アクセス", "ACCESS"),
    ("downloads.html", "資料ダウンロード", "DOWNLOADS"),
]
PURPOSE = [
    ("education.html", "学校・教育旅行"),
    ("sports.html", "スポーツ合宿"),
    ("music.html", "音楽・吹奏楽"),
    ("training.html", "企業研修・ワーケーション"),
    ("ski.html", "スキー・スノーボード"),
    ("touring.html", "バイクツーリング"),
    ("memory.html", "白樺湖メモリアル花火"),
    ("experiences.html", "周辺の観光・体験"),
]
GUIDE = [
    ("downloads.html", "資料ダウンロード"),
    ("travel-agent.html", "旅行会社の方へ"),
    ("guide.html", "幹事・引率者ガイド"),
    ("rooms.html", "客室"),
    ("facilities.html", "館内施設"),
    ("maxhub.html", "MAXHUBのある会議室"),
    ("faq.html", "よくあるご質問"),
    ("index.html#before", "ご予約前のご確認"),
    ("arrival.html", "ご到着までのご案内"),
]


def header(current, solid):
    def cur(href):
        base = href.split("#")[0]
        return ' aria-current="page"' if base == current and "#" not in href else ""
    nav = "".join(f'<a href="{h}"{cur(h)}{" class=\"is-dl\"" if h == "downloads.html" else ""}>{t}</a>' for h, t, _ in NAV)
    main = "".join(f'<li><a href="{h}">{t}<small>{e}</small></a></li>' for h, t, e in NAV)
    purpose = "".join(f'<li><a href="{h}">{t}</a></li>' for h, t in PURPOSE)
    guide = "".join(f'<li><a href="{h}">{t}</a></li>' for h, t in GUIDE)
    cls = "lb-header is-solid" if solid else "lb-header"
    return f"""<!-- LB:HEADER -->
<a class="skip-link" href="#main">本文へスキップ</a>
<header class="{cls}" id="header">
  <div class="lb-header__inner">
    <a href="index.html" class="lb-brand"><span class="lb-brand__jp">山幸閣</span><span class="lb-brand__en">Shirakabako Lakeside Hotel</span></a>
    <nav class="lb-nav" aria-label="メインメニュー">{nav}</nav>
    <a href="contact.html" class="lb-btn lb-header__cta" data-ev="inquiry_cta_click">空室・見積り相談</a>
    <button type="button" class="lb-menu-btn" id="menuBtn" aria-expanded="false" aria-controls="menu"><span class="lb-menu-btn__bars" aria-hidden="true"></span><span>MENU</span></button>
  </div>
</header>
<div class="lb-menu" id="menu" role="dialog" aria-modal="true" aria-label="メニュー" tabindex="-1" hidden>
  <div class="lb-menu__top">
    <a href="index.html" class="lb-brand"><span class="lb-brand__jp">山幸閣</span><span class="lb-brand__en">Shirakabako Lakeside Hotel</span></a>
    <button type="button" class="lb-menu__close" data-menu-close><span aria-hidden="true">×</span>CLOSE</button>
  </div>
  <div class="lb-menu__body">
    <ul class="lb-menu__main">{main}</ul>
    <div class="lb-menu__group"><p>Find your stay</p><ul class="lb-menu__sub">{purpose}</ul></div>
    <div class="lb-menu__group"><p>Guide</p><ul class="lb-menu__sub">{guide}</ul></div>
    <div class="lb-menu__contact">
      <a class="lb-btn lb-btn--on-dark" href="contact.html" data-ev="inquiry_cta_click">空室・見積り相談</a>
      <a class="lb-menu__tel" href="tel:{TEL}" data-ev="tel_click">TEL {TEL}</a>
      <p class="lb-menu__hours">電話受付 9:00〜21:00</p>
    </div>
  </div>
</div>
<!-- /LB:HEADER -->"""


def footer():
    purpose = "".join(f'<li><a href="{h}">{t}</a></li>' for h, t in PURPOSE)
    guide = "".join(f'<li><a href="{h}">{t}</a></li>' for h, t in GUIDE)
    return f"""<!-- LB:FOOTER -->
<footer class="lb-footer">
  <div class="lb-container">
    <div class="lb-footer__grid">
      <div class="lb-footer__brand">
        <p class="lb-footer__concept">Sankokaku — Lake Base Shirakabako</p>
        <p class="lb-footer__name">白樺湖レイクサイドホテル<br>山幸閣</p>
        <address>〒391-0301 長野県茅野市北山3418-32<br>TEL <a href="tel:{TEL}" data-ev="tel_click">{TEL}</a>（受付 9:00〜21:00）<br>FAX 0266-68-2092</address>
      </div>
      <div class="lb-footer__col"><p class="lb-footer__h">Find your stay</p><ul>{purpose}</ul></div>
      <div class="lb-footer__col"><p class="lb-footer__h">Guide</p><ul>{guide}</ul></div>
      <div class="lb-footer__col"><p class="lb-footer__h">Contact</p><ul>
        <li><a href="contact.html" data-ev="inquiry_cta_click">空室・見積り相談</a></li>
        <li><a href="tel:{TEL}" data-ev="tel_click">電話で相談する</a></li>
        <li><a href="access.html">アクセス</a></li>
        <li><a href="privacy.html">プライバシーポリシー</a></li>
      </ul></div>
    </div>
    <div class="lb-footer__bottom"><small>© Shirakabako Lakeside Hotel Sankokaku.</small><em lang="en">Memories by the Lake.</em></div>
  </div>
</footer>
<div class="sticky-cta" aria-label="お問い合わせ"><a class="sc-dl" href="downloads.html" data-ev="downloads_click">資料</a><a class="sc-tel" href="tel:{TEL}" data-ev="tel_click">電話</a><a class="sc-form" href="contact.html" data-ev="inquiry_cta_click">空室・見積り相談</a></div>
<!-- /LB:FOOTER -->"""


COLOR_MAP = {
    "#2f5d57": "#183229", "#ad5424": "#7a6337", "#8f4418": "#5e4b28", "#b29a63": "#b69b67",
    "#1b2826": "#183229", "#141d1b": "#10231c", "#22312e": "#21423a", "#f6f3ec": "#f5f2ea",
    "#efe9dd": "#eeeae0", "#5f5b53": "#5a605c", "#7d6a3c": "#7a6337", "#d8743f": "#7a6337",
    "#4f827a": "#4a6358", "#33433f": "#2e3a36", "#2b2a26": "#1e2321",
    "rgba(173,84,36": "rgba(122,99,55", "rgba(246,243,236": "rgba(250,249,246",
}


def remap_colors(s):
    for a, b in COLOR_MAP.items():
        s = re.sub(re.escape(a), b, s, flags=re.I)
    return s


OLD_HEADER = re.compile(r'(?:<!--\s*ユーティリティバー\s*-->\s*)?(?:<div class="topbar">[\s\S]*?</div>\s*)?(?:<!--\s*ヘッダー\s*-->\s*)?<header[\s\S]*?</header>')
OLD_FOOTER = re.compile(r'(?:<!--\s*フッター\s*-->\s*)?<footer[\s\S]*?</footer>')
OLD_STICKY = re.compile(r'(?:<!--\s*モバイル固定CTA\s*-->\s*)?<div class="sticky-cta"[\s\S]*?</div>\s*')
OLD_SCRIPT = re.compile(r"<script>(?:(?!</script>)[\s\S])*getElementById\('ham'\)(?:(?!</script>)[\s\S])*</script>\s*")
FONT_LINK = re.compile(r'https://fonts\.googleapis\.com/css2\?family=[^"\']*?display=swap')


def process(path):
    name = path.name
    s = path.read_text(encoding="utf-8")
    o = s
    solid = 'class="hero' not in s
    is404 = name == "404.html"

    # 書体・色・読み込み
    s = FONT_LINK.sub(FONTS, s)
    s = s.replace('<link rel="stylesheet" href="assets/site.css">', "")
    if "assets/brand.css" not in s:
        s = s.replace("</head>", '<link rel="stylesheet" href="assets/brand.css">\n</head>', 1)
    if "classList.add('js')" not in s:
        s = s.replace("</head>", "<script>document.documentElement.classList.add('js')</script>\n</head>", 1)
    s = s.replace("%232f5d57", "%23183229").replace("%23b29a63", "%23b69b67").replace("rx='6'", "rx='3'")
    s = remap_colors(s)
    if '<meta name="theme-color"' not in s:
        s = s.replace("</head>", '<meta name="theme-color" content="#183229">\n</head>', 1)

    if not is404:
        # ヘッダー
        if "<!-- LB:HEADER -->" in s:
            s = re.sub(r"<!-- LB:HEADER -->[\s\S]*?<!-- /LB:HEADER -->", lambda m: header(name, solid), s)
        else:
            s = OLD_HEADER.sub(lambda m: header(name, solid), s, count=1)
        # フッター＋固定CTA
        s = OLD_STICKY.sub("", s)
        if "<!-- LB:FOOTER -->" in s:
            s = re.sub(r"<!-- LB:FOOTER -->[\s\S]*?<!-- /LB:FOOTER -->", lambda m: footer(), s)
        else:
            s = OLD_FOOTER.sub(lambda m: footer(), s, count=1)
        # 旧ヘッダー用のインラインJS（site.js に統合済み）
        s = OLD_SCRIPT.sub("", s)
        # <main id="main">
        if "<main" in s:
            s = re.sub(r"<main(?![^>]*\bid=)", '<main id="main"', s, count=1)
        else:
            s = s.replace("<!-- /LB:HEADER -->", '<!-- /LB:HEADER -->\n<main id="main">', 1)
            s = s.replace("<!-- LB:FOOTER -->", "</main>\n<!-- LB:FOOTER -->", 1)
        if solid and "has-solid-header" not in s:
            s = re.sub(r"<body(?![^>]*has-solid-header)([^>]*)>", r'<body class="has-solid-header"\1>', s, count=1)
        if 'src="assets/site.js"' not in s:
            s = s.replace("</body>", '<script src="assets/site.js" defer></script>\n</body>', 1)

    if s != o:
        path.write_text(s, encoding="utf-8")
        print("updated", name)


def main():
    for p in sorted(ROOT.glob("*.html")):
        process(p)
    for css in ["assets/pages.css"]:
        p = ROOT / css
        s = p.read_text(encoding="utf-8")
        t = remap_colors(s)
        if t != s:
            p.write_text(t, encoding="utf-8")
            print("updated", css)


if __name__ == "__main__":
    main()
