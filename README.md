# FuguMT ローカル翻訳 (en → ja)
[FuguMT](https://huggingface.co/staka/fugumt-en-ja)を使用したWindowsローカル環境で動かせるシンプルな翻訳システム。なんとGUIウィンドウが起動します。

![image](https://github.com/sakusaku3939/en2ja-FuguMT/assets/53967490/41d4f457-5a06-42a1-8eca-b1ae4fc18932)


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
