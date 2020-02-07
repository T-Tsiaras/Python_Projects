with open("quote.txt", "r") as f:
    keimeno = f.read()
keimeno = keimeno.split()
keimeno = list(dict.fromkeys(keimeno))  #removing list duplicates
keimeno = [word.strip(",").strip(".").strip("!") for word in keimeno]
vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
if len(keimeno) != 0:
    for i in range(len(keimeno)):
        num_vowels = 0
        total_letters = 0
        for j in keimeno[i]:
            if j in vowels:
                num_vowels = num_vowels + 1
            total_letters = total_letters + 1
            #Counting the number of lowercase bad letters
            f = int(keimeno[i].count("f"))
            c = int(keimeno[i].count("c"))
            k = int(keimeno[i].count("k"))
            r = int(keimeno[i].count("r"))
            #Counting the number of uppercase bad letters
            F = int(keimeno[i].count("F"))
            C = int(keimeno[i].count("C"))
            K = int(keimeno[i].count("K"))
            R = int(keimeno[i].count("R"))
            bad_letters = f + c + k + r + F + C + K + R 
            good_letters = total_letters - bad_letters - num_vowels

        if good_letters <= bad_letters:
            print(keimeno[i], ": is a bad word!")
        else:
            print(keimeno[i], ": is a good word!")
else:
    print("Your file is empty!")