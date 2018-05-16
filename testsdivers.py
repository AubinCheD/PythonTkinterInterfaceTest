def modifString(string):
    n = len(string)
    i=0
    while (i<n):
        if (string[i]==';' or string[i]==','):
            string = string[0:i] + '.' + string[i+1:]
        i += 1
    return string

if (__name__ == '__main__'):
    
    string = ";1;21,azierf"
    print(string)
    #string = string[0:1] + '.' + string[2:]
    string = modifString(string)
    print(string)