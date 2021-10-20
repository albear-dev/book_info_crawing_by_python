from tkinter import *
from tkinter import ttk, filedialog, messagebox
from tkinter import LEFT, RIGHT, BOTH, RAISED
from crawling_manager import CrawlingManager
import os

class UIManager:
    def __init__(self):
        pass

    def show(self):
        window = Tk()

        window.title("서점 크롤링")
        window.geometry("600x420+100+100")

        frame1 = Frame(window, relief=RAISED, borderwidth=1)
        frame1.pack(fill=BOTH)
        frame2 = Frame(window, relief=RAISED)
        frame2.pack(fill=BOTH)
        frame3 = Frame(window, relief=RAISED)
        frame3.pack(fill=BOTH)
        frame4 = Frame(window, relief=RAISED)
        frame4.pack(fill=BOTH)

        self.text_box = Text(frame1)
        self.text_box.pack(fill='both')

        label1 = Label(frame2, text='저장위치')
        label1.pack(side="left", padx=10)
        label2 = Label(frame3, text='파일명')
        label2.pack(side="left", padx=10)

        btn_path = Button(frame2, width=5, text="저장경로", command=self.do_path)
        btn_path.pack(side="right")

        self.file_path = StringVar()
        self.file_path.set(os.path.join(os.path.expanduser('~'),'Desktop'))
        textbox = ttk.Entry(frame2, width=45, textvariable=self.file_path)
        textbox.pack(side="right")



        self.file_name = StringVar()
        self.file_name.set("서점별_베스트_순위_현황.xlsx")
        textbox = ttk.Entry(frame3, width=54, textvariable=self.file_name)
        textbox.pack(side="right")

        btn_stop = Button(frame4, width=10, text="중지", command=self.do_stop)
        btn_stop.pack(side="right", pady=5)

        btn_start = Button(frame4, width=10, text="시작", command=self.do_crawling)
        btn_start.pack(side="right", pady=5)

        window.mainloop()

    def do_crawling(self):
        _file_path = self.file_path.get()
        _file_name = self.file_name.get()

        if _file_path and _file_name:
            CrawlingManager.start(self.fn_update_callback, _file_path, _file_name)
        else:
            messagebox.showinfo("안내", "파일저장 위치를 선택하고 파일명을 입력해 주세요!")

    def do_stop(self):
        CrawlingManager.stop()

    def do_path(self):
        self.file_path.set(filedialog.askdirectory())

    def fn_update_callback(self, text):
        self.text_box.insert(INSERT, text+"\n")