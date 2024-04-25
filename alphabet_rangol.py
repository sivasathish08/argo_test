alphabet_string = 'abcdefghijklmnopqrstuvwxyz'
char = '-'


def addcenter(string):
    result = ''
    for i in range(len(string)):
        if len(string)-1 == i:
            result = result + string[i]
        else:
            result = result + string[i] + char
    return result

def getChar(number):
    return alphabet_string[:number]

def mirror(string):
    result =''
    for line in range(0,len(string)):
         result = result + string[len(string)-(line+1)]
    return addcenter(result+string[1:])

last = ''
size = 10
new_list=[]
for  i in range(size-1):
    print(mirror(alphabet_string[size-(i+1):size]).center(len(mirror(getChar(size))),"-"))
    last=alphabet_string[size-(i+1):size]
    new_list.append(last)
print(mirror(getChar(size)))
for j in range(len(new_list)):
    print(mirror(new_list[len(new_list)-j-1]).center(len(mirror(getChar(size))),"-"))
