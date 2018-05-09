import tkinter as tk
import tkinter.messagebox as tk_mb
import tkinter.ttk as tk_ttk


class Window(tk.Tk):
    #docstring
    """(docstring) Classe Fenetre"""
    
    def __init__(self):
        tk.Tk.__init__(self)	# On dérive de Tk, on reprend sa méthode d'instanciation
        
        self.selectedItem = tk.StringVar()
        
        self.fruitSelect = tk.StringVar()
        self.fruitList = ('pomme','banane','ananas')
        
        self.labelframe = tk.LabelFrame(self, text='Pane1', width=100, height=100)
        self.fruitCombo = self.initCombobox(self.labelframe, self.selectedItem, self.fruitList, 'readonly')
        
        #self.fruitCombo.bind('<<ComboboxSelected>>', self.on_selection)  #works
        
        #self.fruitCombo.bind('<<ComboboxSelected>>', self.on_selection2(self.labelTest))
        
        self.labelTest= tk.Label(self.labelframe, text = "selected : ")
        
        #self.fruitCombo.bind('<<ComboboxSelected>>', self.on_selection2(self.labelTest)) #doesn't work
        
        
        self.fruitCombo.grid()
        self.labelTest.grid()
        
        self.labelframe.pack()
    
    
    def on_selection(self, event=None):  # Just to test
        self.labelTest.configure(text="selected : " + self.selectedItem.get())
        
    def on_selection2(self, label, event=None):  # Just to test
        label.configure(text="selected : " + self.selectedItem.get())
        
    def print_selection(self, event=None):  # Just to test
        print (self.selectedItem.get())
        
    def initCombobox(self, root, varType, listOfAttributes, visibilityState):
        
        return tk_ttk.Combobox(root, textvariable = varType, values = listOfAttributes, state = visibilityState)
        

if (__name__ == '__main__'):
            
    window = Window()
    window.mainloop()
    window.quit()