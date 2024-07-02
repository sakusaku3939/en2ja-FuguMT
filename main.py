import tkinter as tk
from tkinter import ttk
from transformers import pipeline

print("読み込み中...")
ej_translator = pipeline("translation", model="staka/fugumt-en-ja", device=0)


def translate_text():
    input_text = text_area.get("1.0", tk.END).strip()
    output_text = ""

    for input_sentence in input_text.split("\n"):
        # 空行を除いて1行ごとに翻訳
        if input_sentence:
            result = ej_translator(input_sentence)
            translated_text = str(result).replace("[{'translation_text': '", "").replace("'}]", "")
            output_text += translated_text + "\n"
        else:
            output_text += "\n"

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
