while True:
    n = input("Enter a positive integer n: ")
    if n.isdigit() and eval(n) > 0:
        switch = True
        sum = 0.0
        for i in range(1, eval(n)+1, 2):
            if switch:
                sum = sum + 4/i
                switch = False
            else:
                sum = sum - 4/i
                switch = True
        print("Sum =", sum)
    else:
        print("You entered an invalid number.")