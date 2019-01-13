test = ['h','e','l','l','o','\n','w','o','r','l','d']

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

print(toBank(test))   