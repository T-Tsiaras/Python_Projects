with open("quote.txt", "r") as f:
    keimeno = f.read()
keimeno = keimeno.split()
keimeno = list(dict.fromkeys(keimeno))  #removing list duplicates
keimeno = [word.strip(",").strip(".").strip("!") for word in keimeno]
counter = 0
if len(keimeno)!=0:
    for i in range(len(keimeno)):
        if len(keimeno[i])>3:
            counter+=1
            keimeno[i] = keimeno[i][1:] + keimeno[i][0] + "ay"
            print(keimeno[i])
    if counter==0:
        print("No words longer than 3 characters!")
else:
    print("Your file is empty!")