
DB設計による効率的なコラボレーション




# モデルフォルダ構造

以下に、量子化関連のデータベース設計に使用されるモデルのフォルダ構造を示します：

```
C:.
├─preprocessed_models
├─quantized_models
└─raw_models
```

- `preprocessed_models`: 前処理済みのモデルが格納されるフォルダ
- `quantized_models`: 量子化されたモデルが格納されるフォルダ
- `raw_models`: 元の（未処理の）モデルが格納されるフォルダ
```

この例では、フォルダ名の綴りを英語に修正し（`preprocessd_models` を `preprocessed_models` に、`quautized_models` を `quantized_models` に）、Markdownのコードブロック（`` ``` ``）を使用してフォルダ構造を視覚的に表現しています。また、各フォルダの説明も加えています。これにより、`README.md` ファイルの読者がフォルダ構造とその内容を容易に理解できるよう





webサーバ立ち上げの仮想環境とは分ける
必要な処理
>poetry add uvicorn