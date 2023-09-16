import tkinter
import random


## ====  class  ==== ##
# メンバ変数として
# result：おみくじの結果
# text：
# probability：正の整数を入れる
class OmikujiResutlt:
    total_probability = 0

    def __init__(self, result, text, probability):
        self.result = result
        self.text = text
        self.probability = probability
        OmikujiResutlt.total_probability += probability


omikuji_resutlts = [
    OmikujiResutlt(
        "  大凶  ", "最悪に今日はついてない日になるかも？\n逆に運がいいともいう笑\nしかし，明日からは上り調子だ", 10),
    OmikujiResutlt(
        "    凶    ", "今日はついてないね？\n危険だと思うことはしない方がいいかも涙\n明日からは上り調子かも！？", 50),
    OmikujiResutlt(
        "  末吉  ", "中途半端な運勢だね！！\n今日1日は何も起こらないかも\n大きな成功も失敗もしないだろう！", 500),
    OmikujiResutlt(
        "  小吉  ", "小さな奇跡が起こるかも！！\n小さなことでもしっかり喜ぼう．\n小さなことからコツコツと！", 500),
    OmikujiResutlt(
        "  中吉  ", "無くしたものが見つかったり？\n不幸があってもそれを超える大きなことが！\nいつもより幸せ気分で頑張ろう！", 500),
    OmikujiResutlt(
        "    吉    ", "吉ってと思うけど，諸説あるけど大吉の次だよ！！！\n結構すごいよ，ラッキー\n幸せを掴み取れ", 300),
    OmikujiResutlt(
        "  大吉  ", "だ．だ．大吉やるやん！！\nとりあえず何でもやってみよう．うまくいく！\n今日は大丈夫な日です．", 100),
    OmikujiResutlt(
        "  極吉  ", "これが一番最強な日にしか出ません！！\n最高の運気をまとっているよ！\n挑戦して成功をつかめ！", 1),
]

## ====  変数  ==== ##
test_mode = False


def FitString(words):
    strings = ""
    string_num = 17
    add_space = "　"
    split_string = words.split('\n')

    for i in range(len(split_string)):
        seventeen_words = [split_string[i][x:x+string_num]
                           for x in range(0, len(split_string[i]), string_num)]
        for j in range(len(seventeen_words)):
            if len(seventeen_words[j]) < string_num:
                for k in range(string_num-len(seventeen_words[j])):
                    seventeen_words[j] += add_space
            strings += seventeen_words[j]+"\n"

    return strings


def DealFortune():
    total_probability = OmikujiResutlt.total_probability
    sum_num_start = 1
    sum_num_end = 0
    random_num = random.randint(1, total_probability)
    for i in range(len(omikuji_resutlts)):
        sum_num_end += omikuji_resutlts[i].probability
        if sum_num_start <= random_num and random_num <= sum_num_end:
            if test_mode != True:
                result_label["text"] = omikuji_resutlts[i].result
                result_text["text"] = FitString(omikuji_resutlts[i].text)
            return str(omikuji_resutlts[i].result)
        sum_num_start += omikuji_resutlts[i].probability


if test_mode == True:
    # DealFortune()をテストする処理
    i = 0
    array = [0, 0, 0, 0, 0, 0, 0, 0]
    while (True):
        test = DealFortune()
        if test == "  極吉  ":
            array[7] += 1
            break
        elif test == "  大凶  ":
            array[0] += 1
        elif test == "    凶    ":
            array[1] += 1
        elif test == "  末吉  ":
            array[2] += 1
        elif test == "  小吉  ":
            array[3] += 1
        elif test == "  中吉  ":
            array[4] += 1
        elif test == "    吉    ":
            array[5] += 1
        elif test == "  大吉  ":
            array[6] += 1
        i += 1
    for i in range(len(array)):
        print(omikuji_resutlts[i].result + " : " + str(array[i]))

    # FitString(words)をテストする処理
    test_strings = [
        "三文字",
        "あいうえおあいうえおあいうえおあい",
        "あいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえお",
        "あいうえお\n",
        "あいうえお\nあいうえお\nあいうえおあいうえおあいうえおあいうえおあいうえおあいうえお",
    ]
    for i in range(len(test_strings)):
        words = FitString(test_strings[i])
        print("")
        print(words)
    for i in range(len(omikuji_resutlts)):
        words = FitString(omikuji_resutlts[i].text)
        print("========")
        print(words)
    quit()

# ウィンドウオブジェクトを作成
root = tkinter.Tk()
root.title("おみくじアプリ")
# ウィンドウサイズを固定する
root.resizable(False, False)
canvas = tkinter.Canvas(root, width=800, height=600)
canvas.pack()
character_image = tkinter.PhotoImage(file="images/miko.png")
canvas.create_image(400, 300, image=character_image)

# 長方形を配置
canvas.create_rectangle(400, 50, 700, 450, fill="white")
result_label = tkinter.Label(
    root, text=" ？？ ", foreground='white', font=("Times New Roman", 50), bg="gray")
result_label.place(x=475, y=60)

result_text = tkinter.Label(
    root, text=FitString("おみくじの結果は，上の四角には運勢が，\nその運勢の結果を\nここに表示します．\n"), foreground='white', font=("Times New Roman", 15), bg="gray")
result_text.place(x=425, y=150)


# ボタンの配置
button_image = tkinter.PhotoImage(file="images/Button_Omikuji.png")
button = tkinter.Button(root, text="", image=button_image, command=DealFortune)
button.place(x=400, y=500)

root.mainloop()
