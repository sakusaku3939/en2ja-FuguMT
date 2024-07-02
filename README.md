# FuguMT ローカル翻訳 (en → ja)
[FuguMT](https://huggingface.co/staka/fugumt-en-ja)を使用したWindowsローカル環境で動かせるシンプルな翻訳システム。GUIウィンドウが起動します。

![image](https://github.com/sakusaku3939/en2ja-FuguMT/assets/53967490/13a034be-6106-4793-b0dd-41f030472dae)

### 1. 環境構築
```
python -m venv .venv
```

```
pip install transformers==4.26.1
pip install sentencepiece sacremoses
pip install torch -f https://download.pytorch.org/whl/torch_stable.html
```

### 2. 実行
```
python main.py
```
