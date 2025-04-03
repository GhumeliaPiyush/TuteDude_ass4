try:
    with open ("sample.txt","r") as file:
        lines = file.readlines()
        for line in lines:
            print(line,end="")
except FileNotFoundError:
    print("print sample.txt not found")