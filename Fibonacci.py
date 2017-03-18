

number_of_times = input("How many numbers would you like to display of the Fibonacci sequence? ")

def fibonacci ():
    a, b = 1, 1
    print(a)
    steps=0
    while steps < int(number_of_times)-1 :
        a, b = b, a+b
        print(a)
        steps=steps+1

fibonacci()