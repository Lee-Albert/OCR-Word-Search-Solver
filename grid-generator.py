import random
import sys

orig_stdout = sys.stdout
f = open('out.txt', 'w')
sys.stdout = f

wordbox = []
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for col in range(10):
    row_list =  ""
    for row in range(10):
        row_list += alphabet[random.randint(0, 25)] + " "
    wordbox.append(row_list)
    print(row_list)

sys.stdout = orig_stdout
f.close()
