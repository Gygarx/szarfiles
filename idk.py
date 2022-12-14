import os,time
os.system('cls')
file_sprite = """"""
errors = 0

current_pth = "C:\\"

discovered = []

def discover():
    global discovered
    discovered = []
    for path in os.listdir(current_pth):
        if str(path)[0] !="$":
            discovered.append(str(path))

def show_discover():
    os.system('cls')
    print(f"Showing now: {current_pth}")
    print("Name                                 Type      Size")
    print("")
    for obj in discovered:
        try:
            file = current_pth+obj
            isfile = os.path.isdir(file)
            fileType = ""
            if not isfile:
                fileType = "File"
            else:
                fileType = "Dir_"

            fileName = str(obj)+(40-len(file))*" "
            
            print(f"{fileName}{fileType}      {os.stat(file).st_size /(1024*1024)}")
            time.sleep(0.01)
        except:
            global errors
            errors +=1
    print("\n\n\n")

while 1:
    discover()
    show_discover()
    print(errors)
    command = input("Type dir name or 'quit' to exit: ")
    if command == "quit":
        break
    if command == "base":
        current_pth = "C:\\"
    else:
        current_pth += command +"\\"
        print(current_pth)
        time.sleep(1)