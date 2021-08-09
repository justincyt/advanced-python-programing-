#import the library 
import os

print("Hello, Wellcome to my world in cmd \n")

# Create class shell including main and init 
class Shell_python:
    def __init__(self):
        print("Curent the Directory:",os.getcwd())# print the directory currently 
        curr=os.getenv("HOME")
        cmd=os.chdir(curr)
        cmd=""
        self.main(cmd)#link with main() function 

    #main() function to run cmd 
    def main(self,cmd):
        while True:
            cmd=input("cuongnguyen㉿kali:~$"+os.getcwd()+":")
            if cmd.split()[0]=='cd':
                try:
                    os.chdir(cmd[3:])# change directory from home to this directory
                    print("Current Directory:",os.getcwd())
                except FileNotFoundError: #if not found the directory to print 
                    print("bash:cd:No such file or directory")
            elif cmd =='exit':
                exit(0)
            else:
                os.system(cmd)#closed system 

if __name__ == '__main__':
    shell=Shell_python()
