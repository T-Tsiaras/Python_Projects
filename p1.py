#sort the list in ascending order function
def fun(o):
    return len(o)


with open("quote.txt") as f:
    keimeno = f.read()
keimeno = keimeno.split()
keimeno = [word.strip(",").strip(".").strip("!") for word in keimeno]
keimeno = list(dict.fromkeys(keimeno))  #removing list duplicates
keimeno.sort(key = fun)
taksinomish = keimeno[::-1]
vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')

#checking for vowels in 5 longest words
try:
    first = taksinomish[0]
    for i in first:
        if i in vowels:
            first = first.replace(i, '')
    print ("The 1st longest word is: " + first)
    try:
        second = taksinomish[1]
        for i in second:
            if i in vowels:
                second = second.replace(i, '')
        print("The 2nd longest word is: " + second)
        try:
            third = taksinomish[2]
            for i in third:
                if i in vowels:
                    third = third.replace(i, '')
            print("The 3rd longest word is: " + third)
            try:
                fourth = taksinomish[3]
                for i in fourth:
                    if i in vowels:
                        fourth = fourth.replace(i, '')
                print("The 4th longest word is: " + fourth)
                try:
                    fifth = taksinomish[4]
                    for i in fifth:
                        if i in vowels:
                            fifth = fifth.replace(i, '')
                    print("The 5th longest word is: " + fifth)
                except:
                    print("There are less than five words in your file!")
            except:
                print("There are less than five words in your file!")
        except:
            print("There are less than five words in your file!")
    except:
        print("There are less than five words in your file!")
except:
    print("The file is empty!")