# YouTube Video Comment Recording

YouTube動画で話し手が話していることを、SQLite3データベースに記録するためのシステムです。

## 使い方

1. main.py に対象の動画のURLを記入する
2. 以下の前提を満たし、パッケージをインストールする
3. `python main.py` を実行する (ノートブック版: main.ipynb)
4. 生成されたSQLite3を煮るなり焼くなり好きに活用する

## 前提

- FFmpeg
- CUDA 11.8
- ccDNN v8.9.6 for CUDA 11.8
- Python 3.11+

## パッケージのインストール

使用しているパッケージは `requirements.txt` に記載されている通りです。
しかし、そのままではCUDAを使用できないので、以下のコマンドでインストールしてください。

```bash
pip install -r requirements.txt
pip uninstall -y torch torchvision torchaudio
pip cache purge
pip install cuda-python
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```
