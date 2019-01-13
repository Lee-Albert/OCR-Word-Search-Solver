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
    if direction == "n":
        return nDirection(array, position, word)
    elif direction == "ne":
        return neDirection(array, position, word)
    elif direction == "e":
        return eDirection(array, position, word)
    elif direction == "se":
        return seDirection(array, position, word)
    elif direction == "s":
        return sDirection(array, position, word)
    elif direction == "sw":
        return swDirection(array, position, word)
    elif direction == "w":
        return wDirection(array, position, word)
    elif direction == "nw":
        return nwDirection(array, position, word)