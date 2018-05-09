import tkinter as tk
import tkinter.messagebox as tk_mb
import tkinter.ttk as tk_ttk


class Window(tk.Tk):
    #docstring
    """(docstring) Classe Fenetre"""
    
    def __init__(self):
        tk.Tk.__init__(self)	# On dérive de Tk, on reprend sa méthode d'instanciation
        
        self.fruitSelect = tk.StringVar()
        self.fruitList = ('pomme','banane','ananas')
        #self.fruitCombo = tk_ttk.Combobox(self, textvariable = self.fruitSelect, values = self.fruitList, state = 'readonly')
        
        #self.fruitCombo = self.initCombobox(self, tk.StringVar(), self.fruitList, 'readonly')
        self.labelframe = tk.LabelFrame(self, text='Pane1', width=100, height=100)
        
        
        self.fruitCombo = self.initCombobox(self.labelframe, tk.StringVar(), self.fruitList, 'readonly')
        
        self.fruitCombo.grid()
        
        self.labelframe.pack()
        
        
        
    def initCombobox(self, root, varType, listOfAttributes, visibilityState):
        
        return tk_ttk.Combobox(root, textvariable = varType, values = listOfAttributes, state = visibilityState)
        

if (__name__ == '__main__'):
            
    window = Window()
    window.mainloop()
    window.quit()