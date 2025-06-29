** start of main.py **

def number_pattern(n):
    string=''
    if not isinstance (n,int):
        return 'Argument must be an integer value.'
    if n<1:
        return 'Argument must be an integer greater than 0.' 
    else:
        for i in range (1,n+1):
           string+=str(i)+' '
        return string.strip()        
print(number_pattern(4))       

** end of main.py **

