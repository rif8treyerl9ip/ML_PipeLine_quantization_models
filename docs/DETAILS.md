### シード設定

本プロジェクトでは、機械学習モデルの再現性を確保するために、シード設定を一元管理しています。以下の関数`seed_everything`を用いて、様々な乱数生成器のシードを統一的に設定しています。

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