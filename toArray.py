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
