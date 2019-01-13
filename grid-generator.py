import random
import string
import sys

orig_stdout = sys.stdout
f = open('out.txt', 'w')
sys.stdout = f

width = 10
height = 10

def insert_word(word, grid):

    word = random.choice([word,word[::-1]]) # Random order of String
    dir = random.choice([[1,0], [0,1], [1,1]]) # Random choice of Direction

    x_width = width if dir[0] == 0 else width - len(word)
    y_height = height if dir[1] == 0 else height - len(word)

    x = random.randrange(0, x_width)
    y = random.randrange(0, y_height)

    for i in range(0, len(word)):
        grid[y + dir[1]*i][x + dir[0]*i] = word[i]
    return grid

grid = [[random.choice(string.uppercase) for i in range(0, 10)] for i in range(0, 10)]
word_list = ['HELLO','TALON','CLOSE']

for word in word_list:
    grid = insert_word(word, grid)
print "\n".join(map(lambda row: " ".join(row), grid))

sys.stdout = orig_stdout
f.close()
