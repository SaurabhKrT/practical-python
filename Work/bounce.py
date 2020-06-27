# bounce.py
#
# Exercise 1.5
height = 100 #meters
bounce = 1


while bounce <=10:
    height = round(height*3/5, 4)
    print (bounce, height)
    bounce = bounce + 1 