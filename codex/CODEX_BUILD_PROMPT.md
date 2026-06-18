# 山幸閣 ホームページ ビルド指示（Codex貼り付け用）

> このファイルの「===== ここからCodexに貼り付け =====」以降を、Codex CLI（`codex`）の最初のプロンプトとして丸ごと貼り付けてください。
> 画像は同じフォルダの `assets/` を再利用します（事前に assets フォルダを置いておくこと）。

---

===== ここからCodexに貼り付け =====

あなたは一流のフロントエンドエンジニア兼Webデザイナーです。長野県・白樺湖畔の旅館「白樺湖レイクサイドホテル山幸閣」の公式サイトを、単一の静的サイト（依存パッケージなし・素のHTML/CSS/JS）として作成してください。出力は `index.html` と `maxhub.html` の2ファイル。画像はカレントの `assets/` フォルダにある既存ファイルと、指定の外部URLを使います。ビルドツールやフレームワークは使わないこと。

## 1. ブランドの核（最重要）
- ポジショニング：「思い出を創作する宿」。ただ泊まる宿ではなく、**合宿・団体・サプライズ演出**に特化。
- メインターゲット：①学校・教育旅行 ②吹奏楽・スポーツ・音楽合宿 ③大人のスノボ合宿 ④バイク・ツーリング団体 ⑤企業研修・団体研修・ワーケーション。
- 最大の差別化：お客様ごとの**サプライズ演出**（打ち上げ花火・表彰式・記念日）。
- 強み資産：全65室（最大10名/室）、大広間・コンベンションホール、大型バス20台駐車場、白樺湖畔（標高1,400m・ビーナスライン起点）、MaxHub（オールインワン会議システム）導入予定、吹奏楽強豪校・企業研修の実績。
- 連絡先：TEL 0266-68-2021 / FAX 0266-68-2092 / 〒391-0301 長野県茅野市北山3424-1-74 / IN15:00(最終21:00) OUT10:00。

## 2. デザインシステム（厳守）
CSS変数で定義すること：
```
--ink:#1b2826; --ink-soft:#33433f; --paper:#f6f3ec; --paper-2:#efe9dd;
--teal:#2f5d57; --teal-light:#4f827a; --gold:#b29a63; --ember:#d8743f;
--text:#2b2a26; --muted:#6f6b62;
```
フォント（Google Fonts読み込み）：
- 見出し(和)：'Noto Serif JP'、本文(和)：'Noto Sans JP'、英語ディスプレイ：'Cormorant Garamond'、ラベル小文字：'Jost'。
スタイル方針：日本語エディトリアル／上品なミニマル／余白広め（セクション padding 7rem 0 目安）。英語の見出しは Cormorant Garamond の大きめセリフ、和見出しは Noto Serif JP で字間広め(letter-spacing .1em前後)。ラベルは Jost 大文字＋字間 .3em。アクセントは teal＋gold、サプライズ/CTAは ember(オレンジ)。本文 font-weight:300、行間1.9〜2.3。
共通：固定ヘッダー（スクロールで paper 背景＋影に変化）、スクロールで各要素がフワッと出る（IntersectionObserver の `.reveal`→`.in`）、ホバーで画像 scale(1.05)・ナビに gold 下線、900pxでハンバーガーメニュー。角丸は2〜3px、影は控えめ。

## 3. 画像アセット
ローカル `assets/`（既存）：
- `fireworks.png`（湖上の打ち上げ花火・夜）／`camp-students.png`（学生の高原合宿）／`camp-snowboard.png`（大人のスノボ4人組）／`camp-bike.png`（湖畔のツーリングバイク隊列）／`meeting-maxhub.png`（大型ディスプレイのミーティングルーム）／`maxhub-sports.png`（スポーツ映像分析）／`maxhub-webconf.png`（Web会議の研修）／`brass-band.png`（吹奏楽の合奏練習）。
旅館の実写真（外部URL・直リンク可）。ベースURL `https://sankokaku.com/wp/wp-content/uploads/2024/06/`：
- `PhotoGallery-10.webp`（白樺湖の空撮＝最重要の風景）/ `PhotoGallery-2.webp`（大浴場）/ `PhotoGallery-4.webp`（湖畔の外観）/ `PhotoGallery-5.webp`（大広間）/ `PhotoGallery-7.webp`（ロビー）/ `PhotoGallery-9.webp`（客室の湖ビュー）/ `PhotoGallery-6.webp`（ニッコウキスゲ咲く高原）/ `PhotoGallery-1.webp`,`PhotoGallery-3.webp`（館内）/ `top-room.webp`（和室レイクビュー）/ `TOP_facility.webp`（ラウンジ）/ `TOP_sights.webp`（周辺）/ `plan1.webp`,`plan2.webp`,`plan3.webp`（プラン）。

