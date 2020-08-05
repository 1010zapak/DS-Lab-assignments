arr = [0, 0, 0, 0, 0]
amax = 4
top = -1

def push():
    global top, arr
    item = int(input("Item myou want to push="))
    if top == amax - 1:
        print("Overflow")
    else:
        top = top + 1
        arr[top] = item
        print("Array after pushing ", item, " is:", arr)


# deleting element in empty stack
def pop():
    global top, arr
    if top == -1:
        print("underflow")
    else:
        print("Array element popped is:", arr[top])
        arr[top] = 0
        top = top - 1
        print(arr)


def peep():
    global top, arr
    i = int(input("Enter which index element you want="))
    if (i > len(arr)):
        print("Invalid Input")
    else:
        print("Element at", i, "postion=", arr[i])


def main():
    i = 1
    while True:
        print("--------STACK OPERATIONS-----------")
        print("1.Push")
        print("2.Pop")
        print("3.Peep")
        print("5.Exit")
        print("-----------------------")
        choice = int(input("Enter your choice:"))
        if choice == 1:
            push()
            main()
            break;
        elif choice == 2:
            pop()
            main()
            break;
        elif choice == 3:
            peep()
            main()
            break;
        elif choice == 5:
            exit(0)
            break;
        else:
            print("Invalid choice")
            break;


main()