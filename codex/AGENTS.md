# AGENTS.md — 山幸閣サイト（Codex用プロジェクト指示）

> Codex CLI は作業ディレクトリの `AGENTS.md` を自動で読み込みます（Claude Code の CLAUDE.md 相当）。
> このファイルを Codex で作業するフォルダの直下に置いてください。

## プロジェクト概要
- 長野県・白樺湖畔の旅館「白樺湖レイクサイドホテル山幸閣」公式サイトの新規制作。
- 技術：素のHTML/CSS/JS（フレームワーク・ビルドツールなし）。出力は `index.html` と `maxhub.html`。
- 画像は同フォルダの `assets/` と、旅館実写真の外部URL（`https://sankokaku.com/wp/wp-content/uploads/2024/06/...`）を使用。

## 守ること
- 日本語UI。文言・構成・配色は `CODEX_BUILD_PROMPT.md` に従う。
- デザイン：日本語エディトリアル／上品ミニマル。配色 ink #1b2826・paper #f6f3ec・teal #2f5d57・gold #b29a63・ember #d8743f。フォントは Noto Serif JP / Noto Sans JP / Cormorant Garamond / Jost。
- ブランドの核：「思い出を創作する宿」。合宿・団体・サプライズ演出（花火）＋MaxHub（会議システム）＋吹奏楽/企業研修の実績。
- レスポンシブ必須（900px / 520px）。コンソールエラーゼロ。リンク切れ厳禁。
- 価格は「目安」表記。お客様の声は実データに差し替え前提のプレースホルダー。AI使用の事実はページに書かない。

## 作業の進め方
1. `index.html` → `maxhub.html` の順で作成。
2. ローカル静的サーバで表示確認（レイアウト・リンク・コンソール）。
3. 自己点検してから完了報告。
