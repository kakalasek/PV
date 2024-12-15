import os
import shutil
import subprocess

if __name__ == "__main__":
    if os.path.isdir("/home"):
        print("/home is a directory")

    os.mkdir("TestDir")
    os.rmdir("TestDir")

    # shutil.rmtree("TestDir")      Smaze slozku i s obsahem

    print(os.listdir("."))

    tree = subprocess.call(["tree", "../.."])
    print(tree)