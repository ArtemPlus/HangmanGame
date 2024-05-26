import tkinter as tk
from tkinter import ttk, font
import random as rd
from tkinter.messagebox import showerror, showinfo


class Game(tk.Frame):
    categories = ["Фауна", "Флора", "Еда", "Страны", "Химэлементы"]
    words = [["Медведь", "Собака", "Кошка", "Тигр", "Панда", "Снегирь", "Бегемот",
              "Утконос", "Дельфин", "Кабан", "Лошадь", "Белка", "Слон"],
             ["Ромашка", "Тюльпан", "Василёк", "Гиацинт", "Лаванда", "Сосна", "Берёза"],
             ["Солянка", "Шашлык", "Окрошка", "Гречка", "Холодец"],
             ["Либерия", "Австрия", "Бахрейн", "Боливия", "Венгрия", "Россия", "Япония"],
             ["Водород", "Кремний", "Кальций", "Скандий", "Кобальт"]]
    cnt = 0
    session = 0
    pix = "1000x500"

    def __init__(self, contain):
        super().__init__(contain)
        self.startUI()


    def startUI(self):
        global start_UI
        global notebook
        global vybor
        notebook = ttk.Notebook()
        notebook.grid(row=0, column=0)
        start_UI = tk.Frame()
        start_UI.grid(row=1, column=1)
        notebook.add(start_UI, text="Настройка игры")
        self.font = font.Font(family="Forte", size=20)
        lbl_glav = tk.Label(master=start_UI, text="Vicilitca", font=self.font)
        lbl_glav.grid(row=1, column=3)
        lbl1 = tk.Label(master=start_UI, text="Выберите категорию")
        lbl1.grid(row=2, column=2)
        lbl_pass = tk.Label(master=start_UI, text=" "*50)
        lbl_pass.grid(row=2, column=4)
        vybor = tk.StringVar(value=Game.categories[0])
        get_categories = ttk.Combobox(master=start_UI,
                                      values=Game.categories,
                                      state="readonly",
                                      textvariable=vybor)
        get_categories.grid(row=2, column=3)
        get_categories.bind("<<ComboboxSelected>>", self.__cbx)
        lbl_on_vybor = tk.Label(master=start_UI, textvariable=vybor)
        lbl_on_vybor.grid(row=4, column=3)
        lbl_pass2 = tk.Label(master=start_UI, text=" "*64)
        lbl_pass2.grid(row=3, column=3)
        lbl_inf = tk.Label(master=start_UI, text="Вы выбрали категорию: ")
        lbl_inf.grid(row=4, column=2)
        game_butt = tk.Button(master=start_UI, text="Начать игру", command=self.__gameUI)
        game_butt.grid(row=6, column=3)

    @staticmethod
    def __cbx(*args):
        start_UI.focus()

    def __gameUI(self):
        global image_of_step0
        global game_UI, canva, word, cnt
        global lbl_letter1, lbl_letter2, lbl_letter3, lbl_letter4, lbl_letter5, lbl_letter6, lbl_letter7
        game_UI = tk.Frame()
        game_UI.grid(row=1, column=1)
        Game.session += 1
        word = self.__random_word()
        notebook.add(game_UI, text="Висилица")
        notebook.hide(0)
        canva = tk.Canvas(master=game_UI, bg="white", width=250, height=250)
        canva.grid(row=0, column=3)
        image_of_step0 = tk.PhotoImage(file="Step0.png")
        canva.create_image(0, 0, anchor="nw", image=image_of_step0)
        cnt_lbl = tk.Label(master=game_UI, text="Нажми на нужную букву")
        cnt_lbl.grid(row=1, column=2)
        lbl_word = tk.Label(master=game_UI, text="Слово:")
        lbl_word.grid(row=1, column=3)
        lbl_letter1 = tk.Label(master=game_UI)
        lbl_letter1.grid(row=1, column=4)
        lbl_letter2 = tk.Label(master=game_UI)
        lbl_letter2.grid(row=1, column=5)
        lbl_letter3 = tk.Label(master=game_UI)
        lbl_letter3.grid(row=1, column=6)
        lbl_letter4 = tk.Label(master=game_UI)
        lbl_letter4.grid(row=1, column=7)
        lbl_letter5 = tk.Label(master=game_UI)
        lbl_letter5.grid(row=1, column=8)
        lbl_letter6 = tk.Label(master=game_UI)
        lbl_letter6.grid(row=1, column=9)
        lbl_letter7 = tk.Label(master=game_UI)
        lbl_letter7.grid(row=1, column=10)
        if Game.session > 2:
            notebook.hide(notebook.select())
        self.__button_alphabet()
        self.__word_letter()

    def __word_letter(self):
        label_list = [lbl_letter1, lbl_letter2, lbl_letter3, lbl_letter4, lbl_letter5, lbl_letter6, lbl_letter7]
        for i in range(len(word)):
            label_list[i]['text'] = "_"

    def __check_button_game(self, butt):
        global x
        global image_of_step1, image_of_step2, image_of_step3, image_of_step4
        image_of_step1 = tk.PhotoImage(file="Step1.png")
        image_of_step2 = tk.PhotoImage(file="Step2.png")
        image_of_step3 = tk.PhotoImage(file="Step3.png")
        image_of_step4 = tk.PhotoImage(file="Step4.png")
        popw = word.lower()
        popw = list(popw)
        label_list = [lbl_letter1, lbl_letter2, lbl_letter3, lbl_letter4, lbl_letter5, lbl_letter6, lbl_letter7]
        if butt["text"] not in popw:
            butt["state"] = "disabled"
            Game.cnt += 1
        else:
            for i in word.lower():
                if i == butt["text"]:
                    a = word.lower().index(i)
                    zapoln = label_list[a]
                    zapoln["text"] = butt['text']
                    butt['state'] = "disabled"
                    if word.lower().count(i) > 1:
                        vv = a+1
                        x = word.lower().index(i, vv)
                        zapoln = label_list[x]
                        zapoln["text"] = butt['text']
                    if word.lower().count(i) > 2:
                        vv = a+1
                        vv += 1
                        c = word.lower().index(i, vv+1)
                        zapoln = label_list[c]
                        zapoln["text"] = butt['text']
        av = Game.cnt
        if av == 1:
            canva.create_image(0, 0, anchor="nw", image=image_of_step1)
        elif av == 2:
            canva.create_image(0, 0, anchor="nw", image=image_of_step2)
        elif av == 3:
            canva.create_image(0, 0, anchor="nw", image=image_of_step3)
        elif av >= 4:
            canva.create_image(0, 0, anchor="nw", image=image_of_step4)
            showerror(title="Висилица", message=f"Вы проиграли! Человек повешен! Загаданное слово: {word}")
            notebook.hide(1)
            notebook.select(0)
            Game.cnt = 0
        zov = ("йёцукенгшщзхъфывапролджэячсмитьбю")
        if lbl_letter7["text"] in zov:
            if lbl_letter6["text"] in zov:
                if lbl_letter5["text"] in zov:
                    if lbl_letter4["text"] in zov:
                        if lbl_letter3["text"] in zov:
                            if lbl_letter2["text"] in zov:
                                if lbl_letter1["text"] in zov:
                                    showinfo(title="Висилица", message="Вы выиграли! Поздравляю!")
                                    notebook.hide(1)
                                    notebook.select(0)
                                    Game.cnt=0
    def __button_alphabet(self):
        letter_a = tk.Button(master=game_UI, text="а", command=lambda: self.__check_button_game(letter_a))
        letter_a.grid(row=3, column=0)
        letter_b = tk.Button(master=game_UI, text="б", command=lambda: self.__check_button_game(letter_b))
        letter_b.grid(row=3, column=1)
        letter_c = tk.Button(master=game_UI, text="в", command=lambda: self.__check_button_game(letter_c))
        letter_c.grid(row=3, column=2)
        letter_d = tk.Button(master=game_UI, text="г", command=lambda: self.__check_button_game(letter_d))
        letter_d.grid(row=3, column=3)
        letter_f = tk.Button(master=game_UI, text="д", command=lambda: self.__check_button_game(letter_f))
        letter_f.grid(row=3, column=4)
        letter_g = tk.Button(master=game_UI, text="е", command=lambda: self.__check_button_game(letter_g))
        letter_g.grid(row=3, column=5)
        letter_q = tk.Button(master=game_UI, text="ё", command=lambda: self.__check_button_game(letter_q))
        letter_q.grid(row=3, column=6)
        letter_w = tk.Button(master=game_UI, text="ж", command=lambda: self.__check_button_game(letter_w))
        letter_w.grid(row=3, column=7)
        letter_e = tk.Button(master=game_UI, text="з", command=lambda: self.__check_button_game(letter_e))
        letter_e.grid(row=3, column=8)
        letter_r = tk.Button(master=game_UI, text="и", command=lambda: self.__check_button_game(letter_r))
        letter_r.grid(row=3, column=9)
        letter_t = tk.Button(master=game_UI, text="й", command=lambda: self.__check_button_game(letter_t))
        letter_t.grid(row=3, column=10)
        letter_y = tk.Button(master=game_UI, text="к", command=lambda: self.__check_button_game(letter_y))
        letter_y.grid(row=3, column=11)

        letter_u = tk.Button(master=game_UI, text="л", command=lambda: self.__check_button_game(letter_u))
        letter_u.grid(row=4, column=0)
        letter_i = tk.Button(master=game_UI, text="м", command=lambda: self.__check_button_game(letter_i))
        letter_i.grid(row=4, column=1)
        letter_o = tk.Button(master=game_UI, text="н", command=lambda: self.__check_button_game(letter_o))
        letter_o.grid(row=4, column=2)
        letter_p = tk.Button(master=game_UI, text="о", command=lambda: self.__check_button_game(letter_p))
        letter_p.grid(row=4, column=3)
        letter_s = tk.Button(master=game_UI, text="п", command=lambda: self.__check_button_game(letter_s))
        letter_s.grid(row=4, column=4)
        letter_h = tk.Button(master=game_UI, text="р", command=lambda: self.__check_button_game(letter_h))
        letter_h.grid(row=4, column=5)
        letter_j = tk.Button(master=game_UI, text="с", command=lambda: self.__check_button_game(letter_j))
        letter_j.grid(row=4, column=6)
        letter_k = tk.Button(master=game_UI, text="т", command=lambda: self.__check_button_game(letter_k))
        letter_k.grid(row=4, column=7)
        letter_l = tk.Button(master=game_UI, text="у", command=lambda: self.__check_button_game(letter_l))
        letter_l.grid(row=4, column=8)
        letter_z = tk.Button(master=game_UI, text="ф", command=lambda: self.__check_button_game(letter_z))
        letter_z.grid(row=4, column=9)
        letter_x = tk.Button(master=game_UI, text="х", command=lambda: self.__check_button_game(letter_x))
        letter_x.grid(row=4, column=10)
        letter_v = tk.Button(master=game_UI, text="ц", command=lambda: self.__check_button_game(letter_v))
        letter_v.grid(row=4, column=11)

        letter_n = tk.Button(master=game_UI, text="ч", command=lambda: self.__check_button_game(letter_n))
        letter_n.grid(row=5, column=0)
        letter_m = tk.Button(master=game_UI, text="ш", command=lambda: self.__check_button_game(letter_m))
        letter_m.grid(row=5, column=1)
        letter_a1 = tk.Button(master=game_UI, text="щ", command=lambda: self.__check_button_game(letter_a1))
        letter_a1.grid(row=5, column=2)
        letter_b1 = tk.Button(master=game_UI, text="ъ", command=lambda: self.__check_button_game(letter_b1))
        letter_b1.grid(row=5, column=3)
        letter_c1 = tk.Button(master=game_UI, text="ы", command=lambda: self.__check_button_game(letter_c1))
        letter_c1.grid(row=5, column=4)
        letter_v1 = tk.Button(master=game_UI, text="ь", command=lambda: self.__check_button_game(letter_v1))
        letter_v1.grid(row=5, column=5)
        letter_q1 = tk.Button(master=game_UI, text="э", command=lambda: self.__check_button_game(letter_q1))
        letter_q1.grid(row=5, column=6)
        letter_w1 = tk.Button(master=game_UI, text="ю", command=lambda: self.__check_button_game(letter_w1))
        letter_w1.grid(row=5, column=7)
        letter_e1 = tk.Button(master=game_UI, text="я", command=lambda: self.__check_button_game(letter_e1))
        letter_e1.grid(row=5, column=8)

    @staticmethod
    def __random_word():
        categorie = vybor.get()
        word = rd.choice(Game.words[Game.categories.index(categorie)])
        return word


class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Висилица")
        self.columnconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], minsize=50)
        self.rowconfigure([0, 1, 2, 3, 4, 5], minsize=50)
        self.reg_widget()
        self.geometry(Game.pix)
        self.resizable(False, False)

    def reg_widget(self):
        game = Game(self)
        game.grid(row=0, column=0)


if __name__ == "__main__":
    app = App()
    app.mainloop()
