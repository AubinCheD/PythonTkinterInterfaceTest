import tkinter as tk

class Window(tk.Tk):                      
    
    def __init__(self):
        tk.Tk.__init__(self)
        self.entry = EntryBoxFormated()
        self.entry.pack()

        
class EntryBoxFormated (tk.Entry):

    def __init__ (self, min=None, max=None, precision=None, type=None):   

        if (min == None):
            self.min = 0
        if (max == None):
            self.max = 10
        if (precision == None):
            self.precision = 4
        if (type == None or type != 'string'):
            self.type = "float" 
        
        self.entryTkValue = self.initEntryValue()
        
        cmd = self.register(self.entryFloatValidation)        
        super().__init__(textvariable = self.entryTkValue, text = self.entryTkValue, validate=tk.ALL, validatecommand = cmd)  
        
    
    def initEntryValue(self):
        initVal = "0"
        if (self.precision > 0):
            initVal += "."
            for i in range(0,self.precision):
                initVal += "0"
        return tk.StringVar(value=initVal)
    
 
    def entryFloatValidation(self):

        tempString = self.entryTkValue.get()
        n = len(tempString)
        print(n)
        nbPoints = 0
        res = True
        i=0
            
        while (i<n):
            if (tempString[i] < '0' or tempString[i] > '9'):
                if (tempString[i] == ',' or tempString[i] == ';'):
                    tempString[i] == '.'

                if (tempString[i] == '.'):
                    nbPoints += 1
                    if (nbPoints > 1):
                        res = False
                else:
                    res = False
        
        if (res):
            if (float(tempString) < self.min or float(tempString) > self.max):
                res = False
            else:
                self.delete(0,tk.END)
                self.insert(0,tempString)

        return res
                
                
                

if (__name__ == '__main__'):
    window = Window()    
    window.mainloop()
    window.quit()
    
    

        #super().register(self.entryFloatValidation)

cmd = self.register(self.entryFloatValidation)
        
        
        #self.entryTk = tk.Entry(self, textvariable = self.entryTkValue, text = self.entryTkValue, validate=tk.ALL, validatecommand = {})
        #super().__init__(textvariable = self.entryTkValue, text = self.entryTkValue, validate=tk.ALL, validatecommand = self.register(self.entryFloatValidation) ) #, validatecommand = self.entryFloatValidation
  
  
cmd = self.register(self.entryFloatValidation)      
super().__init__(textvariable = self.entryTkValue, text = self.entryTkValue, validate=tk.ALL, validatecommand = cmd) 


super().__init__(textvariable = self.entryTkValue, text = self.entryTkValue, validate=tk.ALL, validatecommand = self.entryFloatValidation)