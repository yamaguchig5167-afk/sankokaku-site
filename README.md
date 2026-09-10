# 白樺湖レイクサイドホテル山幸閣 ｜ 団体・合宿サイト（ドラフト）

信州・白樺湖畔の旅館「白樺湖レイクサイドホテル山幸閣」の公式サイト改修案。
**合宿・団体・サプライズ演出**を軸に、旅行会社・学校・スポーツ/音楽団体・企業研修・ツーリング団体からの
**空室確認・見積り相談・電話問い合わせ**を増やすことを目的とした、素のHTML/CSS/JSによる静的サイト。

> ⚠️ 制作中のドラフトです。掲載中の「お客様の声」は代表例（サンプル）、料金は目安、一部写真はデザイン用のイメージです。
> 公開（本番）前の確認事項は **[CHECKLIST.md](CHECKLIST.md)** を参照してください。`robots.txt` で検索インデックスを抑止しています。

## ページ構成
| ファイル | 内容 |
|---|---|
| `index.html` | トップページ（ヒーローCTA・サプライズ演出・合宿4タイプ・実績・MaxHub/O2・施設・衛星マップ・客室・プラン・ギャラリー・アクセス） |
| `rooms.html` | 客室（4タイプ・スペック表） |
| `education.html` | 教育旅行・合宿 |
| `facilities.html` | 館内施設 |
| `maxhub.html` | ミーティングルーム（MaxHub 55型） |
| `contact.html` | **団体宿泊のご相談・お見積りフォーム** |
| `faq.html` | よくあるご質問 |
| `privacy.html` | プライバシーポリシー |
| `404.html` | 404ページ |

## 共通機能
- `assets/site.css` … モバイル固定CTA・フォーカス可視化・reduced-motion
- `assets/site.js` … ハンバーガーのa11y（aria/Escape）・計測フック（GA4未接続でdataLayerに積むだけ）
- 全ページ：canonical・OGP/Twitter Card・JSON-LD（LodgingBusiness／FAQ）

## 技術
- フレームワーク・ビルドツールなし（素のHTML/CSS/JS・GitHub Pages）
- フォント：Shippori Mincho / Cormorant Garamond / Noto Sans JP / Jost
- 画像は `assets/` にローカル保持（外部依存なし）

## 公開URL
https://yamaguchig5167-afk.github.io/sankokaku-site/

## ローカルプレビュー
```bash
python -m http.server 3020   # → http://localhost:3020
```

## 公開・設定手順
フォーム送信先（Formspree/GAS）・GA4・検索インデックス切替の手順は **[CHECKLIST.md](CHECKLIST.md)** に記載。
