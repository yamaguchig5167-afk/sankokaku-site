# -*- coding: utf-8 -*-
"""独自ドメインでの公開（Vercel）を、ドメインの紐付けから資料のQR作り直しまで一度に行う。

前提：ドメインは Vercel のチーム（yamaguchig5167-afks-projects）で購入済み
      （Vercel は代理購入を受け付けないため、購入は人の操作）。

使い方:
  python tools/go-live.py sankokaku-group.com           # 確認だけ（何も変えない）
  python tools/go-live.py sankokaku-group.com --apply   # 実行

流れ:
  1. ドメインが Vercel のチームにあるか確認し、プロジェクト sankokaku-group に紐付け（www も）
  2. サイト内のアドレス表記（canonical・OGP・サイトマップ等）を新ドメインへ置き換え
  3. github.io の旧アドレスを新ドメインへ転送するページを docs/ に作り、GitHub Pages の公開元を /docs に切り替え
  4. GitHub へ push し、Vercel へ本番デプロイ
  5. 館内掲示・旅行会社向けQR・案内文面のアドレスを置き換えて作り直す
  6. 新アドレスと旧アドレス（github.io からの転送）を実際に開いて確認
"""
import pathlib
import subprocess
import sys
import time
import urllib.request

REPO = 'yamaguchig5167-afk/sankokaku-site'
PROJECT = 'sankokaku-group'
OLD = 'https://yamaguchig5167-afk.github.io/sankokaku-site/'
ROOT = pathlib.Path(__file__).resolve().parent.parent
CASES = pathlib.Path(r'C:\Users\gyama\OneDrive\Desktop\①Claude Code\案件')
# サイトの外にある、アドレスを書き込んでいる資料（置き換えたあと、括弧内のコマンドで作り直す）
EXTERNAL = [
    (CASES / '山幸閣_旅行会社向け営業' / 'make-qr.cjs', ['node', 'make-qr.cjs']),
    (CASES / '山幸閣_館内掲示' / 'render.cjs', ['node', 'render.cjs']),
    (CASES / '山幸閣_旅行会社向け営業' / '旅行会社への案内_文面と使い方_内部メモ.md', None),
]


def run(cmd, cwd=ROOT, check=True):
    print('  $ ' + ' '.join(cmd))
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, encoding='utf-8', shell=(cmd[0] == 'vercel'))
    out = (r.stdout or '') + (r.stderr or '')
    if check and r.returncode != 0:
        print(out)
        sys.exit(f'  失敗：{" ".join(cmd)}')
    return out


def fetch(url):
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=20) as r:
            return r.status, r.geturl()
    except Exception as e:  # noqa: BLE001
        return str(e), url


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    if len(args) != 1:
        sys.exit(__doc__)
    host = args[0].lower().strip('/')
    new = f'https://{host}/'
    apply = '--apply' in sys.argv

    print('1. ドメインの確認')
    info = run(['vercel', 'domains', 'inspect', host], check=False)
    if 'not found' in info.lower() or 'error' in info.lower():
        print(info.strip()[-400:])
        sys.exit(f'  {host} が Vercel のチームにありません。Vercel の画面で購入（または追加）してから実行してください。')
    print('  OK：Vercel のチームにあります')
    if not apply:
        print('（確認のみ。実行するには --apply を付ける）')
        return

    for d in (host, 'www.' + host):
        out = run(['vercel', 'domains', 'add', d, PROJECT], check=False)
        print('  ' + (out.strip().splitlines() or [''])[-1])

    print('2. サイト内のアドレスを置き換え')
    subprocess.run([sys.executable, str(ROOT / 'tools' / 'switch-domain.py'), host, '--apply', '--no-cname'], cwd=ROOT, check=True)

    print('3. github.io からの転送ページ')
    subprocess.run([sys.executable, str(ROOT / 'tools' / 'make-gh-redirect.py'), host], cwd=ROOT, check=True)

    print('4. GitHub へ push と Vercel へデプロイ')
    run(['git', 'add', '-A'])
    run(['git', 'commit', '-m', f'独自ドメイン {host}（Vercel）で公開し、github.io は新ドメインへ転送\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>'])
    run(['git', 'push', 'origin', 'main'])
    run(['gh', 'api', '-X', 'PUT', f'repos/{REPO}/pages', '-f', 'source[branch]=main', '-f', 'source[path]=/docs'])
    print(run(['vercel', 'deploy', '--prod', '--yes']).strip().splitlines()[-1])

    print('5. 資料のアドレスを置き換えて作り直す')
    for path, cmd in EXTERNAL:
        s = path.read_text(encoding='utf-8')
        if OLD in s:
            path.write_text(s.replace(OLD, new), encoding='utf-8')
            print(f'  {path.name}：置き換え')
        if cmd:
            run(cmd, cwd=path.parent)

    print('6. 表示の確認（GitHub Pages の切り替え反映を待つ）')
    time.sleep(90)
    for url in (new, new + 'downloads.html', new + 'arrival.html', 'https://www.' + host + '/', OLD + 'downloads.html', OLD + 'assets/docs/sankokaku-group-guide-20p.pdf'):
        print(f'  {url} → {fetch(url)}')
    print('github.io の行は「JS/meta で新ドメインへ移る」ため、ブラウザで開いて新アドレスに着くことも確認する。')


if __name__ == '__main__':
    main()
