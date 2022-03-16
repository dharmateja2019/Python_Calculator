def addition():
    print("Addition")
    n = float(input("Enter the number: "))
    t = 0
    ans = 0
    while n!=0:
        ans += n
        t += 1
        if t > 1:
            t=0
            break
        n = float(input("Enter another number(0 to calulate): "))
    return [ans]

def subtraction():
    print("Subtraction")
    n = float(input("Enter the number: "))
    t = 0
    ans = 0
    while n!=0:
        ans -= n
        t += 1
        if t > 1:
            t=0
            break
        n = float(input("Enter another number(0 to calulate): "))
    return [ans]

def multiplication():
    print("Multiplication")
    n = float(input("Enter the number: "))
    t = 0
    ans = 0
    while n!=0:
        ans *= n
        t += 1
        if t > 1:
            t=0
            break
        n = float(input("Enter another number(0 to calulate): "))
    return [ans]

def division():
    print("Division")
    n = float(input("Enter the number: "))
    t = 0
    ans = 0
    while n!=0:
        ans /= n
        t += 1
        if t > 1:
            t=0
            break
        n = float(input("Enter another number(0 to calulate): "))
    return [ans]

if __name__ == "__main__":
    print('--------------------------')
    print('THE CALCULATOR')
    print('--------------------------')
    print('1.Addition')
    print('2.Subtraction')
    print('3.Muliplication')
    print('4.Division')
    choice = 1
    while choice>0:
        choice = int(input('Enter your choice: '))
        if choice == 1:
            print(addition())
        elif choice == 2:
            print(subtraction())
        elif choice == 3:
            print(multiplication())
        elif choice == 4:
            print(division())
        else:
            print('Wrong choice enter again: ')