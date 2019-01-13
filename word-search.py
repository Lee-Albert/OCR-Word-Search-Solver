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
            continue
    except:
        pass
     try:
        if grid[pos[0] - 1][pos[1] + 1] == word[1] and directionSearch(grid, pos, "NE", word):
            print(word, pos, "NE")
        else:
            continue
    except:
        pass
     try:
        if grid[pos[0]][pos[1] + 1] == word[1] and directionSearch(grid, pos, "E", word):
            print(word, pos, "E")
        else:
            continue
    except:
        pass
     try:
        if grid[pos[0] + 1][pos[1] + 1] == word[1] and directionSearch(grid, pos, "SE", word):
            print(word, pos, "SE")
        else:
            continue
    except:
        pass
     try:
        if grid[pos[0] + 1][pos[1]] == word[1] and directionSearch(grid, pos, "S", word):
            print(word, pos, "S")
        else:
            continue
    except:
        pass
     try:
        if grid[pos[0] + 1][pos[1] - 1] == word[1] and directionSearch(grid, pos, "SW", word):
            print(word, pos, "SW")
        else:
            continue
    except:
        pass
     try:
        if grid[pos[0]][pos[1] - 1] == word[1] and directionSearch(grid, pos, "W", word):
            print(word, pos, "W")
        else:
            continue
    except:
        pass
     try:
        if grid[pos[0] - 1][pos[1] - 1] == word[1] and directionSearch(grid, pos, "NW", word):
            print(word, pos, "NW")
        else:
            continue
    except:
        pass


wordsearch = translate("test1.png")
print(wordsearch)
array = list(wordsearch)

