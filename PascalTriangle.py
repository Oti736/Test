
def pascal(row,col):
   if (col == 1):return 1
   if (row == col):return 1
   #folosim metoda recursiva
   return pascal(row - 1, col - 1) + pascal(row - 1, col)

rows = int(sys.argv[1])
for r in range(1, rows + 1):
 print(" ")
 for c in range (1, r+1):
     value = pascal(r,c)
     print (value, end = " ")
 print(" ")
