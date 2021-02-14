def fibonacci(counter):
    x = 0
    y = 1
    z = 0
    count = 0

    while count < counter:
        
        z = x + y
        x = y
        y = z

        count += 1
        print(x)
    
fibonacci(20)

  