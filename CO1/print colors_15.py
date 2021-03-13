# printout all colors from color list 1 not contained in color list 2
list_1=["red","black","green","yellow","silver","orange"]
list_2=["blue","white","silver","gold","grey","black"]
print([i for i in list_1 if i not in list_2])