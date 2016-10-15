count=0
print("enter a name to get the vowels in it")
name=input()
for letters in name:
    if(letters in['a','e','i','o','u']):
       count=count+1
print ("you have " +str(count)+ 'vowel in name')
