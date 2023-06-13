def sum(*num):
   sum = 0
   i = 0
   while i < len(num):
       sum += num[i]
       i += 1
   print(sum)

sum(1, 2, 3, 4, 5, 6)
