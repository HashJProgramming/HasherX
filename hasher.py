import hashlib

# Hash'J Programming
def hashing(xhash):
    return hashlib.md5(xhash.encode())
def result(md5hash):   
    x = hashing(md5hash).hexdigest()
    print("HASH 1: ", x)
    y = hashing(x).hexdigest()
    print("HASH 2: ", y)
    z = hashing(y).hexdigest()
    print("HASH 3: ", z)
# Hash'J Programming
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
MD5 = input("Enter Number: ")
print("#################################################")
result(MD5)
print("#################################################")
