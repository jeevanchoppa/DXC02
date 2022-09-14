choice = 9
while (choice != 0):
    print("Enter 1 to Create Table :")
    print("Enter 2 for INSERT :")
    print("Enter 3 for FETCH : ")
    print("Enter 4 for UPDATE :")
    print("Enter 5 for DELETE :")
    print(" ")
    print("Enter 0 to EXIT ")
    print(" ")
    choice = int(input('Enter your Choice : '))
    if choice == 1:
        print(create())
    if choice == 2:
        print(insert('val1', 'val2', 'val3', 'val4', 'val5'))
    elif choice == 3:
        print(fetch ())
    elif choice == 4:
        print(update('RollNo', 'MathMarks'))
    elif choice == 5:
        print(delete('RollNo'))
