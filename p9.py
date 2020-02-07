number = int(input("Enter number: "))
Sum = 0
if number == 3 or number == 9:      #Αν βάλω 3 ή 9, μετά την πράξη το άθροισμα των ψηφίων θα κάνει 10. Χωρίς την if θα γινόταν η πράξη 1 + 0 με τα mod(%) και div(//) και δεν θα έμπαινα στη while.
    number = 10
elif number < 10:
    number = number * 3 + 1
    if len(str(number)) > 1:
        Sum = number // 10 + number % 10
        number = Sum
while len(str(number)) > 1:
    number = number * 3 + 1
    _str = str(number)
    _list = list(_str)
    for i in _list:
        Sum = Sum + int(i)
    number = Sum
    Sum = 0
print("The final summary is: ", number)