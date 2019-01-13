array1 = [["J", "S", "O", "L", "U", "T", "I", "S"], ["S", "U", "N", "A", "R", "U", "U", "A"], ["N", "E", "P", "T", "U", "N", "E", "T"], ["S", "O", "N", "I", "E", "I", "S", "U"], ["R", "C", "E", "V", "T", "R", "E", "R"], ["A", "H", "T", "R", "A", "E", "S", "N"], ["M", "M", "E", "R", "C", "U", "R", "Y"]]
words = ["EARTH", "JUPITER", "MARS", "MERCURY", "NEPTUNE", "SATURN", "URANUS", "VENUS"]


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

    




checkFirst(array1, words[0]) 

directionSearch()