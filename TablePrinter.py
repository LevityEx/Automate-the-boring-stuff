tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose'],
             ['stapler', 'ruler', 'pencil', 'scissors']]


def printTable(table):
    colWidths = [0] * len(table)

    for i in range(len(table)): #for each list
        for j in range(len(table[i])): #for each word in the list
            if(len(table[i][j]) > colWidths[i]): #if longest word
                colWidths[i] = len(table[i][j]) #store new max len

    for n in range(len(table[0])): # for len of each list (same size in spec)
        for m in range(len(table)):
            print(table[m][n].rjust(colWidths[m]), end=" ") # print each column 
        print('', end='\n')
printTable(tableData)