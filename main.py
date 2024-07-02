import tkinter as tk
from tkinter import ttk
from transformers import pipeline

print("読み込み中...")
ej_translator = pipeline("translation", model="staka/fugumt-en-ja", device=0)


def translate_text():
    input_text = text_area.get("1.0", tk.END).strip()
    input_lines = input_text.split("\n")

    # 改行のインデックスと翻訳対象のテキストを抽出
    newline_indices = [index for index, line in enumerate(input_lines) if not line]
    sentences_to_translate = [line for line in input_lines if line]

    # 翻訳を実行し、改行だけの行を元のインデックスに挿入
    translated_results = ej_translator(sentences_to_translate)
    translated_text_list = [result['translation_text'] for result in translated_results]

    for index in newline_indices:
        translated_text_list.insert(index, '')

    output_text = "\n".join(translated_text_list)

    # ウィンドウに翻訳結果を表示
    output_area.config(state=tk.NORMAL)
    output_area.delete("1.0", tk.END)
    output_area.insert(tk.END, output_text)
    output_area.config(state=tk.DISABLED)


# GUIレイアウト設定
root = tk.Tk()
root.title("FuguMT 英日翻訳")
root.geometry("500x500")

input_label = ttk.Label(root, text="翻訳したい文章 (en)")
input_label.pack(padx=10, pady=10)

text_area = tk.Text(root, wrap=tk.WORD, height=12, width=60)
text_area.pack(padx=10, pady=10)

translate_button = ttk.Button(root, text="翻訳", command=translate_text)
translate_button.pack(pady=10)

output_label = ttk.Label(root, text="翻訳結果 (ja)")
output_label.pack(padx=10, pady=10)

output_area = tk.Text(root, wrap=tk.WORD, height=12, width=60, state=tk.DISABLED)
output_area.pack(padx=10, pady=10)

root.mainloop()
