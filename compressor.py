
import time
from PIL import Image, ImageEnhance
import os
import subprocess

###
start_time = time.time()
###

extensions = [".png", ".jpg", ".jpeg"]

def compress_png(input_path, output_path):
    try:
        # First Install pngquant. (https://pngquant.org/)
        subprocess.run(['C:/pngquant/pngquant', '--force', '--skip-if-larger', '--quality=0-20', input_path, '-o', output_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error al comprimir la imagen: {e}")

if __name__ == "__main__":
    c = 0
    for file in os.listdir():
        filename, extension = os.path.splitext(file)
        if extension.lower() in extensions:
            c += 1
            original_size = os.path.getsize(file)

            # Crea un nombre de archivo temporal para la imagen comprimida
            temp_filename = "temp_" + filename + extension
            full_filename = filename + extension

            if (original_size == 0):
                print(f"{c:3} {original_size:9} -> --------- [--.--%] {full_filename}")
                continue
            
            if extension.lower() == ".png":
                # Para PNG, usa pngquant para la compresión
                compress_png(file, temp_filename)
            else:
                # Para JPEG, usa PIL para la compresión
                imagen = Image.open(file)
                imagen.save(temp_filename, optimize=True, quality=18)
            
            # Comprueba si el archivo temporal existe (puede no existir si pngquant no guardó el archivo debido a --skip-if-larger)
            if os.path.exists(temp_filename):
                final_size = os.path.getsize(temp_filename)
                if final_size < original_size:
                    # Si el archivo comprimido es más pequeño, reemplaza el original
                    os.replace(temp_filename, full_filename)
                else:
                    # Si no, elimina el archivo temporal
                    os.remove(temp_filename)
            else:
                final_size = original_size  # No hubo compresión efectiva

            percent = round((1 - (final_size / original_size)) * 100, 2)
            print(f"{c:3} {original_size:9} -> {final_size:9} [{percent}%] {full_filename}")

    print(f"{c} Images compressed")




###
end_time = time.time()
execution_time = end_time - start_time
print(f"Tiempo de ejecución: {execution_time} segundos.")
###

