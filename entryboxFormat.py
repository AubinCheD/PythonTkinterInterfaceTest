import tkinter as tk
import tkinter.messagebox as tk_mb
import tkinter.ttk as tk_ttk

class Window(tk.Tk):
    #docstring
    """(docstring) Classe Fenetre"""
    
    def __init__(self):
        tk.Tk.__init__(self)	# On dérive de Tk, on reprend sa méthode d'instanciation
        
        self.entryTkValue = tk.StringVar(value="0000.0000")
        self.entryTkTtkValue = tk.StringVar()
        
        self.entryTk = tk.Entry(self, textvariable = self.entryTkValue, text = self.entryTkValue)
        self.entryTkTtk = tk.Entry(self, textvariable = self.entryTkTtkValue, text = self.entryTkTtkValue)
        
        print(self.entryTk.get())
        self.entryTk.configure(textvariable = "0000.0000")
        print(self.entryTk.get())
        
        self.entryTk.pack()
        
        
        print(self.entryTkTtk.get())
        self.entryTkTtk.configure(textvariable = "0000.0000")
        print(self.entryTkTtk.get())
        
        self.entryTkTtk.pack()
        

 

if (__name__ == '__main__'):
    
    window = Window()    
    window.mainloop()
    window.quit()