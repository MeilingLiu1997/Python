def cs110upper(str):
    newstr = ''
    n = 0
    for n in range (0, len(str)):
        if ord(str[n]) in range (97, 123):
            newstr += chr(ord(str[n]) - 32)
        else:
            newstr += str[n]
    return newstr


def cs110lower(str):
    newstr = ''
    n = 0
    for n in range (0, len(str)):
        if ord(str[n]) in range (65, 91):
            newstr += chr(ord(str[n]) + 32)
        else:
            newstr += str[n]
    return newstr


def cs110rfind(str, char):
    for n in range(len(str),-1, -1):
        if str[n-1] == char:
            return n-1
    else:
        return -1


def cs110compare(str1, str2):
    if str1 < str2:
        return -1
    elif str1 == str2:
        return 0
    elif str1 > str2:
        return +1


def cs110strip(str):
    temp = ''
    index = 0
    for c in str:
        if c == ' ' or c == '\n' or c == '\t':
            index += 1
        else:
            break
    while index < len(str):
        temp += str[index]
        index += 1
    newstr = ''
    count = len(temp)-1
    num = 0
    for c in temp:
        if temp[count] == ' ':
            count -= 1
        else:
            while num < count+1:
                newstr += temp[num]
                num += 1
                break
    return newstr


def cs110replace(str, chr1, chr2):
    newstr = ''
    index = 0
    for c in str:
        if c == chr1:
            c = chr2
            index +=1
        newstr += c
    return newstr


def cs110lstrip(str):
    newstr = ''
    index = 0
    for c in str:
        if c == ' ' or c == '\n' or c == '\t':
            index += 1
        else:
            break
    while index < len(str):
        newstr += str[index]
        index += 1
    return newstr


def cs110in(str, search):
    if search in str:
        return True
    else:
        return False


def cs110notin(str, search):
    if search not in str:
        return True
    else:
        return False


def cs110capitalize(str):
    newstr = ''
    n = 0
    while n <= len(str)-1:
        newstr += str[n]
        if str[n] == ' ' and ord(str[n+1]) in range (97, 123):
            newstr += chr(ord(str[n+1])-32)
            n += 2
        elif ord(str[n]) in range (65, 91) and ord(str[n+1]) in range (65, 91):
            newstr += chr(ord(str[n+1])+32)
            n += 2
        else:
            n += 1
    return newstr


def main():
    s1 = 'I like PYthon a lot Ah'
    print('Own function1:', cs110upper(s1))
    print('        Test1:', s1.upper())
    print('=====================================')
    s2 = 'I like PYthon a lot Ah'
    print('Own function2:',cs110lower(s2))
    print('        Test2:',s2.lower())
    print('=====================================')
    s3 = 'I like PYthon a lot Ah'
    print('Own function3:',cs110rfind(s3, 'a'))
    print('        Test3:', s3.rfind('a'))
    print('=====================================')
    print('Own function4:',cs110compare('dog','cat'))
    print("        Test4: There's already been an answer.")
    print('=====================================')
    s5 = '   Monday\tTuesday\n   .      '
    print('Own function5:',"***" +cs110strip(s5)+ "***")
    print('        Test:5',"***" + s5.strip() + "***")
    print('=====================================')
    s6 = 'this is a nice day.'
    print('Own function6:',cs110replace(s6, 'a', 'k'))
    print('        Test6:', s6.replace('a','k'))
    print('=====================================')
    s7 = '   Mondday\tTuesday\n   .      '
    print('Own function:7',"***" +cs110lstrip(s7)+"***")
    print('        Test7:',"***" + s7.lstrip() +"***")
    print('=====================================')
    s8 = 'I like PYthon a lot Ah'
    print('Own function8:',cs110in(s8,'PYthon'))
    print('        Test8:','PYthon' in s8)
    print('=====================================')
    s9 = 'I like PYthon a lot Ah'
    print('Own function9:',cs110notin(s9,'python'))
    print('        Test9:', 'python' not in s9)
    print('=====================================')
    s10 = 'I like Python a lot'
    print('Own function10:',cs110capitalize(s10))
    print('Test10 (title):', s10.title())
    print(' (capitalize) :',s10.capitalize())
main()