from PIL import Image
import pytesseract

#resizes the wordsearch and turns into text
def translate(image):
    im = Image.open(image)
    basewidth = 2000
    wpercent = (basewidth/float(im.size[0]))
    hsize = int((float(im.size[1])*float(wpercent)))
    im = im.resize((basewidth,hsize), Image.ANTIALIAS)
    text = pytesseract.image_to_string(im, lang = "eng")

    return text

def toGrid(array):
    rowLength = array.index('\n')
    grid = []

    grid.append(array[:rowLength])
    array = array[rowLength:]

    while array:
        array = array[1:]
        grid.append(array[:rowLength])
        array = array[rowLength:]
        
    return grid

def toBank(array):
    rowLength = array.index('\n')
    grid = []

    grid.append(array[:rowLength])
    array = array[rowLength:]

    while array:
        array = array[1:]
        grid.append(array[:rowLength])
        array = array[rowLength:]

    bank = []
    for word in grid:
        bank.append(''.join(word))
    
    return bank
  
def checkFirst(grid, word):
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if grid[i][j] == word[0]:
                pos = [i, j]
                checkSecond(grid, word, pos)



def checkSecond(grid, word, pos):
    try:
        if grid[pos[0] - 1][pos[1]] == word[1] and directionSearch(grid, pos, "N", word):
            print(word, pos, "N")
        else:
            pass 
    except:
        pass
    try:
        if grid[pos[0] - 1][pos[1] + 1] == word[1] and directionSearch(grid, pos, "NE", word):
            print(word, pos, "NE")
        else:
            pass
    except:
        pass
    try:
        if grid[pos[0]][pos[1] + 1] == word[1] and directionSearch(grid, pos, "E", word):
            print(word, pos, "E")
        else:
            pass
    except:
        pass
    try:
        if grid[pos[0] + 1][pos[1] + 1] == word[1] and directionSearch(grid, pos, "SE", word):
            print(word, pos, "SE")
        else:
            pass
    except:
        pass
    try:
        if grid[pos[0] + 1][pos[1]] == word[1] and directionSearch(grid, pos, "S", word):
            print(word, pos, "S")
        else:
            pass
    except:
        pass
    try:
        if grid[pos[0] + 1][pos[1] - 1] == word[1] and directionSearch(grid, pos, "SW", word):
            print(word, pos, "SW")
        else:
            pass
    except:
        pass
    try:
        if grid[pos[0]][pos[1] - 1] == word[1] and directionSearch(grid, pos, "W", word):
            print(word, pos, "W")
        else:
            pass
    except:
        pass
    try:
        if grid[pos[0] - 1][pos[1] - 1] == word[1] and directionSearch(grid, pos, "NW", word):
            print(word, pos, "NW")
        else:
            pass
    except:
        pass

def nDirection(array, position, word):
    possible = True
    while possible:
        if word == "":
            return True
        elif position[0] != 0:
            if word[0] == array[position[0]][position[1]]:
                word = word[1:]
                position[0] -=1
            else:
                return False
        elif position[0] == 0:
            if len(word)>1:
                return False
            elif word != array[position[0]][position[1]]:
                return False
            else:
                return True

def neDirection(array, position, word):
    width = len(array[0])-1
    possible = True
    while possible:
        if word == "":
            return True
        elif position[0] != 0 and position[1] != width:
            if word[0] == array[position[0]][position[1]]:
                word = word[1:]
                position[0] -=1
                position[1] +=1
            else:
                return False
        elif position[0] == 0 or position[1] == width:
            if len(word)>1:
                return False
            elif word != array[position[0]][position[1]]:
                return False
            else:
                return True

def eDirection(array, position, word):
    width = len(array[0])-1
    possible = True
    while possible:
        if word == "":
            return True
        elif position[1] != width:
            if word[0] == array[position[0]][position[1]]:
                word = word[1:]
                position[1] +=1
            else:
                return False
        elif position[1] == width:
            if len(word)>1:
                return False
            elif word != array[position[0]][position[1]]:
                return False
            else:
                return True

def seDirection(array, position, word):
    height = len(array)-1
    width = len(array[0])-1
    possible = True
    while possible:
        if word == "":
            return True
        elif position[0] != height and position[1] != width:
            if word[0] == array[position[0]][position[1]]:
                word = word[1:]
                position[0] +=1
                position[1] +=1
            else:
                return False
        elif position[0] == height or position[1] == width:
            if len(word)>1:
                return False
            elif word != array[position[0]][position[1]]:
                return False
            else:
                return True

def sDirection(array, position, word):
    height = len(array) - 1
    possible = True
    while possible:
        if word == "":
            return True
        elif position[0] != height:
            if word[0] == array[position[0]][position[1]]:
                word = word[1:]
                position[0] +=1
            else:
                return False
        elif position[0] == height:
            if len(word)>1:
                return False
            elif word != array[position[0]][position[1]]:
                return False
            else:
                return True

def swDirection(array, position, word):
    height = len(array)-1
    possible = True
    while possible:
        if word == "":
            return True
        elif position[0] != height and position[1] != 0:
            if word[0] == array[position[0]][position[1]]:
                word = word[1:]
                position[0] +=1
                position[1] -=1
            else:
                return False
        elif position[0] == height or position[1] == 0:
            if len(word)>1:
                return False
            elif word != array[position[0]][position[1]]:
                return False
            else:
                return True

def wDirection(array, position, word):
    possible = True
    while possible:
        if word == "":
            return True
        elif position[1] != 0:
            if word[0] == array[position[0]][position[1]]:
                word = word[1:]
                position[1] -=1
            else:
                return False
        elif position[1] == 0:
            if len(word)>1:
                return False
            elif word != array[position[0]][position[1]]:
                return False
            else:
                return True

def nwDirection(array, position, word):
    possible = True
    while possible:
        if word == "":
            return True
        elif position[0] != 0 and position[1] != 0:
            if word[0] == array[position[0]][position[1]]:
                word = word[1:]
                position[0] -=1
                position[1] -=1
            else:
                return False
        elif position[0] == 0 or position[1] == 0:
            if len(word)>1:
                return False
            elif word != array[position[0]][position[1]]:
                return False
            else:
                return True

def directionSearch(array, position, direction, word):
    if direction == "N":
        return nDirection(array, position, word)
    elif direction == "NE":
        return neDirection(array, position, word)
    elif direction == "E":
        return eDirection(array, position, word)
    elif direction == "SE":
        return seDirection(array, position, word)
    elif direction == "S":
        return sDirection(array, position, word)
    elif direction == "SW":
        return swDirection(array, position, word)
    elif direction == "W":
        return wDirection(array, position, word)
    elif direction == "NW":
        return nwDirection(array, position, word)

wordsearch = translate("test-image.png")
wordbank = translate("test-bank.png")

print(toGrid(list(wordsearch)))
print(toBank(list(wordbank)))

