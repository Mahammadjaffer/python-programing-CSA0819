n=int(input("enter="))
for fizzbuzz in range(1,n+1):

    if fizzbuzz % 15 == 0:
        print("FizzBuzz")                                        
        continue

    elif fizzbuzz % 3 == 0:    
        print("Fizz")                                        
        continue

    elif fizzbuzz % 5 == 0:        
        print("Buzz")                                    
        continue

    print(fizzbuzz)
