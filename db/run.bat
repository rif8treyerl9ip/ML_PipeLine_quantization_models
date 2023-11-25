call C:\Users\thyt\Pytorch\pytorchenv\Scripts\activate.bat
cd C:\Users\thyt\Learning\Learning_py\Repositories\ML_PipeLine_quantization_models\db

uvicorn src.api.app:app --host 127.0.0.1 --port 8000 --reload --workers 4 --limit-concurrency 8 --limit-max-requests 1000