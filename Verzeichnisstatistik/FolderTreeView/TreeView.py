from tkinter import *
from sys import platform

class TreeView:

    X_Verschiebung_Line = 40
    Y_Verschiebeung_Line = 30
    X_Verschiebung_Text = 17
    Y_Verschiebeung_Text = 30

    file_seperator = "/"

    def __init__(self, canvas):
        self.__folders = {}
        self.canvas = canvas
        self.X = 10
        self.Y = 50

        if "win" in platform.lower():
            TreeView.file_seperator = "\\"

        self.image = PhotoImage(file=".."+ TreeView.file_seperator +"Images"+ TreeView.file_seperator +"Ordner.png")

    def get_folders(self):
        return self.__folders

    def set_directory(self, dir):
        self.__dir = dir

    def get_folder_information(self, name):
        root = Tk()
        scroll = Scrollbar(root)
        text = Text(root)
        scroll.pack(side=RIGHT, fill=BOTH)
        text.pack(side=LEFT, fill=BOTH)
        scroll.config(command=text.yview)
        text.config(yscrollcommand=scroll.set)

        text.insert(END, self.__folders.get(name))

        root.mainloop()

    def set_folder_informations(self, name, content):
        self.__folders[name] = content
        new_x = self.X + TreeView.X_Verschiebung_Line
        new_y = self.Y + TreeView.Y_Verschiebeung_Line
        self.canvas.create_line([self.X, self.Y, new_x, self.Y], fill="#476042")
        self.canvas.create_text(new_x + TreeView.X_Verschiebung_Text, self.Y - TreeView.Y_Verschiebeung_Text,
                                text=name.rsplit('\\', 1)[1])

        self.canvas.create_image(new_x + TreeView.X_Verschiebung_Text, self.Y, image=self.image, tag=name)

        self.canvas.create_line([self.X, self.Y, new_x, self.Y], fill="#476042")

        self.X = new_x
        self.Y = new_y


