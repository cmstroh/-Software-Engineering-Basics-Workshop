for fb in range(20):
    
    if fb % 3 == 0 and fb % 5 == 0:
        print("fizzbuzz")
        continue
    elif fb % 3 == 0:
        print("fizz")
        continue
    elif fb % 5 == 0:
        print("buzz")
        continue

    print(fb) 