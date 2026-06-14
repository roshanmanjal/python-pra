name = "Roshan"
# positive slice
print(name[0:3]) # from start to 3rd by excluding 3rd
 # r=0 o=1 s=2 h=3 a=4 n=5
print(name[0:6])    
print(name[0:4]) # 0 to 4 but excluding 4th char
print(name[0:]) # 0 to length os string
print(name[1:5]) # from 1 to 4 (exclude 5)
print("Positive Slice Ends Here")
# neg slicing 
# r=-6 o=-5 s=-4 h=-3 a=-2 n=-1
print(name[-5:-3])  # from -5 to -3 (exclude -3 char)
print(name[-2:-5]) # this will never work 
# as it cannot backwards 
# so to go backwards we will do in 3 nmubers
print(name[-2:-5:-1]) # ahs
