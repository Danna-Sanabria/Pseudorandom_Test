import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


class Frame:
    def __init__(self, control):
        self.control = control
        self.mywindow = tk.Tk()
        self.mywindow.geometry("1080x980")
        self.mywindow.title("PRUEBAS # PSEUDOALEATORIOS")
        self.mywindow.resizable(False,False)
        self.mywindow.config(background = "#F2F2F0")
        main_title = tk.Label(text = "PRUEBAS DE NÚMEROS PSEUDOALEATORIOS", anchor=tk.CENTER, font = ("Georgia", 26), bg = "#F2F2F0", fg = "#F06E3E", width = "500", height = "2")
        main_title.pack()
        self.selected_option = tk.StringVar()
        self.selected_file = tk.StringVar()
        self.x1=22
        self.y1=190
        self.labels = []
        self.initComponents()
    
    def initComponents(self):
        select_file_lbl = tk.Label(text = "Seleccione los números a probar", font = ("Georgia", 17))
        select_file_lbl.place(x = 400, y = 100)

        # self.graphic_lbl = tk.Label(text = "NUMBERS DISTRIBUTION", bg = "#FFEEDD")
        # self.graphic_lbl.place(x = 470, y = 147)

        browse_button = tk.Button(self.mywindow, text="Adjuntar", command=self.browseFiles, width=15, height=2, bg="#025959",fg="white" , font = ("Georgia", 12) , highlightbackground="#FF0000", highlightthickness=2)
        browse_button.place(x=500 , y=147)

        select_test = tk.Label(text = "Seleccione la prueba a realizar", font = ("Georgia", 17))
        select_test.place(x = 381, y = 302)

        self.meanTest_button = tk.Button(self.mywindow, text="Prueba de medias", command=self.control.meanTest, width=18, height=2, bg="#5c9b9b", fg="black", font=("Georgia", 12), bd=2)
        self.meanTest_button.place(x=100, y=358)

        self.VarianceTest = tk.Button(self.mywindow, text="Prueba de varianza", command=self.control.varianceTest, width=18, height=2, bg="#5c9b9b",fg="black" , font = ("Georgia", 12), bd=1.5)
        self.VarianceTest.place(x=278 , y=358 )

        self.KSTest = tk.Button(self.mywindow, text="Prueba de KS", command=self.control.KSTest, width=18, height=2, bg="#5c9b9b",fg="black" , font = ("Georgia", 12), bd=1.5)
        self.KSTest.place(x=456 , y=358)

        self.Chi2Test = tk.Button(self.mywindow, text="Prueba de Chi2", command=self.control.Chi2Test, width=18, height=2, bg="#5c9b9b",fg="black" , font = ("Georgia", 12), bd=1.5)
        self.Chi2Test.place(x=634 , y=358)

        self.PokerTest = tk.Button(self.mywindow, text="Prueba de Poker", command=self.control.PokerTest, width=18, height=2, bg="#5c9b9b",fg="black" , font = ("Georgia", 12), bd=1.5)
        self.PokerTest.place(x=812 , y=358)


    def buttonVerificacion(self, color, x, y):
        test_button = tk.Button(self.mywindow, command=self.control.meanTest, width=18, height=3, bg=color, bd=1.5)
        test_button.place(x, y)
        
    def browseFiles(self):
        file = filedialog.askopenfilename()
        self.selected_file = file
        self.path_lbl = tk.Label(text = file, bg = "#FFEEDD", fg="black" , font = ("Georgia", 9), )
        self.path_lbl.place(x = 325, y = 210)

    #get the selected file path
    def getFilePath(self):
        return self.selected_file
    
    #gets the selected option
    def getSelectedOption(self):
        return self.selected_option.get()

    #Allows clean the frame to show other labels 
    def destroyAlllbls(self):
        for label in self.labels:
            label.destroy()
        self.x1 = 22
        self.y1 = 190
        self.mywindow.update()
    
    #Cuts the string if it is too long
    def cutString(self,cadena):
        # If the string is shorter than 200 characters, it is returned as-is.
        if len(cadena) <= 60:
            return cadena
        # If the string is longer than 200 characters, it is split into 200-character parts with newlines
        partes = []
        i = 0
        while i < len(cadena):
            partes.append(cadena[i:i+60])
            i += 60
        return '\n'.join(partes) #finally join the parts with a line break

    #Allows create a new label to show information
    def generateLbl(self, labelname, x, y, extraHeight=0):
        new_lbl = tk.Label(text=self.cutString(labelname), font=("Georgia", 13))
        new_lbl.place(x=x, y=y)
        self.labels.append(new_lbl)
        self.y1 = y + 100 + extraHeight
        self.mywindow.update()
        return new_lbl

    def messageAlert(message):
        messagebox.showinfo("Alerta", message)

    