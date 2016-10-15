import pyperclip

message = 'this is my secret message '

key = 13

mode = 'encrypt'

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

translated = ''

message = message.upper()

for symbol in message:
    if symbol in LETTERS:
        num = LETTERS.find(symbol) #this function is used to find and return index of value by comparing with symbol with in LETTERS,,,,
                                   #this will return index values of message found in LETTERS just comparing it between LETTERS and message
        #print (LETTERS.find(symbol))
        if mode ==  'encrypt':
            num = num + key #this will add(+) 13 to every value from letters which was obtained from find funtion
            
        elif mode == 'decrypt':
            num = num - key
        if num >= len(LETTERS):
            num = num - len(LETTERS) # this is used when the value exceed the index  obtained by adding 13 (encrypting) to the values 
            print (str(num ) + ' this is if statement')
        elif num < 0:
            num = num + len(LETTERS)
            #print (str(num ) + ' this is elif statement')


        translated = translated + LETTERS[num]

    else:

        translated = translated + symbol


print(translated)

pyperclip.copy(translated)
        
