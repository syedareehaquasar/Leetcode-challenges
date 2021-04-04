''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

virusComp = input()
tc = int(input())
for z in range(tc):
    totest = input()
    i, j = 0, 0
    while j < len(totest) and i < len(virusComp):
        if totest[j] == virusComp[i]:
            j += 1
        i += 1
    if j == len(totest):
        print("POSITIVE")
    else:
        print("NEGATIVE")

