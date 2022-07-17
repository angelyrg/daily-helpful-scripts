import os, shutil

downloads_path = "/Users/ANGEL/Downloads/Licia_files/"
nombre_carpeta = "LiciaFiles"

if __name__ == "__main__" :

    try:

        path = os.path.join("/Users/ANGEL/Downloads/", nombre_carpeta)
        os.mkdir(path)

        for filename in os.listdir( downloads_path ):

            file, extension =  os.path.splitext(filename)

            if "licia" in filename.lower() and extension != "" :

                shutil.move( downloads_path + filename, path )
                print( "Moved " + filename )


    except OSError as error:
        print(error)

