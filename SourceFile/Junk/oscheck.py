from sys import platform

if platform == "linux" or platform == "linux2":
    print("linux")
elif platform == "darwin":
    print("OS X")
elif platform == "win32":
    print("Windows")
