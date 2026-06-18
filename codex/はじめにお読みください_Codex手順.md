# Codexで山幸閣サイトを作る手順（Windows 11）

Claude版と別フォルダに、Codex（OpenAIのコーディングエージェント）で同じサイトを作ります。
所要：インストール5分＋生成。**Claude版は上書きしません**（比較できます）。

---

## 0. 必要なもの
- **Node.js 22以上**（Codexのnpm版に必須）。`node -v` で確認。
- **ChatGPT 有料プラン**（Plus / Pro / Business / Edu / Enterprise のいずれか）。Codex CLIはこのプランに含まれます。無料アカウントは不可。
- ※ APIキーでも使えますが、まずはChatGPTサインインが簡単です。

---

## 1. Codex CLI をインストール（PowerShell）
次のどちらか。**パッケージ名を間違えないこと**（`codex` 単体は無関係の別物。必ず `@openai/codex`）。

```powershell
# 方法A：npm（Node 22+ が必要）
npm install -g @openai/codex

# 方法B：公式インストーラ（Nodeなしでも可）
powershell -ExecutionPolicy ByPass -c "irm https://chatgpt.com/codex/install.ps1 | iex"
```

確認：
```powershell
codex --version
```
※ `codex` が見つからない場合はPowerShellを開き直す（PATH反映のため）。

---

## 2. 作業フォルダを用意（Claude版を温存）
このフォルダ（`案件/山幸閣_サイトリニューアル`）の中に、Codex用の別フォルダを作り、**画像だけコピー**します。

```powershell
$base = "C:\Users\user\OneDrive\Desktop\①Claude Code\案件\山幸閣_サイトリニューアル"
New-Item -ItemType Directory -Force "$base\codex-ban"
Copy-Item "$base\assets" "$base\codex-ban\assets" -Recurse
Copy-Item "$base\codex\AGENTS.md" "$base\codex-ban\AGENTS.md"
```

> これで `codex-ban\`（Codex版）に `assets\` と `AGENTS.md` が入ります。Codexはこのフォルダに `index.html` / `maxhub.html` を作ります。

---

## 3. Codexを起動して認証
```powershell
codex --cd "C:\Users\user\OneDrive\Desktop\①Claude Code\案件\山幸閣_サイトリニューアル\codex-ban"
```
初回は **「Sign in with ChatGPT」** を選択 → ブラウザでログイン → ターミナルに戻る。

---

## 4. ビルドプロンプトを貼り付け
1. `codex\CODEX_BUILD_PROMPT.md` を開く。
2. 「===== ここからCodexに貼り付け =====」〜「===== ここまで =====」の**間を全部コピー**。
3. Codexのプロンプト欄に貼り付けて実行。
4. ファイル作成・コマンド実行の許可を聞かれたら承認（Approvalモード）。

> モデルを変えたい時はCodex内で `/model`（例：高品質なら上位モデル、軽作業なら mini）。

---

## 5. 確認
Codexが `index.html` / `maxhub.html` を作ったら、ブラウザで開くか簡易サーバで確認：
```powershell
cd "C:\Users\user\OneDrive\Desktop\①Claude Code\案件\山幸閣_サイトリニューアル\codex-ban"
python -m http.server 3030   # → http://localhost:3030
```
（PythonがなければエクスプローラからHTMLをダブルクリックでもOK。ただし衛星マップ等は簡易サーバ推奨）

---

## 6. 直したい時
Codexに続けて日本語で指示すればOK（例：「ヒーローの文字をもっと大きく」「花火をもっと派手に」）。Claude版（`index.html`）と見比べて、良い方を採用・融合できます。

---

## つまずきポイント
| 症状 | 対処 |
|---|---|
| `codex` が見つからない | PowerShell開き直し。`$env:PATH` にnpmのグローバルbinが必要 |
| 認証が通らない | ChatGPTが無料プラン／別アカウントでログインの可能性。`codex auth logout` → 再ログイン |
| `npm i -g codex` を実行してしまった | 無関係の別パッケージ。`npm uninstall -g codex` → `npm install -g @openai/codex` |
| Node が古い | Node 22以上へ更新（または方法Bのインストーラを使用） |
| 画像が出ない | `codex-ban\assets\` に画像がコピーされているか確認（手順2） |

---

## 補足：Claude版 と Codex版 の比較ポイント
- **デザイン忠実度**（配色・余白・タイポ）
- **花火アニメ／カウントアップの実装品質**
- **レスポンシブの崩れにくさ**
- **修正指示への追従**
同じプロンプト・同じ画像で作るので、ツールの"クセ"がよく分かります。Claude版は `案件/山幸閣_サイトリニューアル/index.html` にあります。
