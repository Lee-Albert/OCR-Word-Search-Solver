
test = ['a', 't', 'r', 't', 'm', 'f', '\n' , 
        'w', 'e','e','q','u','z', '\n', 
        'o', 't', 's','x','j','y','\n',
        's','y','k','h','c','e']

def toGrid(array):
    rowLength = array.index('\n')
    x = []

    x.append(array[:rowLength])
    array = array[rowLength:]

    while array:
        array = array[1:]
        x.append(array[:rowLength])
        array = array[rowLength:]
        
    return x
    
print(toGrid(test))