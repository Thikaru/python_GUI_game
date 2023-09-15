import tkinter

root = tkinter.Tk()
root.title("初めてのキャンバス")

# キャンバスの部品を作成する
canvas = tkinter.Canvas(root, width=400, height=600, bg="skyblue")
# ウィンドウにキャンバスを配置
# pack()命令で配置するとキャンバスのサイズに合わせてウィンドウサイズが決まる．\
# ウィンドウにキャンバスだけ置くならこのプログラムのようroot.geometry()を省略できる．
canvas.pack()

# 画像を表示
# 画像ファイルを読み込む
image_iroha = tkinter.PhotoImage(file="images/iroha.png")
# キャンバスに画像を描画 create_image(x座標の中心, y座標の中心,image=読み込んだ画像ファイル)
canvas.create_image(200, 300, image=image_iroha)

root.mainloop()
