# Fizz Buzz

count = 1

while count <= 100:
    if (count % 3 == 0) and (count % 5 == 0):
        print("Fizz Buzz")
    elif count % 3 == 0:
        print("Fizz")
    elif count % 5 == 0:
        print("Buzz")
    elif (count % count == 1) and (count % 1 == 0):

    else:
        print(count)

    count += 1
