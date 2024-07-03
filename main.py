import tkinter as tk
import winsound
from tkinter import ttk
from threading import Thread
from queue import Queue
from transformers import pipeline

print("読み込み中...")
ej_translator = pipeline("translation", model="staka/fugumt-en-ja", device=0)


def translate_text():
    output_area.config(state=tk.NORMAL)
    output_area.delete("1.0", tk.END)
    translate_button.config(state=tk.DISABLED)

    def translate_line_by_line(queue):
        input_text = text_area.get("1.0", tk.END).strip()

        # 空行を除いて1行ごとに翻訳
        for input_sentence in input_text.split("\n"):
            if input_sentence:
                result = ej_translator(input_sentence)
                translated_text = str(result).replace("[{'translation_text': '", "").replace("'}]", "")
                queue.put(translated_text)
            else:
                queue.put("")

    # スレッドを作成して翻訳処理をバックグラウンドで実行
    translation_queue = Queue()
    translation_thread = Thread(target=translate_line_by_line, args=(translation_queue,))
    translation_thread.start()

    def update_output_area():
        # キューから翻訳結果を取得してGUIに表示
        while not translation_queue.empty():
            translated_text = translation_queue.get_nowait()
            output_area.insert(tk.END, translated_text + "\n")

        # スレッドがまだ生きている場合、再度キューのチェックを行う
        if translation_thread.is_alive():
            root.after(100, update_output_area)
        else:
            output_area.config(state=tk.DISABLED)
            translate_button.config(state=tk.NORMAL)
            winsound.MessageBeep(winsound.MB_OK)  # 完了音を鳴らす

    # 100msごとにキューをチェックしてGUIを更新
    root.after(100, update_output_area)


# GUIレイアウト設定
root = tk.Tk()
root.title("FuguMT 英日翻訳")
root.geometry("500x500")

# 日本語の入力エリア
input_label = ttk.Label(root, text="翻訳したい文章 (en)")
input_label.pack(padx=10, pady=10)

input_frame = tk.Frame(root)
input_frame.pack(padx=10, pady=10)

text_area = tk.Text(input_frame, wrap=tk.WORD, height=12, width=60)
text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

input_scrollbar = tk.Scrollbar(input_frame, command=text_area.yview)
input_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text_area.config(yscrollcommand=input_scrollbar.set)

# 翻訳ボタン
translate_button = ttk.Button(root, text="翻訳", command=translate_text)
translate_button.pack(pady=10)

# 翻訳結果の出力エリア
output_label = ttk.Label(root, text="翻訳結果 (ja)")
output_label.pack(padx=10, pady=10)

output_frame = tk.Frame(root)
output_frame.pack(padx=10, pady=10)

output_area = tk.Text(output_frame, wrap=tk.WORD, height=12, width=60, state=tk.DISABLED)
output_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

output_scrollbar = tk.Scrollbar(output_frame, command=output_area.yview)
output_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
output_area.config(yscrollcommand=output_scrollbar.set)

root.mainloop()
