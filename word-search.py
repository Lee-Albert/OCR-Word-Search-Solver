from PIL import Image
import pytesseract

#resizes the wordsearch and turns into text
def translate(image):
    im = Image.open(image)
    basewidth = 1000
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
    grid = []
    
    length = array.index('\n')
    grid.append(array[:length])
    array = array[length:]
    
    while array:
        array = array[1:]
        try:
            length = array.index('\n')
            grid.append(array[:length])
            array = array[length:]
        except:
            grid.append(array[0:])
            array = []
    
    bank = []

    for word in grid:
        bank.append(''.join(word))

    return bank
  
def checkFirst(grid, word):
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            try:
                if grid[i][j] == word[0]:
                    pos = [i, j]
                    checkSecond(grid, word, pos)
                else:
                    pass
            except:
                pass


def checkSecond(grid, word, pos):
    xy = pos.copy()
    for i in range(0,1):
        try:
            if grid[pos[0] - 1][pos[1]] == word[1] and directionSearch(grid, pos, "N", word):
                print(word, xy, "N")
                break 
            else:
                pass 
        except:
            pass
        try:
            if grid[pos[0] - 1][pos[1] + 1] == word[1] and directionSearch(grid, pos, "NE", word):
                print(word, xy, "NE")
                break 
            else:
                pass
        except:
            pass
        try:
            if grid[pos[0]][pos[1] + 1] == word[1] and directionSearch(grid, pos, "E", word):
                print(word, xy, "E")
                break
            else:
                pass
        except:
            pass
        try:
            if grid[pos[0] + 1][pos[1] + 1] == word[1] and directionSearch(grid, pos, "SE", word):
                print(word, xy, "SE")
                break
            else:
                pass
        except:
            pass
        try:
            if grid[pos[0] + 1][pos[1]] == word[1] and directionSearch(grid, pos, "S", word):
                print(word, xy, "S")
                break
            else:
                pass
        except:
            pass
        try:
            if grid[pos[0] + 1][pos[1] - 1] == word[1] and directionSearch(grid, pos, "SW", word):
                print(word, xy, "SW")
                break
            else:
                pass
        except:
            pass
        try:
            if grid[pos[0]][pos[1] - 1] == word[1] and directionSearch(grid, pos, "W", word):
                print(word, xy, "W")
                break
            else:
                pass
        except:
            pass
        try:
            if grid[pos[0] - 1][pos[1] - 1] == word[1] and directionSearch(grid, pos, "NW", word):
                print(word, xy, "NW")
                break
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

wordSearchArray = translate("test-image3.png")
#im = Image.open("test-image3.png")
#wordSearchArray = pytesseract.image_to_string(im, lang = "eng") 
wordBankArray = translate("test-bank3.png")

wordSearch = toGrid(list(wordSearchArray))
wordBank = toBank(list(wordBankArray))

print(wordBank)
print(wordSearch)

for word in wordBank:
    checkFirst(wordSearch, word)






