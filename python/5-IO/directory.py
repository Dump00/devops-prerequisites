import os

# Get Current Directory
print(os.getcwd())
# /media/optimus-prime/blackhole/devops/python/5-IO


# making a new directory
# os.mkdir('newdir')


# Changing Directory 
os.chdir('/media/optimus-prime/blackhole/devops/python/5-IO/newdir')
print(os.getcwd())

with open("demo.txt", "w") as file1:
    file1.write("this is a new file")
    file1.close()


