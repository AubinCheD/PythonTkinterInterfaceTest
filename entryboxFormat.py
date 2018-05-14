import tkinter as tk
import tkinter.messagebox as tk_mb
import tkinter.ttk as tk_ttk

class Window(tk.Tk):                          #PRENDRE UN INTERVALLE EN PARAM DE CE WIDGET ( min et max autorisés -> 2 attributs d'instance)
                                            # + une variable pour le nombre de chiffres après la virgule
    #docstring
    """(docstring) Classe Fenetre"""
    
    def __init__(self, min=None, max=None, precision=None):  #precision = nb digits after comma
        tk.Tk.__init__(self)	       # On dérive de Tk, on reprend sa méthode d'instanciation
        
        if (min == None):
            self.min = 0
        if (max == None):
            self.max = 10
        if (precision == None):
            precision = 4    
        
        self.entryTkValue = tk.StringVar(value="0000.0000")
        #self.entryTkTtkValue = tk.StringVar()
        
        self.entryTk = tk.Entry(self, textvariable = self.entryTkValue, text = self.entryTkValue, validate=tk.ALL, validatecommand = {})
        
        #self.entryTkTtk = tk.Entry(self, textvariable = self.entryTkTtkValue, text = self.entryTkTtkValue)
        
        #print(self.entryTk.get())
        
        
        #POUR UPDATE, FAIRE UN DELETE PUIS UN INSERT ou FAIRE UN SET SUR LA VARIABLE
        
        #self.entryTk.delete(0, tk.END) #deletes the current value
        #self.entryTk.insert(0, "0000.1111")
        
        #self.entryTkValue.set("0000.1111")
        
        
        
        #self.entryTk.configure(textvariable = "0000.1111")
        #print(self.entryTk.get())
        #self.entryTk["textvariable"] = "0000.1111"    ##WORKS
        
        
        #print(self.entryTk["textvariable"])
        
        self.entryTk.pack()
        
        
        #print(self.entryTkTtk.get())
        #self.entryTkTtk.configure(textvariable = "0000.0000")
        #print(self.entryTkTtk.get())
        
        #self.entryTkTtk.pack()
        

 
    def entryFloatValidation(self):
        
        """
        Cas : - pas de "." dans la chaine, si c'est que des entiers c'est bon
               - caractères non autorisés
               - plus d'un point
               - chaine correcte mais valeur en dehors de l'intervalle de valeur
               - s'il rentre "," instead of '.', change it
        
        """
        n = len(string)
        nbPoints = 0
        res = True
        
        """for i in range (0,n):
            if (string[i] < '0' and string[i] > '9'):
                res = False
          """  
            
        while (i<n):
            if (string[i] < '0' and string[i] > '9'):
                if (string[i] == ',' or string[i] == ';'):
                    string[i] == '.'

                if (string[i] == '.'):
                    nbPoints += 1
                    if (nbPoints > 1):
                        res = False
                else:
                    res = False
            
 

if (__name__ == '__main__'):
    
    window = Window()    
    window.mainloop()
    window.quit()
    
    
