import sys

print(2+2)

xxtentation = sys.argv[1]

if xxtentation == "add":
    x = int(sys.argv[2])
    y = int(sys.argv[3])

    print(x+y)

if command == "countto":
    x = int(sys.argv[2])

    for i in range (x):
        print(i)
