
Fsel = input("Enter file name: ")
Ftype = input("Enter file type: ")
full_file_name = Fsel + "." + Ftype

root_location = input("do you want to use different location? (y/n):")
root_location_check = root_location.lower()

if root_location_check == "y":
    root_locations = input("Enter file location: ") 
elif root_location_check == "n":
    print("okay, file will be saved in current directory")

start_line = input("Enter start line: ")

f = open(full_file_name, "x")
f.write(start_line)
f.close()