#Fails 231.py
#Autors: Artis Erglis

from PythonMagick import Image
 
# Izgatavojam jaunu objektu - bilde
bilde= Image("3x3", "#22aaff")

# Izgatavojam mainiigos x un y
x=y=0

# Uzstāda objekta 'bilde' x,y pixela krasu
bilde.pixelColor (x,y, "#eeff22")
bilde.pixelColor (1,1, "#eeff22")
bilde.pixelColor (2,2, "#eeff22")

# 3x3 pixels palielina liidz 200x200
bilde.scale("200x200")

# Objektu 'bilde' ieraksta failaa
bilde.write ("231.png")
