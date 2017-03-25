from tkinter import *
from FolderStatistic import *
from FolderTreeView.TreeView import TreeView
import tkinter.filedialog, threading




class FolderTree():

    def __init__(self):

        threading.Event.__init__(self)
        self.__folder_stats = FolderStats(self.process_is_finished)
        self.connected =threading.Event

        root = Tk()
        root.title = "Verzeichnisstatistik"
        root.minsize(width=666, height=666)

        menu = Menu(root)
        root.config(menu=menu)

        start = Menu(menu)
        menu.add_cascade(label="Start", menu=start)
        start.add_command(label="Connect", command=self.__save_path)
        start.add_command(label="Speichern", command=self.speichern)

        frame_but = Frame()

        start_but = Button(frame_but, state=DISABLED, text="Start", command=self.__start_process)
        start_but.pack(side=LEFT, padx=5)

        pause_but = Button(frame_but, state=DISABLED, text="Pause", command=self.__pause_process)
        pause_but.pack(side=LEFT, padx=5)

        continue_but = Button(frame_but, state=DISABLED, text="Weiter", command=self.__continue_process)
        continue_but.pack(side=LEFT, padx=5)

        stop_but = Button(frame_but, state=DISABLED, text="Stop", command=self.__stop_process)
        stop_but.pack(side=LEFT, padx=5)

        ausgabe_but = Button(frame_but, state=DISABLED, text="Ausgabe", command=self.__show_folder_stats)
        ausgabe_but.pack(side=LEFT, padx=5)

        frame_but.pack(fill=X, pady=5)

        self.__buttons = [start_but, pause_but, continue_but, stop_but, ausgabe_but]

        frame_text = Frame()
        scroll = Scrollbar(frame_text)
        text = Text(frame_text, state=DISABLED)
        scroll.pack(side=RIGHT, fill=Y)
        text.pack(fill=BOTH, expand=1)
        scroll.config(command=text.yview)
        text.config(yscrollcommand=scroll.set)

        self.__text_field = text

        frame_text.pack(fill=BOTH, expand=1)
        frame_status = Frame(height=10)

        status = StringVar()
        status.set("Status: " + str(self.__folder_stats.status))
        self.__status_var = status

        label_analse = Label(frame_status, textvariable=status)
        label_analse.pack(side=RIGHT)

        frame_status.pack(side=BOTTOM, fill=X)

        self.__root = root

    def speichern(self):
        if self.__folder_stats.status == Status.Finished:
            with open("FolderStats.txt", "w") as file:
                for fold in self.__folder_stats.get_folders():
                    file.write(str(fold) + "\n")

    def process_is_finished(self):
        if self.__folder_stats.status == Status.Finished:
            self.__status_var.set("Status: " + str(self.__folder_stats.status))
            self.__text_field["state"] = NORMAL
            self.__text_field.delete("1.0", END)
            for folder in self.__folder_stats.get_folders():
                self.__text_field.insert(END, str(folder) + "\n")
            self.__text_field["state"] = DISABLED

    def __start_process(self):
        if self.__folder_stats.status != Status.Running and self.__folder_stats.status != Status.Finished and\
                        self.__folder_stats.status != Status.Paused:
            self.__folder_stats.start()
            self.__status_var.set("Status: " + str(self.__folder_stats.status))

    def __pause_process(self):
        if self.__folder_stats.status == Status.Running:
            self.__folder_stats.pause()
            self.__status_var.set("Status: " + str(self.__folder_stats.status))

    def __continue_process(self):
        if self.__folder_stats.status == Status.Paused:
            self.__folder_stats.resume()
            self.__status_var.set("Status: " + str(self.__folder_stats.status))

    def __stop_process(self):
        if self.__folder_stats.status == Status.Running or self.__folder_stats.status == Status.Paused:
            self.__folder_stats.stop()
            self.__status_var.set("Status: " + str(self.__folder_stats.status))

            self.__text_field["state"] = NORMAL
            self.__text_field.delete("1.0", END)
            for folder in self.__folder_stats.get_folders():
                self.__text_field.insert(END, str(folder) + "\n")
            self.__text_field["state"] = DISABLED


    def __show_folder_stats(self):
        self.__text_field["state"] = NORMAL
        self.__text_field.delete("1.0", END)
        for folder in self.__folder_stats.get_folders():
            self.__text_field.insert(END, str(folder) + "\n")
        self.__text_field["state"] = DISABLED


    def __save_path(self):
            directory = tkinter.filedialog.askdirectory(title="Zielordner auswählen", mustexist=True)
            self.__folder_stats.connect(directory)
            self.__show_buttons()
            self.dir = directory

    def __show_buttons(self):
        if self.__folder_stats.status == Status.Connected:
            self.__status_var.set("Status: " + str(self.__folder_stats.status))
            for but in self.__buttons:
                but["state"] = NORMAL


    def drawCanvas(self):
        pass



    def show(self):
        self.__root.mainloop()


tf = FolderTree()
tf.show()


