# 白樺湖レイクサイドホテル 山幸閣 ｜ SANKOKAKU — LAKE BASE SHIRAKABAKO

信州・白樺湖畔の「白樺湖レイクサイドホテル 山幸閣」の公式サイト改修案。
**団体・合宿専用**のご案内サイト。旅行会社の方と、幹事・引率の方が、施設情報と資料（パンフレット・チラシ）にすぐたどり着けることを目的にしている。
条件は先に見せる（セルフスタイルの宿・温泉ではない・大浴場は事前相談制）。否定の強い言葉は使わず、合わない方には事実を括弧で添える書き方にする。

> 料金は目安、一部写真は「イメージ」表示のデザイン用画像です。公開前の確認事項は **[CHECKLIST.md](CHECKLIST.md)** を参照。

## ページ構成
| ファイル | 内容 |
|---|---|
| `index.html` | トップ（団体・合宿専用：Hero → 入口（旅行会社／幹事）と資料 → About → 目的別 → 数字 → 客室と施設 → ご予約の前に → 立地 → 四季 → 花火 → 相談 → ご案内） |
| `downloads.html` | **資料ダウンロード**（総合パンフ・旅行会社様向け・チラシ6種・アレルギー確認書） |
| `arrival.html` | ご到着までのご案内（セルフスタイルの宿・持ち物・館内の決まり） |
| `memory.html` | 白樺湖メモリアル花火（団体向け・事前相談制） |
| `education.html` / `sports.html` / `music.html` / `training.html` / `touring.html` / `ski.html` | 目的別ページ |
| `rooms.html` / `facilities.html` / `maxhub.html` / `experiences.html` / `access.html` | 滞在・施設・周辺・アクセス |
| `travel-agent.html` / `guide.html` / `faq.html` | 旅行会社向け・幹事ガイド・よくあるご質問 |
| `contact.html` / `privacy.html` / `404.html` | 相談フォーム・プライバシーポリシー・404 |

## デザインシステム
- `assets/brand.css` … 全ページ共通。色（Forest `#183229`／Ivory `#F5F2EA`／Charcoal `#1E2321`／Brass `#B69B67`）、書体、余白、ボタン、ヘッダー、フルスクリーンメニュー、フッター、スマホ固定CTA、reduced-motion。旧ページの変数（`--teal` `--gold` `--ember` など）もここでブランド色へ置き換える
  - 真鍮色 `#B69B67` は細線と暗い背景上の文字だけに使う。明るい背景上の文字は `--brass-ink #7A6337`（コントラスト比5:1以上）
- `assets/pages.css` … 下層ページの部品（見出し、チェックリスト、行程表など）
- `assets/site.js` … ヘッダーの背景切替、メニュー（フォーカス管理・Escで閉じる）、スクロール表示、地図の遅延読み込み、計測フック（GA4未接続でdataLayerに積むだけ）

## 共通レイアウトの更新方法
ヘッダー・メニュー・フッター・固定CTAは `tools/layout.py` が全ページへ流し込む（`<!-- LB:HEADER -->` と `<!-- LB:FOOTER -->` の間を置き換え）。
ナビやフッターのリンクを変えるときは `tools/layout.py` を直して次を実行する。
```bash
python tools/layout.py
```

## 技術
- フレームワーク・ビルドなし（素のHTML/CSS/JS・GitHub Pages。`main` へ push すると自動公開）
- 書体：見出し Shippori Mincho／英字 Cormorant Garamond・DM Sans（Webフォント）、本文は端末標準の日本語ゴシック
- 画像は `assets/` に WebP で保持（主要写真は 800／960／1440px の srcset）

## 公開URL
https://sankokaku-group.com/

### 公開先と独自ドメイン（Vercel・sankokaku-group.com）
団体・合宿向けのこのサイトは、宿研の旧公式サイト（sankokaku.com・個人向け・2027年4月終了予定）とは別サイト。
他のお客様サイト（NEXEL GARAGE）と同じく **Vercel で配信し、ドメインも Vercel で購入**する構成にそろえる。

- Vercel プロジェクト：`sankokaku-group`（チーム yamaguchig5167-afks-projects）／仮アドレス https://sankokaku-group.vercel.app（検索除外）
- 更新の反映：`git push origin main` のあと `vercel deploy --prod --yes`（GitHub 連携なしの CLI デプロイ）
- 配信しないもの：`.vercelignore`（tools・codex・README 等）

切り替え手順
1. Vercel の画面で `sankokaku-group.com` を購入（自動更新ON）。**Vercel はエージェントによる代理購入を受け付けない**ので人の操作。
2. `python tools/go-live.py sankokaku-group.com` で確認 → `--apply` で一括公開
   （ドメインと www の紐付け・アドレス置換・github.io を新ドメインへ転送する docs/ 生成と Pages 公開元の切替・デプロイ・館内掲示とQRの作り直し・表示確認）
3. Search Console に新アドレスを登録（Googleアカウントでの操作）

github.io の旧アドレスは、切り替え後は docs/ の転送ページで新ドメインへ案内する（配布済みQR対策）。
旧サイトのアドレスからの転送ページ（tools/old-redirects.py）は、将来 sankokaku.com をこのサイトへ向けた場合に働く。その際、フッターとトップの「個人は公式サイトへ」のリンクは見直す。

## ローカルプレビュー
```bash
python -m http.server 3020
```
→ http://localhost:3020

## 公開・設定手順
フォーム送信先（GAS）・GA4・Search Console の手順は **[CHECKLIST.md](CHECKLIST.md)** に記載。
