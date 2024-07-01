while True:
    val = input("Enter an integer number (or the word 'stop' to stop) >> ")
    if val == "stop":
        print("No number received. No Minimum found.")
        break
    else:
        if val.isdigit():
            minimum = eval(val)
            while True:
                val = input("Enter an integer number (or the word 'stop' to stop) >> ")
                if val.isdigit():
                    if eval(val) < minimum:
                        minimum = eval(val)
                elif val == "stop":
                    print("Minimum =", minimum)
                    exit()
                else:
                    print("You did not enter an integer value.")
        else:
            print("You did not enter an integer value.")
