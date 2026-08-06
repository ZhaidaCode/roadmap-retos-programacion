def countdown(number:int):
    if number <= 0:
        print("Done")

    else: 
        print(number)
        countdown(number - 1)

countdown(5)