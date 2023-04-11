#! python3
# tablePrinter.py - program to take a table (2d Array of strings and pring them out in a formatted table)

def printTable(table):
    longestWord = []
    formatted = []

    for i in range(len(table)):
        for j in range(len(table[0])):
            if j == 0:
                longestWord.append(len(table[i][j]))
            else:
                if len(table[i][j]) > longestWord[i]:
                    longestWord[i] = len(table[i][j])
    
    for i in range(len(table[0])):
        row = ''
        for j in range(len(table)):
            row += f'{table[j][i].rjust(longestWord[j])} ' 
        print(row)

            




tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)