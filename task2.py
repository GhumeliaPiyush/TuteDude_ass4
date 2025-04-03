with open ("output.txt","w") as file:
    line1 = input("Enter text to write to the file: ")
    file.write(line1+"\n")
    
    print("Data successfully written to the output.txt.")

with open("output.txt","a") as file:
    line2=input("Enter additional text to appand the file: ")
    file.write(line2)
    print("Data successfully appanded")
    
with open("output.txt","r") as file:
    lines = file.read()
    print("Final content of output.txt:")
    print(lines)