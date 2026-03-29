import os

def scan_folder(path, level=0):  # scans a folder and prints what inside of it
    items = os.listdir(path)
    spaces = "    " * level  # for decoration :)

    for item in items:
        full_path = os.path.join(path, item) 
        
        if os.path.isfile(full_path):
            print(f"{spaces}📄 {item}")
        elif os.path.isdir(full_path):
            print(f"{spaces}📁 {item}")
            scan_folder(full_path, level + 1)  # Recursive call 

def main():
    try:
        user_path = input("Enter the path: ")
        print(f"Scanning: {user_path}")
        scan_folder(user_path)
    except OSError:  
        print("File not found")

if __name__ == "__main__": 
    main()
