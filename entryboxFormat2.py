import tkinter as tk
import tkinter.messagebox as tk_mb
import tkinter.ttk as tk_ttk

class Window(tk.Tk):                      
    #docstring
    """(docstring) Classe Fenetre"""
    
    def __init__(self):
        tk.Tk.__init__(self)
        self.entry = EntryBoxFormated(self)
        self.entry2 = EntryBoxFormated(self)
        
        self.entry.entryTkValue.set("0000.1111")
        
        self.entry.pack()
        self.entry2.pack()

#TO DO:  tenir compte des négatifs
#        faire en sorte de selectionner le texte lorsque d'un appui sur tab


class EntryBoxFormated (tk.Entry):          #PRENDRE UN INTERVALLE EN PARAM DE CE WIDGET ( min et max autorisés -> 2 attributs d'instance)
                                            # + une variable pour le nombre de chiffres après la virgule
                                            # ameliorer pour tenir compte des nombres négatifs ??
    #docstring
    """(docstring) Classe Fenetre"""
    
                                                                #precision = nb digits after comma
                                                                #type : "float" or "string", if string no need for validation  "not used now"

    def __init__ (self, root, min=0.0, max=100., precision=3, type=None):  
        self.min = min
        self.max = max
        self.precision = precision
        self.root = root
            
        if (type == None or type != 'string'):
            self.type = "float"
        #self.root = window
        
        self.RealValue = self.initEntryValue()
        self.entryTkValue = self.RealValue
                
        super().__init__(self.root, textvariable = self.entryTkValue, text = self.entryTkValue, validate='focus')
        cmd = self.register(self.entryFloatValidation)
        self.configure(validatecommand=cmd)
        
        self.bind("<Return>", (lambda event: self.entryFloatValidation()))
        self.bind("<KP_Enter>", (lambda event: self.entryFloatValidation()))

    
    def getText(self):
        return self.RealValue
    
    def initEntryValue(self):
        initVal = "0"
        if (self.precision > 0):
            initVal += "."
            for i in range(0,self.precision):
                initVal += "0"
        return tk.StringVar(value=initVal)
    
 
    def entryFloatValidation(self):
        
        """
        Cas : - pas de "." dans la chaine, si c'est que des entiers c'est bon
               - caractères non autorisés
               - plus d'un point
               - chaine correcte mais valeur en dehors de l'intervalle de valeur
               - s'il rentre "," instead of '.', change it
        
        """

        tempString = self.entryTkValue.get()
        n = len(tempString)
        nbPoints = 0
        res = True
        i=0
            
        while (i<n):
            if (tempString[i] < '0' or tempString[i] > '9'):
                if (tempString[i] == ',' or tempString[i] == ';'):
                    tempString = tempString[0:i] + '.' + tempString[i+1:]

                if (tempString[i] == '.'):
                    nbPoints += 1
                    if (nbPoints > 1):
                        res = False
                else:
                    res = False
            i += 1
        
        if (res):                 #correct string, checking if min<value<max
            if (float(tempString) < self.min or float(tempString) > self.max):
                res = False
        
        if (res):                #string correct
            i=0
            test = True
            while(test):
                n = len(tempString)
                if (i<(n-1) and tempString[i]=='0' and tempString[i+1]=='0'):
                    tempString = tempString[1:]
                else:
                    test=False            

            self.RealValue = tempString
            self.delete(0,tk.END)
            self.insert(0,tempString)
        else:
            self.delete(0,tk.END)
            self.insert(0,self.RealValue)
        
        return res
                
    
    def onEnterKey(event=None):
        self.EntryFloatValidation()            




if (__name__ == '__main__'):

    #print(tk.StringVar().configure())
    window = Window()    
    window.mainloop()
    window.quit()
