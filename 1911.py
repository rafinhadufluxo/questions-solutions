number = 1 
 while True: 
     number = int(input("")) 
     if number == 0: break 
  
     dic = {} 
  
     for x in range(number): 
         entry_a = input().split() 
         dic[entry_a[0]] = entry_a[1] 
  
     students = int(input("")) 
     mis, sin = int(0), int(0) 
  
     for x in range(students): 
         count = int(0) 
         name_dic = input().split() 
         for y in dic[name_dic[0]]: 
             if y != name_dic[1][count]: 
                 mis += 1 
             count += 1 
         if mis > 1: sin += 1 
  
         mis = 0 
  
     print(sin)
    
    ## referencia -> https://github.com/victorsaad00/URI---PYTHON/blob/master/1911.py
