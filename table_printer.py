tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
    colWidth = [0] * len(tableData)
    for i, list in enumerate(tableData):
        colWidth[i] = len(max(list, key = len))
    for j, word in enumerate(list):
        for k, list in enumerate(tableData):
            print(tableData[k][j].rjust(colWidth[k]), end=' ')
        print()
            
    
printTable(tableData)