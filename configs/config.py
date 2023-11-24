import random
import os
import numpy as np
import torch

def seed_everything(seed=42):
    random.seed(seed)  # Python標準のrandomモジュールのシードを設定
    os.environ['PYTHONHASHSEED'] = str(seed)  # ハッシュ生成のためのシードを環境変数に設定
    np.random.seed(seed)  # NumPyの乱数生成器のシードを設定
    torch.manual_seed(seed)  # PyTorchの乱数生成器のシードをCPU用に設定
    torch.cuda.manual_seed(seed)  # PyTorchの乱数生成器のシードをGPU用に設定
    torch.backends.cudnn.deterministic = True  # PyTorchの畳み込み演算の再現性を確保

seed_everything()  # 上述のシード設定関数を呼び出し


CONFIG_PATH = "C:/Users/thyt/Learning/Learning_py/Repositories/ML_PipeLine_quantization_models/configs",

RAW_DATA_PATH = "C:/Users/thyt/Learning/Learning_py/Repositories/ML_PipeLine_quantization_models/data",
PREPROCESSED_DATA_PATH = "C:/Users/thyt/Learning/Learning_py/Repositories/ML_PipeLine_quantization_models/data/preprocessed",

LOG_PATH = "C:/Users/thyt/Learning/Learning_py/Repositories/ML_PipeLine_quantization_models/logs",

RAW_MODELS_PATH = "C:/Users/thyt/Learning/Learning_py/Repositories/ML_PipeLine_quantization_models/models/raw_models",
PREPROCESSED_MODELS_PATH = "C:/Users/thyt/Learning/Learning_py/Repositories/ML_PipeLine_quantization_models/models/preprocessed_models",
QUANTIZED_MODELS_PATH = "C:/Users/thyt/Learning/Learning_py/Repositories/ML_PipeLine_quantization_models/models/quautized_models",
MODELS_DB_PATH = "C:/Users/thyt/Learning/Learning_py/Repositories/ML_PipeLine_quantization_models/models/DB",

PREPROCESSING_PATH = "C:/Users/thyt/Learning/Learning_py/Repositories/ML_PipeLine_quantization_models/preprocessing"