# Fails: 232.py
# Autors: Artis Erglis

from PythonMagick import Image

# Izgatavojam jaunu objektu - bilde
# Objekta izmeers 16x16 pixels
bilde = Image ( "16x16", "#22aaff" )

# Izgatavojam mainiigos x un y
x = y = 0

# Uzstaada objekta 'bolde' x,y pixela kraasu
bilde.pixelColor ( x,y, "#FF0000")

# 16x16 pixels palielina lidz 200x200
bilde.scale ( "200x200" )

# Objektu 'bilde' ieraksata failaa
bilde.write ( "232.png" )

