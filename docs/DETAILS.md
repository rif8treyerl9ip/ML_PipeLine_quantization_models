### シード設定

本プロジェクトでは、機械学習モデルの再現性を高めるために、シード設定を一元管理しています。以下の関数`seed_everything`を用いて、様々な乱数生成器のシードを統一的に設定しています。

ファイルパス：configs\config.py

```python
def seed_everything(seed=42):
    random.seed(seed)  # Python標準のrandomモジュールのシードを設定
    os.environ['PYTHONHASHSEED'] = str(seed)  # ハッシュ生成のためのシードを環境変数に設定
    np.random.seed(seed)  # NumPyの乱数生成器のシードを設定
    torch.manual_seed(seed)  # PyTorchの乱数生成器のシードをCPU用に設定
    torch.cuda.manual_seed(seed)  # PyTorchの乱数生成器のシードをGPU用に設定
    torch.backends.cudnn.deterministic = True  # PyTorchの畳み込み演算の再現性を確保

seed_everything()  # 上述のシード設定関数を呼び出し
```


#### 本リポジトリの実験管理方法のメリット
1. **一元管理された実験開発**: 当リポジトリでは、アドホックな実験を一元管理することが可能です。複数の実験を一つのスクリプトで効率的に開発し、管理することができます。

2. **フレキシブルなフロントエンド**: Flaskを活用し、実験管理ツールのフロントエンドを柔軟にカスタマイズすることができます。これにより、ユーザーのニーズに合わせたインターフェースを提供できます。

#### デメリット
1. **コード管理の課題**: 当リポジトリのコード管理には、特定の点で複雑性があります。例えば、特定のモデルを実行した際のノートブックを「ショートコミットハッシュ_yyyymmdd」という形式で追跡する必要があります。これは標準的な管理方法からの逸脱であり、使用者には理解しづらいかもしれません。

2. **実験管理プロセスの複雑さ**: 実験管理に関するプロセスが複雑で、以下のような重要な項目のハードコーディングが難しい場合があります。
    - モデルのパス (`model_path`)
    - モデルのバージョンID (`model_version_id`)
    - モデルID (`model_id`)
    - パラメータ (`parameters`)
    - トレーニングデータセットのパス (`training_dataset_path`)
    - バリデーションデータセットのパス (`validation_dataset_path`)
    - テストデータセットのパス (`test_dataset_path`)
    - アーティファクトファイルのパス (`artifact_file_paths`)