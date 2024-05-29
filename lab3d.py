#!/usr/bin/env python3
#AuthorID: mcini


import subprocess

def free_space():

    space = subprocess.Popen(["df -h | grep '/$' | awk '{print $4}'"], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True )

    output = space.communicate()
    stdout = output[0].decode('utf-8').strip()
    print(stdout)
    return stdout

free_space()



