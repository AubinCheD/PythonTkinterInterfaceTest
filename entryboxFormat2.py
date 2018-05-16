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
        
class EntryBoxFormated (tk.Entry):          #PRENDRE UN INTERVALLE EN PARAM DE CE WIDGET ( min et max autorisés -> 2 attributs d'instance)
                                            # + une variable pour le nombre de chiffres après la virgule
                                            # ameliorer pour tenir compte des nombres négatifs ??
    #docstring
    """(docstring) Classe Fenetre"""
    

    def __init__ (self, min=None, max=None, precision=None, type=None):  #precision = nb digits after comma       #??, window=None, 
                                                                #type : "float" or "string", if string no need for validation
        if (min == None):
            self.min = 0.1
        '''else:
            self.min = min'''
        if (max == None):
            self.max = 10
        '''else:
            self.max = max'''
        if (precision == None):
            self.precision = 4
        if (type == None or type != 'string'):
            self.type = "float"
        #self.root = window
        
        self.RealValue = self.initEntryValue()
        self.entryTkValue = self.RealValue
                
        super().__init__(textvariable = self.entryTkValue, text = self.entryTkValue, validate='focus')
        cmd = self.register(self.entryFloatValidation)
        self.configure(validatecommand=cmd)
        
                                                        #when enter button pressed and entry is beeing focused
        
        #self.config(command=self.entryFloatValidation)
        #self.bind('<Return>',self.entryFloatValidation())
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
        """for item in self.keys():
            print(item)
            print(self.cget(item))
        """
        """
        print('before   ' + self.cget('text'))
        print('before' + self.get())
        print('before' + self.entryTkValue.get())
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
        
        if (res):
            """if (float(tempString) < self.min or float(tempString) > self.max):
                res = False
            else:
                self.delete(0,tk.END)
                self.insert(0,tempString)"""
            self.RealValue = tempString
            self.delete(0,tk.END)
            self.insert(0,tempString)

        else:
            self.delete(0,tk.END)
            self.insert(0,self.RealValue)
        #print(self.entryTkValue.get())
        #self.configure(text=self.entryTkValue)
        #self.root.update()
        
        print('after' + self.get())
        print('after' + self.entryTkValue.get())
        
        return res
                
    
    def onEnterKey(event=None):
        self.EntryFloatValidation()            
    
                

if (__name__ == '__main__'):
    
    #print(tk.StringVar().configure())
    window = Window()    
    window.mainloop()
    window.quit()
