# -*- coding: utf-8 -*-
"""独自ドメインへの切り替え（サイト内のアドレス表記と CNAME をまとめて更新する）

使い方:
  python tools/switch-domain.py sankokaku.jp            # 変更予定の一覧だけ出す（書き込まない）
  python tools/switch-domain.py sankokaku.jp --apply    # 書き込む

先に DNS を設定し、名前が引けることを確かめてから --apply すること。
DNS より先に CNAME を公開すると、github.io のアドレスも見られなくなる。
"""
import pathlib
import socket
import sys

OLD = 'https://yamaguchig5167-afk.github.io/sankokaku-site/'
ROOT = pathlib.Path(__file__).resolve().parent.parent
TARGETS = ['*.html', 'sitemap.xml', 'robots.txt', 'README.md']


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    if len(args) != 1:
        sys.exit(__doc__)
    host = args[0].strip().lower().rstrip('/')
    if '://' in host or '/' in host:
        sys.exit('ドメイン名だけを指定してください（例：sankokaku.jp）')
    new = 'https://' + host + '/'
    apply = '--apply' in sys.argv

    try:
        socket.getaddrinfo(host, 443)
    except socket.gaierror:
        msg = f'{host} の名前がまだ引けません（DNS 未設定か反映待ち）'
        if apply:
            sys.exit(msg + '。中止しました。')
        print('注意：' + msg)

    total = 0
    for pattern in TARGETS:
        for p in sorted(ROOT.glob(pattern)):
            s = p.read_text(encoding='utf-8')
            n = s.count(OLD)
            if not n:
                continue
            total += n
            print(f'{p.name}: {n} か所')
            if apply:
                p.write_text(s.replace(OLD, new), encoding='utf-8')
    print(f'合計 {total} か所 → {new}')

    if apply:
        (ROOT / 'CNAME').write_text(host + '\n', encoding='utf-8')
        print('CNAME を作成しました。コミットして push したら、GitHub の Pages 設定で "Enforce HTTPS" を有効にしてください。')
    else:
        print('（確認のみ。書き込むには --apply を付けて実行）')


if __name__ == '__main__':
    main()
