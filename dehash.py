import hashlib
import threading
print("#################################################")
print()
print("""
██╗░░██╗░█████╗░░██████╗██╗░░██╗██╗░░░░░██╗
██║░░██║██╔══██╗██╔════╝██║░░██║╚█║░░░░░██║
███████║███████║╚█████╗░███████║░╚╝░░░░░██║
██╔══██║██╔══██║░╚═══██╗██╔══██║░░░██╗░░██║
██║░░██║██║░░██║██████╔╝██║░░██║░░░╚█████╔╝
╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝░░░░╚════╝░
""")
print("Develop by Hash'J Programming")
print("#################################################")
MD5 = input("Enter MD5 Hash: ")
def dehashing(xhash):
    return hashlib.md5(xhash.encode())

def threader1():
    for x in range(9999999999, 0, -1):
        if MD5 == dehashing(str(x)).hexdigest():
            print(f"CORRECT MD5: {dehashing(str(x)).hexdigest()} | {x}")
            break
def threader2():
    for x in range(0,9999999999):
        if MD5 == dehashing(str(x)).hexdigest():
            print(f"CORRECT MD5: {dehashing(str(x)).hexdigest()} | {x}")
            break
def threader3():
    for x in range(1000000000,9999999999):
        if MD5 == dehashing(str(x)).hexdigest():
            print(f"CORRECT MD5: {dehashing(str(x)).hexdigest()} | {x}")
            break
def threader4():
    for x in range(2000000000,9999999999):
        if MD5 == dehashing(str(x)).hexdigest():
            print(f"CORRECT MD5: {dehashing(str(x)).hexdigest()} | {x}")
            break
def threader5():
    for x in range(3000000000,9999999999):
        if MD5 == dehashing(str(x)).hexdigest():
            print(f"CORRECT MD5: {dehashing(str(x)).hexdigest()} | {x}")
            break
def threader6():
    for x in range(4000000000,9999999999):
        if MD5 == dehashing(str(x)).hexdigest():
            print(f"CORRECT MD5: {dehashing(str(x)).hexdigest()} | {x}")
            break
def threader7():
    for x in range(5000000000,9999999999):
        if MD5 == dehashing(str(x)).hexdigest():
            print(f"CORRECT MD5: {dehashing(str(x)).hexdigest()} | {x}")
            break
print("#################################################")
print("Select thread to run?: (1)(2)(3)(4)(5)(6)(7)")
print("[1] - 9999999999 to 0")
print("[2] -          0 to 9999999999")
print("[3] - 1000000000 to 9999999999")
print("[4] - 2000000000 to 9999999999")
print("[5] - 3000000000 to 9999999999")
print("[6] - 4000000000 to 9999999999")
print("[7] - 5000000000 to 9999999999")
print("#################################################")
slcted = input("Select: ")

if slcted == "1":
    print("Running. . .")
    threading.Thread(target=threader1).start()
elif slcted == "2":
    print("Running. . .")
    threading.Thread(target=threader2).start()
elif slcted == "3":
    print("Running. . .")
    threading.Thread(target=threader3).start()
elif slcted == "4":
    print("Running. . .")
    threading.Thread(target=threader4).start()
elif slcted == "5":
    print("Running. . .")
    threading.Thread(target=threader5).start()
elif slcted == "6":
    print("Running. . .")
    threading.Thread(target=threader6).start()
elif slcted == "7":
    print("Running. . .")
    threading.Thread(target=threader7).start()
else:
    print("Invalid Input")        
