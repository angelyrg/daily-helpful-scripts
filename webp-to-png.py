#Install Pillow First [ pip install Pillow ]
from PIL import Image  
import os

if __name__ == "__main__":
    
    for file in os.listdir():
        filename, extension =  os.path.splitext(file)

        if(extension != "" and extension == ".webp" ):
            imagen = Image.open(file)
            imagen.save("mim_"+filename+".png", optimize=True, quality=60)