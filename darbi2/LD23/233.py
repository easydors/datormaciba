# Fails: 233.py
# Autors: Artis Erglis

from PythonMagick import Image

# Izgatavojam jaunu objektu - bilde
# Objekta izmeers 32x32 pixels
bilde = Image ( "32x32", "#22aaff" )

# Izgatavojam mainiigos x un y
x = y = 0

# Uzstaada objekta 'bolde' x,y pixela kraasu
bilde.pixelColor ( x,y, "#FFC0CB")

# 32x32 pixels palielina lidz 200x200
bilde.scale ( "200x200" )

# Objektu 'bilde' ieraksata failaa
bilde.write ( "233.png" )
