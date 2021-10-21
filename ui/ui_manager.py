from tkinter import *
from tkinter import ttk, filedialog, messagebox
from tkinter import LEFT, RIGHT, BOTH, RAISED
from crawling_manager import CrawlingManager
from ui.ui_option import UIOption
import os

class UIManager:
    def __init__(self):
        pass

    def show(self):
        window = Tk()

        window.title("서점 크롤링")
        window.geometry("600x390+100+100")

        frame1 = Frame(window, relief=RAISED, borderwidth=1)
        frame1.pack(fill=BOTH)
        frame2 = Frame(window, relief=RAISED)
        frame2.pack(fill=BOTH)
        frame3 = Frame(window, relief=RAISED)
        frame3.pack(fill=BOTH)
        frame4 = Frame(window, relief=RAISED)
        frame4.pack(fill=BOTH)
        frame5 = Frame(window, relief=RAISED)
        frame5.pack(fill=BOTH)

        self.text_box = Text(frame1, height=20)
        self.text_box.pack(fill='both')

        label1 = Label(frame2, text='저장위치')
        label1.pack(side="left", padx=10)
        label2 = Label(frame3, text='파일명')
        label2.pack(side="left", padx=10)
        label3 = Label(frame4, text='키워드 강조')
        label3.pack(side="left", padx=10)

        btn_path = Button(frame2, width=5, text="저장경로", command=self.do_path)
        btn_path.pack(side="right", padx=(0,5))

        self.file_path = StringVar()
        self.file_path.set(os.path.join(os.path.expanduser('~'),'Desktop'))
        textbox = ttk.Entry(frame2, width=45, textvariable=self.file_path)
        textbox.pack(side="right")

        self.file_name = StringVar()
        self.file_name.set("서점별_베스트_순위_현황.xlsx")
        textbox = ttk.Entry(frame3, width=54, textvariable=self.file_name)
        textbox.pack(side="right", padx=(0,5))

        self.highlight_keyword = StringVar()
        self.highlight_keyword.set("윌북,키워드1,키워드2")
        textbox = ttk.Entry(frame4, width=54, textvariable=self.highlight_keyword)
        textbox.pack(side="right", padx=(0, 5))

        self.detail_info = BooleanVar()
        self.detail_info.set(False)
        checkbox = Checkbutton(frame5, text='세부 페이지 추가 정보추출 (시간걸림)', var=self.detail_info)
        checkbox.pack(side="left", pady=5, padx=(5,0))

        btn_stop = Button(frame5, width=10, text="중지", command=self.do_stop)
        btn_stop.pack(side="right", pady=5, padx=(0,5))

        btn_start = Button(frame5, width=10, text="시작", command=self.do_crawling)
        btn_start.pack(side="right", pady=5, padx=(0,5))

        window.mainloop()

    def do_crawling(self):
        _file_path = self.file_path.get()
        _file_name = self.file_name.get()
        _ui_option = UIOption(self.file_path.get(), self.file_name.get(), self.detail_info.get(), self.highlight_keyword.get())

        if _file_path and _file_name:
            CrawlingManager.start(_ui_option)
        else:
            messagebox.showinfo("안내", "파일저장 위치를 선택하고 파일명을 입력해 주세요!")

    def do_stop(self):
        CrawlingManager.stop()

    def do_path(self):
        self.file_path.set(filedialog.askdirectory())

    def fn_update_callback(self, text):
        self.text_box.insert(INSERT, text+"\n")