import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("ANTIVIRUS GUI")
        #setting window size
        width=880
        height=450
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_986=tk.Button(root)
        GButton_986["bg"] = "#85ffff"
        ft = tkFont.Font(family='Times',size=13)
        GButton_986["font"] = ft
        GButton_986["fg"] = "#000000"
        GButton_986["justify"] = "center"
        GButton_986["text"] = "PROTECTION"
        GButton_986.place(x=50,y=240,width=174,height=185)
        GButton_986["command"] = self.GButton_986_command

        GButton_437=tk.Button(root)
        GButton_437["bg"] = "#85ffff"
        ft = tkFont.Font(family='Times',size=13)
        GButton_437["font"] = ft
        GButton_437["fg"] = "#000000"
        GButton_437["justify"] = "center"
        GButton_437["text"] = "PRIVACY"
        GButton_437.place(x=250,y=240,width=174,height=185)
        GButton_437["command"] = self.GButton_437_command

        GButton_924=tk.Button(root)
        GButton_924["bg"] = "#25d1eb"
        ft = tkFont.Font(family='Times',size=10)
        GButton_924["font"] = ft
        GButton_924["fg"] = "#000000"
        GButton_924["justify"] = "center"
        GButton_924["text"] = "SETTINGS"
        GButton_924.place(x=670,y=360,width=113,height=48)
        GButton_924["command"] = self.GButton_924_command

        GButton_856=tk.Button(root)
        GButton_856["bg"] = "#85ffff"
        ft = tkFont.Font(family='Times',size=13)
        GButton_856["font"] = ft
        GButton_856["fg"] = "#000000"
        GButton_856["justify"] = "center"
        GButton_856["text"] = "TOOLS"
        GButton_856.place(x=450,y=240,width=174,height=185)
        GButton_856["command"] = self.GButton_856_command

        GButton_230=tk.Button(root)
        GButton_230["bg"] = "#25d1eb"
        ft = tkFont.Font(family='Times',size=10)
        GButton_230["font"] = ft
        GButton_230["fg"] = "#000000"
        GButton_230["justify"] = "center"
        GButton_230["text"] = "QUICK SCAN"
        GButton_230.place(x=670,y=130,width=113,height=48)
        GButton_230["command"] = self.GButton_230_command

        GButton_50=tk.Button(root)
        GButton_50["bg"] = "#25d1eb"
        ft = tkFont.Font(family='Times',size=10)
        GButton_50["font"] = ft
        GButton_50["fg"] = "#000000"
        GButton_50["justify"] = "center"
        GButton_50["text"] = "UPDATE"
        GButton_50.place(x=670,y=200,width=113,height=48)
        GButton_50["command"] = self.GButton_50_command

        GButton_494=tk.Button(root)
        GButton_494["bg"] = "#25d1eb"
        ft = tkFont.Font(family='Times',size=10)
        GButton_494["font"] = ft
        GButton_494["fg"] = "#000000"
        GButton_494["justify"] = "center"
        GButton_494["text"] = "OPTIMIZE"
        GButton_494.place(x=670,y=280,width=113,height=48)
        GButton_494["command"] = self.GButton_494_command

        GMessage_657=tk.Message(root)
        GMessage_657["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times',size=18)
        GMessage_657["font"] = ft
        GMessage_657["fg"] = "#333333"
        GMessage_657["justify"] = "center"
        GMessage_657["text"] = "You are protected!"
        GMessage_657.place(x=50,y=50,width=571,height=124)

        GMessage_604=tk.Message(root)
        GMessage_604["bg"] = "#fffefe"
        ft = tkFont.Font(family='Times',size=13)
        GMessage_604["font"] = ft
        GMessage_604["fg"] = "#333333"
        GMessage_604["justify"] = "center"
        GMessage_604["text"] = "The system is safe."
        GMessage_604.place(x=50,y=180,width=262,height=36)

        GButton_440=tk.Button(root)
        GButton_440["bg"] = "#f8e9e9"
        ft = tkFont.Font(family='Times',size=8)
        GButton_440["font"] = ft
        GButton_440["fg"] = "#000000"
        GButton_440["justify"] = "center"
        GButton_440["text"] = "PROFILE  "
        GButton_440.place(x=10,y=10,width=70,height=25)
        GButton_440["command"] = self.GButton_440_command

        GButton_359=tk.Button(root)
        GButton_359["anchor"] = "nw"
        GButton_359["bg"] = "#fc8080"
        GButton_359["disabledforeground"] = "#000000"
        ft = tkFont.Font(family='Times',size=10)
        GButton_359["font"] = ft
        GButton_359["fg"] = "#000000"
        GButton_359["justify"] = "center"
        GButton_359["text"] = "X"
        GButton_359.place(x=820,y=10,width=33,height=30)
        GButton_359["command"] = self.GButton_359_command

        GButton_59=tk.Button(root)
        GButton_59["bg"] = "#f8e9e9"
        ft = tkFont.Font(family='Times',size=10)
        GButton_59["font"] = ft
        GButton_59["fg"] = "#000000"
        GButton_59["justify"] = "center"
        GButton_59["text"] = "_"
        GButton_59.place(x=770,y=10,width=33,height=30)
        GButton_59["command"] = self.GButton_59_command

    def GButton_986_command(self):
        print("command")


    def GButton_437_command(self):
        print("command")


    def GButton_924_command(self):
        print("command")


    def GButton_856_command(self):
        print("command")


    def GButton_230_command(self):
        print("command")


    def GButton_50_command(self):
        print("command")


    def GButton_494_command(self):
        print("command")


    def GButton_440_command(self):
        print("command")


    def GButton_359_command(self):
        print("command")


    def GButton_59_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
