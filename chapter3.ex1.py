string=input()
string=string.lower()
vowels=['a','A','e','E', 'i', 'I', 'O','o','u','U']
result=''
for i in range(len(string)):
    if string[i] not in vowels:
        result=result+string[i]
string=result
#print(string)
new=''
for i in range(len(string)):
    #print(string[i])
    string_new='.'+ string[i]
    #print(string_new)
    new=new+string_new

print(new)
