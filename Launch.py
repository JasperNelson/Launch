#NOTE: This script is intended to be used with Oh-My-Zsh
import sys
import os
import subprocess

#function to combine a list into a string separated by spaces
def comb(li):
    return ' '.join(li)
    
#function to return point of where a line becomes a comment in a zshrc file
def commentchk(line):
    #checks if the first chr is a comment
    if line.startswith('#'):
        return 0
    for x in range(1,len(line)):
        #nullifies any text after a comment 
        if line[x-1]==" " and line[x]=="#":
            return x
    return len(line)

  
#gets rid of the first part of the list as its always the name of the program
args=sys.argv[1:]

#checks if ZDOTDIR has been set by the user
if "ZDOTDIR" in os.environ:
    if os.path.isdir(os.getenv("ZDOTDIR")):
        home=os.getenv("ZDOTDIR")
    else:
        raise Exception("ZDOTDIR is Malformed or improperly defined: needs to be a real directory")
else:
#if ZDOTDIR isnt defined user must be using default .zshrc conf file loc
    home=os.path.expanduser('~')

if 'starship' in args:
    args.remove('starship')
else:
    args.append('starship')

#gets rid of any duplicate plugins
args=set(args)
com=comb(args)
#opens contents of zshrc file
with open(f'{home}/.zshrc', 'r', encoding='utf-8') as file: 
    data = file.readlines() 

for x in range(0,len(data)):
    #ignores commented out sections of shell
    comloc=commentchk(data[x])
    before=data[x][:comloc]
    if "plugins=(" in before:
        data[x]= "plugins=("+com+")\n"

with open(f'{home}/.zshrc', 'w', encoding='utf-8') as file: 
    file.writelines(data)

# be very careful with changing this if you allow direct user manipulation it can be a security flaw
subprocess.call(f"source {home}/.zshrc", shell=False, executable='/usr/bin/zsh' )


        