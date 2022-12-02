import base64
with open("C:\Users\PATRIX\Documents\project graphics\New folder\Half-Life 2.png",'rb') as imagefile:
    base64string=base64.b64encode(imagefile.read()).decode('ascii')
with open("C:\Graphics\HL2.txt","w") as f:
    f.write(base64string)
