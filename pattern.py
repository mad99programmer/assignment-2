import math

def generate_pattern(rows=9):
    

    mid_row=math.ceil(rows/2) #ceil rounds up
    for i in range (0,mid_row):

        for e in range(i+1):
            print('*',end=" ")
        print()   

    for i in range (mid_row-1,0,-1):

        for num in range(i,0,-1):
            print("*",end=' ')
        print()
    
generate_pattern()