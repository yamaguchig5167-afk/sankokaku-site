# -*- coding: utf-8 -*-
"""旧公式サイト（宿研・WordPress）のアドレスから、新サイトの同じ内容のページへ案内する転送ページを作る。

sankokaku.com を新サイトへ切り替えたあと、検索結果やブックマークから旧アドレスに来た人が
行き止まりにならないようにするためのもの。GitHub Pages はサーバー側の転送を設定できないので、
旧アドレスと同じ場所に小さな転送用HTMLを置く。

  python tools/old-redirects.py     # 何度実行してもよい（上書き）

一覧にない旧アドレス（記事・プラン・カテゴリー等）は 404.html がトップへ案内する。
"""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent

# 旧アドレス（先頭・末尾の / なし） → 新ページ
MAP = {
    'rooms': 'rooms.html',
    'access': 'access.html',
    'facility': 'facilities.html',
    'sights': 'experiences.html',
    'education': 'education.html',
    'faq': 'faq.html',
    'policy': 'privacy.html',
    'contact': 'contact.html',
    'contact/confirm': 'contact.html',
    'contact/complete': 'contact.html',
    'contact/error': 'contact.html',
    'contact/recaptcha-error': 'contact.html',
    'plan': 'index.html',
}

TPL = '''<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ページを移動しました｜白樺湖レイクサイドホテル 山幸閣</title>
<meta name="robots" content="noindex">
<link rel="canonical" href="{to}">
<meta http-equiv="refresh" content="0; url={to}">
<script>location.replace('{to}' + location.hash)</script>
<style>body{{font-family:system-ui,sans-serif;background:#F5F2EA;color:#1E2321;margin:0;padding:3rem 1.25rem;line-height:1.8}}a{{color:#183229}}</style>
</head>
<body>
<p>このページは移動しました。<br><a href="{to}">新しいページへ進む</a></p>
</body>
</html>
'''


def main():
    for old, new in MAP.items():
        depth = old.count('/') + 1
        to = '../' * depth + new
        d = ROOT / old
        d.mkdir(parents=True, exist_ok=True)
        (d / 'index.html').write_text(TPL.format(to=to), encoding='utf-8', newline='\n')
        print(f'/{old}/ → {new}')


if __name__ == '__main__':
    main()
