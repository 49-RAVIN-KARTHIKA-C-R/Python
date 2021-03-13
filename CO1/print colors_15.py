# printout all colors from color list 1 not contained in color list 2
list_1=["violet","black","green","yellow","pink","orange"]
list_2=["blue","white","pink","gold","grey","black"]
print([i for i in list_1 if i not in list_2])