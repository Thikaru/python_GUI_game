# GUIのライブラリ
import tkinter


# ボタン押下時に実行したい処理
def click_btn():
    button['text'] = "クリックされました"


# ウィンドウの部品を作成する．この部品のことをオブジェクトという．
root = tkinter.Tk()
# ウィンドウのタイトルを指定
root.title("初めてのウィンドウ")
# ウィンドウサイズを指定
root.geometry("800x600")

# ラベル追加
# ラベルの部品を作る
label = tkinter.Label(root, text="ラベルの文字列", font=("Times New Roman", 24))
# ウィンドウにラベルを配置
label.place(x=200, y=100)

# ボタン追加
# ボタンの部品を作る
button = tkinter.Button(root, text="ボタンの文字列", font=(
    "Times New Roman", 24), command=click_btn)
# ウィンドウにボタンを配置する
button.place(x=400, y=300)

# ウィンドウを表示する
root.mainloop()
