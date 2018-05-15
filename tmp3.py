Tkinter : Can't get register function to work


Hi, after a lot of research, I come to you for help.
On the Entry Wdiget from tkinter, there is a validatecommand option you can pass. The documentation seem to say that the function you pass as argument first needs to be registered via the .register() function so it can become a callback function.

Here's what I found : http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/entry-validation.html

So it should be something like this :  


----------  

    import tkinter as tk
    
    
    class Window(tk.Tk):
    
        def __init__(self):
            tk.Tk.__init__(self)
            self.entry = EntryBoxFormated()
            self.entry.pack()

----------  

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

----------  

    if (__name__ == '__main__'):
        window = Window()    
        window.mainloop()
        window.quit()

----------  

But with this, I get this error :

> Traceback (most recent call last):
  File "/home/aubin/PyzoWorkspace/Interface/TESTS/topic.py", line 75, in <module>
    window = Window()
  File "/home/aubin/PyzoWorkspace/Interface/TESTS/topic.py", line 9, in __init__
    self.entry = EntryBoxFormated()
  File "/home/aubin/PyzoWorkspace/Interface/TESTS/topic.py", line 28, in __init__
    cmd = self.register(self.entryFloatValidation)
  File "/home/aubin/anaconda3/lib/python3.6/tkinter/__init__.py", line 1366, in _register
    self.tk.createcommand(name, f)
AttributeError: 'EntryBoxFormated' object has no attribute 'tk'  


If I skip the call to register in the init() of the class EntryBoxFormated, I don't get any erro but the window doesn't show.

Am I forgeting anything ?

Thanks in advance. 



Edit : you marked it as the same question as another topic but i actually call the constructor of the mother class and i can't switch the last two lines of the constructor of the class EntryBoxFormated.
Is there a way to pass around that.