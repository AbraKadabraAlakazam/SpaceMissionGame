room = [ 
        [3,2,2],
        [3,1,3],
        [2,2,3]
       ]
       

#version 3.0
m=0
n=0
f='';
for m in range(len(room)):
    for n in range(len(room[m])):
        f = f + str(room[m][n])
    print (f)    
    f=''
    

#version 2.0
"""
i=0
for i in range(len(room)):
   print (str(room[i][0])+ str(room[i][1])+ str(room[i][2]))
"""

#version 1.0
"""
print (str(room[0][0])+str(room[0][1])+str(room[0][2]))
print (str(room[1][0])+str(room[1][1])+str(room[1][2]))
print (str(room[2][0])+str(room[2][1])+str(room[2][2]))
"""

    