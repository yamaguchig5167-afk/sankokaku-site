# -*- coding: utf-8 -*-
"""独自ドメインでの公開を、DNS確認から https 有効化・資料のQR作り直しまで一度に行う。

使い方:
  python tools/go-live.py group.sankokaku.com           # 確認だけ（何も変えない）
  python tools/go-live.py group.sankokaku.com --apply   # 実行

流れ:
  1. DNS が GitHub Pages を向いているか確認（向いていなければ中止）
  2. サイト内のアドレス表記を置き換え、CNAME を作って公開（switch-domain.py）
  3. GitHub の Pages 設定にドメインを登録し、証明書の発行を待って https を強制
  4. 館内掲示・旅行会社向けQR・案内文面のアドレスを置き換えて作り直す
  5. 新アドレスと旧アドレス（github.io からの転送）を実際に開いて確認
"""
import json
import pathlib
import socket
import subprocess
import sys
import time
import urllib.request

REPO = 'yamaguchig5167-afk/sankokaku-site'
OLD = 'https://yamaguchig5167-afk.github.io/sankokaku-site/'
PAGES_IPS = {'185.199.108.153', '185.199.109.153', '185.199.110.153', '185.199.111.153'}
ROOT = pathlib.Path(__file__).resolve().parent.parent
CASES = pathlib.Path(r'C:\Users\gyama\OneDrive\Desktop\①Claude Code\案件')
# サイトの外にある、アドレスを書き込んでいる資料（置き換えたあと、括弧内のコマンドで作り直す）
EXTERNAL = [
    (CASES / '山幸閣_旅行会社向け営業' / 'make-qr.cjs', ['node', 'make-qr.cjs']),
    (CASES / '山幸閣_館内掲示' / 'render.cjs', ['node', 'render.cjs']),
    (CASES / '山幸閣_旅行会社向け営業' / '旅行会社への案内_文面と使い方_内部メモ.md', None),
]


def run(cmd, cwd=ROOT):
    print('  $ ' + ' '.join(cmd))
    return subprocess.run(cmd, cwd=cwd, check=True, capture_output=True, text=True, encoding='utf-8').stdout


def gh_pages():
    return json.loads(run(['gh', 'api', f'repos/{REPO}/pages']))


def http_ok(url):
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

    print('1. DNS の確認')
    try:
        ips = {i[4][0] for i in socket.getaddrinfo(host, 443, socket.AF_INET)}
    except socket.gaierror:
        sys.exit(f'  {host} はまだ DNS に登録されていません。設定と反映を待ってから実行してください。')
    print('  ' + ', '.join(sorted(ips)))
    if not ips <= PAGES_IPS:
        sys.exit('  GitHub Pages 以外を向いています。DNS の値（CNAME → yamaguchig5167-afk.github.io.）を確認してください。')
    print('  OK：GitHub Pages を向いています')
    if not apply:
        print('（確認のみ。実行するには --apply を付ける）')
        return

    print('2. サイト内のアドレスを置き換えて公開')
    subprocess.run([sys.executable, str(ROOT / 'tools' / 'switch-domain.py'), host, '--apply'], cwd=ROOT, check=True)
    run(['git', 'add', '-A'])
    run(['git', 'commit', '-m', f'独自ドメイン {host} で公開\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>'])
    run(['git', 'push', 'origin', 'main'])

    print('3. GitHub の Pages 設定と https')
    run(['gh', 'api', '-X', 'PUT', f'repos/{REPO}/pages', '-f', f'cname={host}'])
    for i in range(60):  # 証明書の発行は通常数分〜1時間
        st = (gh_pages().get('https_certificate') or {}).get('state')
        print(f'  証明書：{st}')
        if st == 'approved':
            run(['gh', 'api', '-X', 'PUT', f'repos/{REPO}/pages', '-F', 'https_enforced=true'])
            print('  https を強制しました')
            break
        time.sleep(60)
    else:
        print('  証明書がまだ発行されていません。後で「gh api -X PUT repos/%s/pages -F https_enforced=true」を実行してください。' % REPO)
    run(['git', 'pull', '-q', 'origin', 'main'])

    print('4. 資料のアドレスを置き換えて作り直す')
    for path, cmd in EXTERNAL:
        s = path.read_text(encoding='utf-8')
        if OLD in s:
            path.write_text(s.replace(OLD, new), encoding='utf-8')
            print(f'  {path.name}：置き換え')
        if cmd:
            run(cmd, cwd=path.parent)

    print('5. 表示の確認')
    for url in (new, new + 'downloads.html', new + 'arrival.html', OLD + 'downloads.html'):
        print(f'  {url} → {http_ok(url)}')


if __name__ == '__main__':
    main()
