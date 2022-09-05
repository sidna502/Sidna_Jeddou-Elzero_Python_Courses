import os
# First
num = 1

while num <= 50:
    if num == 25:
        myFile = open("special-text.text ", 'w')

    else:
        myFile = open(f"Text{str(num)}.text ", 'w')
        myFile.write(f"Elzero Web School => {num}")

    num += 1
    myFile.close()

print(os.getcwd())      # Current Working Directory
print(os.path.dirname(os.path.abspath(__file__)))      # The Path of My Folder
print(os.path.basename(myFile.name))
print(num)
