# Lumi Jelly PNGTuber

[English](./README.md) | [日本語](./README.ja.md) | [頭部5方向版](https://github.com/Sunwood-ai-labs/lumi-jelly-head-motion-pngtuber)

天体クラゲをモチーフにした、衣装付き上半身の正面向きPNGTuber素材です。
このリポジトリには汎用的な6表情版だけを収録しています。頭部のみの5方向版と
方向制御パッチは、別リポジトリへ分離しています。

<p align="center">
  <img src="./avatar/concept.png" width="520" alt="衣装付き上半身の天体クラゲPNGTuber Lumi Jelly">
</p>

<p align="center">
  <img alt="衣装付き上半身版" src="https://img.shields.io/badge/%E7%89%88-%E8%A1%A3%E8%A3%85%E4%BB%98%E3%81%8D%E4%B8%8A%E5%8D%8A%E8%BA%AB-5865f2">
  <img alt="6表情" src="https://img.shields.io/badge/%E8%A1%A8%E6%83%85-6-6c63ff">
  <img alt="1024 x 1024" src="https://img.shields.io/badge/Canvas-1024%C3%971024-20a4c8">
  <img alt="Image Gen生成元保存" src="https://img.shields.io/badge/Image%20Gen-%E7%94%9F%E6%88%90%E5%85%83%E4%BF%9D%E5%AD%98-8b5cf6">
</p>

## プレビュー

![Lumi Jellyの目と口を組み合わせた6表情](./avatar/expression-preview.png)

開眼／閉眼と、口閉じ／半開き／全開きを組み合わせた6枚です。すべて同じ
透過 `1024 × 1024` キャンバスに整列しています。`back-hair.png` と
`front-hair.png` は互換用の透明レイヤーで、髪と衣装の完成画は各表情PNGに
含まれています。

## 素材の使い方

[`avatar/`](./avatar/) の画像を、使用するPNGTuberアプリの各状態へ割り当てます。

| 状態 | ファイル |
| --- | --- |
| 開眼・口閉じ | `eyes-open-mouth-closed.png` |
| 開眼・口半開き | `eyes-open-mouth-half.png` |
| 開眼・口全開き | `eyes-open-mouth-open.png` |
| 閉眼・口閉じ | `eyes-closed-mouth-closed.png` |
| 閉眼・口半開き | `eyes-closed-mouth-half.png` |
| 閉眼・口全開き | `eyes-closed-mouth-open.png` |

PuruPuru PNGTuberで使用した設定は
[`avatar/default-settings.json`](./avatar/default-settings.json)、実アプリの確認画像は
[`docs/screenshots/lumi-jelly-screenshot-proof-v2.png`](./docs/screenshots/lumi-jelly-screenshot-proof-v2.png)
に保存しています。

## リポジトリ構成

```text
avatar/                 6枚の実行用PNG、設定、コンセプト、表情一覧
provenance/source/      未加工のImage Gen出力
provenance/keyed/       背景除去済み中間PNG
provenance/PROMPTS.md   マスターと同一性維持編集のプロンプト
tools/                  決定論的な正規化ツール
docs/screenshots/       実アプリでの確認証拠
SHA256SUMS              公開ファイルの整合性マニフェスト
```

頭部方向素材、方向制御コード、不採用の旧試作はこのリポジトリに含めません。

## 実行用PNGの再構築

```bash
python3 -m pip install Pillow
./tools/render_lumi_jelly_assets.sh
```

再構築で行うのはクロマ背景の除去、サイズと余白の正規化、互換レイヤーの生成だけです。
Image Genキャラクターの描き直しやコード描画への置換は行いません。

## 頭部5方向版

頭部のみ、正面・左・右・上・下、合計30状態、PuruPuru方向制御パッチ付きの版は
[`lumi-jelly-head-motion-pngtuber`](https://github.com/Sunwood-ai-labs/lumi-jelly-head-motion-pngtuber)
にあります。

## 来歴

- 2026-07-15にOpenAI組み込みImage Genで制作。
- 承認済みマスターを同一性維持編集し、6表情を生成。
- 未加工出力、中間PNG、プロンプトをリポジトリ内に保存。
- 特定の作家、既存キャラクター、第三者キャラクター素材は参照していません。

## ライセンスとクレジット

- キャラクター画像と生成元: [LICENSE-ASSETS.md](./LICENSE-ASSETS.md)
- `tools/` のコード: [LICENSE-CODE](./LICENSE-CODE)
- 確認対象アプリ: masa氏の [PuruPuru PNGTuber](https://github.com/rotejin/PuruPuruPNGTuber)

生成物に関するユーザーとOpenAIの関係にはOpenAIの規約が適用されます。
各法域での著作権成立や第三者権利非侵害を保証するものではありません。