## 4. index.html のセクション構成（この順番・この文言で）
1. **ユーティリティバー**（ink背景）：左「信州・白樺湖畔 標高1,400m｜合宿・団体・サプライズ演出の宿」／右「合宿・団体のご相談 0266-68-2021」。
2. **ヘッダー**：ロゴ「山幸閣 / SHIRAKABAKO LAKESIDE HOTEL」。ナビ：サプライズ演出(#surprise)／合宿・団体(#camp)／客室(#rooms)／施設(#feature)／ギャラリー(#gallery)／アクセス(#info)。右に「合宿の相談」ボタン(#cta)。
3. **ヒーロー**（全画面・背景 `assets/fireworks.png` ではなく `PhotoGallery-10.webp`＝白樺湖空撮、ゆっくりズーム）：ラベル「Memories by the Lake — Shirakabako」／h1「ここでしか、つくれない思い出がある。」＋小さく「合宿と団体の、記憶に残る宿」／斜体英語「— where every stay becomes a story —」／下部に Scroll。
4. **イントロ**：ラベル「Our Mission」／h2「『泊まる』より、『忘れられない』を。」／本文（標高1,400m・白樺湖畔、学校/スポーツ/音楽/スノボ/バイク仲間の合宿、一生の思い出を「創作」する宿）。
5. **数字カウントアップ**（スクロールで0から加算）：65室／10名・室／20台(大型バス)／1,400m(標高)。
6. **サプライズ演出**（ダーク・背景 `assets/fireworks.png`＋上にcanvasで動く花火アニメ）：ラベル「The Sankokaku Experience」(ember)／h2「夜空に、あなたのための **打ち上げ花火**を。」(「打ち上げ花火」をemberで発光)／本文（だいご味＝お客様だけのサプライズ。卒業の花火・優勝の表彰式…）／演出メニューのピル（打ち上げ花火/表彰式・セレモニー/サプライズ記念日/オリジナル横断幕/特別ディナー演出/ご要望に合わせて）／演出の流れ3ステップ（ご相談→演出プランご提案→当日サプライズ）／注記。
7. **合宿・団体**（#camp、4枚グリッド／縦長カード・下に半透明グラデで文字）：①学校・教育旅行(`camp-students.png`)②スポーツ・音楽合宿(`PhotoGallery-6.webp`)③大人のスノボ合宿(`camp-snowboard.png`)④バイク・ツーリング団体(`camp-bike.png`)。各番号・見出し・短文。
8. **実績**（#proof、ダーク）：見出し「Proven Track Record／選ばれる理由・実績」。カードA(画像左)：`brass-band.png`＋「吹奏楽の強豪校に、選ばれています。」＋お客様の声(引用)。カードB(画像右・反転)：`maxhub-webconf.png`＋「企業研修・団体研修にも、豊富な実績。」＋ご担当者の声。下にタグ帯「こんな団体に、ご利用いただいています」＝学校・教育旅行／吹奏楽・音楽部／スポーツ部／企業研修／団体研修／ゼミ・研究室／スノボ・バイク団体。
9. **MaxHub**（#meeting）：見出し「Smart Meeting Room／MaxHub完備の合宿」。横並びカード：画像 `meeting-maxhub.png`＋「New · DX 設備」バッジ／右に「合宿が、もっと"伸びる"場所へ。」＋本文＋3用途リスト（スポーツ＝映像で動作チェック／ゼミ・研修＝ワイヤレスでプレゼン共有／企業合宿・ワーケーション＝Web会議対応）＋リンク「MaxHubのページを詳しく見る」→ `maxhub.html`。
10. **施設**（#feature、交互レイアウト3行）：①大広間(`PhotoGallery-5.webp`)②大浴場(`PhotoGallery-2.webp`)③白樺湖まるごと(`PhotoGallery-10.webp`)。各見出し＋斜体英語＋本文＋more リンク。
11. **ロケーション/衛星ビュー**（#location）：左にコピー（白樺湖畔という特等席・諏訪南ICから40分等のピル）、右に Google衛星マップ iframe（APIキー不要の埋め込み：`https://maps.google.com/maps?q=白樺湖レイクサイドホテル山幸閣&t=k&z=15&hl=ja&output=embed`、t=k＝衛星）。
12. **客室**（#rooms、ダーク・3カード）：和室（〜10名/室）`top-room.webp`／和洋室 `PhotoGallery-9.webp`／ツイン `plan1.webp`。
13. **プラン**（#plans、3カード）：合宿スタンダード2食付(¥6,500〜目安)`plan2.webp`／スノボ・素泊まり団体(¥4,500〜目安)`plan1.webp`／★思い出演出パッケージ(要相談・ember枠)`fireworks.png`。価格は「目安」表記。
14. **ギャラリー**（#gallery、masonry 4列）：`fireworks.png`,`PhotoGallery-10`,`camp-students`,`PhotoGallery-5`,`camp-bike`,`camp-snowboard`,`PhotoGallery-7`,`PhotoGallery-9`,`TOP_facility`,`PhotoGallery-1`,`top-room`,`TOP_sights` など。
15. **CTA**（#cta、背景 `PhotoGallery-4.webp`）：「あなたの合宿を、一生の思い出に。」＋ボタン2つ（電話 tel:0266-68-2021 ／ 見積り相談 #info）。
16. **アクセス/情報**（#info、ダーク）：所在地・客室数(全65室)・団体設備(大広間/ホール/MaxHub導入予定)・標高・IN/OUT・駐車場(乗用車100/大型バス20)・電車(JR茅野駅→バス50分 西白樺湖 徒歩1分)・車(諏訪南IC40分/佐久南IC50分)。右に大きなTEL＋Google Mapボタン。
17. **フッター**（#141d1b）：ロゴ・住所・TEL、リンク2列（MaxHub/サプライズ/合宿プラン/客室、ギャラリー/アクセス/相談/電話）、コピーライト。

## 5. JavaScript（素のJSのみ）
- ヘッダー：scrollY>60 で `.scrolled` クラス付与。
- ハンバーガー：ナビ開閉、リンククリックで閉じる。
- リビール：IntersectionObserver で `.reveal`→`.in`。
- 数字カウントアップ：`.stat .num[data-to]` を可視時に easeOutCubic で0→目標値、`toLocaleString()`でカンマ。
- 花火アニメ：サプライズ部の `<canvas>` に requestAnimationFrame で粒子花火。可視時のみ稼働。`mix-blend-mode:screen`、色は金/オレンジ系、1.2秒ごとに新しい打ち上げ。

## 6. maxhub.html（下層ページ・同じデザインシステム）
ヘッダー/フッターは index と共通（ロゴは index.html へリンク）。構成：
1. ヒーロー（背景 `meeting-maxhub.png`／パンくず「TOP / Smart Meeting Room」／「MaxHub 完備」バッジ／h1「白樺湖で、成果の出る合宿を。」＋小さく「オールインワン会議システム『MaxHub』完備のミーティングルーム」）。
2. イントロ「"泊まる合宿"から、"伸びる合宿"へ。」。
3. **Why MaxHub**：Before/After 対比（これまでの合宿＝映像が小さい/紙資料/遠隔不可/板書消える → MaxHubのある合宿＝大画面で映像分析/ワイヤレス共有/Web会議/データ保存）。中央にemberの矢印。
4. **できること**：機能6カード（4K大画面タッチ／電子ホワイトボード／ワイヤレス画面共有／Web会議対応／映像再生・分析／記録・持ち帰り）。
5. **用途別シーン**（ダーク・交互3行）：①スポーツ合宿の映像分析(`maxhub-sports.png`)②企業研修・ワーケーション(`maxhub-webconf.png`)③吹奏楽・音楽合宿(`brass-band.png`／演奏の録音録画を大画面で振り返り)。各 tag＋見出し＋本文＋bullet。
6. **設置場所**：ミーティングルーム(`meeting-maxhub.png`)／ロビー(`PhotoGallery-7.webp`)。
7. **CTA**（背景 `PhotoGallery-10.webp`）：「成果の出る合宿を、白樺湖で。」＋電話/見積りボタン＋注記「MaxHubは導入予定」。
8. フッター（index と共通、MaxHubリンクあり）。

## 7. 品質要件
- レスポンシブ必須（900pxでナビ→ハンバーガー、グリッド→1〜2列、交互レイアウト→縦積み、衛星マップ→下、520pxで1列）。
- 画像は `object-fit:cover`、`loading="lazy"` を適宜。リンク切れを作らない。
- コンソールエラーゼロ。`<canvas>` 花火が重すぎないよう粒子数を抑える。
- AI使用の事実はページに記載しないこと。
- まず2ファイルを作り、簡易ローカルサーバ（例：`python -m http.server` か Node静的サーバ）で表示確認し、レイアウト崩れ・リンク切れ・コンソールエラーがないか自己点検してから完了報告すること。

===== ここまで =====
