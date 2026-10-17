# -*- coding: utf-8 -*-
"""github.io の旧アドレスを、新しいドメインへ転送するページ一式を docs/ に作る。

サイト本体を Vercel へ移したあと、配布済みのQRコードや案内文の github.io アドレスが
行き止まりにならないようにするためのもの。GitHub Pages の公開元を main ブランチの /docs に切り替えて使う。

  python tools/make-gh-redirect.py sankokaku-group.com

- 各ページ（*.html と旧サイト用の転送フォルダ）は、新ドメインの同じページへ転送
- それ以外のアドレス（PDF・画像など）は 404.html が新ドメインの同じ場所へ転送
"""
import pathlib
import shutil
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS = ROOT / 'docs'
PREFIX = '/sankokaku-site/'

PAGE = '''<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>新しいアドレスへ移転しました｜白樺湖レイクサイドホテル 山幸閣</title>
<link rel="canonical" href="{to}">
<meta http-equiv="refresh" content="0; url={to}">
<script>location.replace('{to}' + location.search + location.hash)</script>
<style>body{{font-family:system-ui,sans-serif;background:#F5F2EA;color:#1E2321;margin:0;padding:3rem 1.25rem;line-height:1.8}}a{{color:#183229}}</style>
</head>
<body>
<p>団体・合宿のご案内サイトは、新しいアドレスへ移転しました。<br><a href="{to}">{to}</a></p>
</body>
</html>
'''

NOT_FOUND = '''<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="robots" content="noindex">
<title>新しいアドレスへ移転しました｜白樺湖レイクサイドホテル 山幸閣</title>
<script>
(function(){{var p=location.pathname;var pre='{prefix}';
if(p.indexOf(pre)===0)p=p.slice(pre.length);else p=p.replace(/^\\//,'');
location.replace('{base}'+p+location.search+location.hash);}})();
</script>
</head>
<body><p>新しいアドレスへ移転しました。<a href="{base}">{base}</a></p></body>
</html>
'''


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    base = 'https://' + sys.argv[1].strip('/').lower() + '/'
    if DOCS.exists():
        shutil.rmtree(DOCS)
    DOCS.mkdir()
    (DOCS / '.nojekyll').write_text('', encoding='utf-8')
    n = 0
    for p in sorted(ROOT.glob('*.html')):
        if p.name == '404.html':
            continue
        to = base if p.name == 'index.html' else base + p.name
        (DOCS / p.name).write_text(PAGE.format(to=to), encoding='utf-8', newline='\n')
        n += 1
    for idx in sorted(ROOT.glob('*/**/index.html')):
        rel = idx.relative_to(ROOT)
        if rel.parts[0] in ('docs', 'tools', 'codex', 'assets', '.git', '.vercel'):
            continue
        out = DOCS / rel
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(PAGE.format(to=base + rel.parent.as_posix() + '/'), encoding='utf-8', newline='\n')
        n += 1
    (DOCS / '404.html').write_text(NOT_FOUND.format(prefix=PREFIX, base=base), encoding='utf-8', newline='\n')
    print(f'docs/ に転送ページ {n} 件と 404.html を作成 → {base}')


if __name__ == '__main__':
    main()
