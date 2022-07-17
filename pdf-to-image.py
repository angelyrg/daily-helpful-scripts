#Install pdf2image [ pip install psd2image ]
from pdf2image import convert_from_path
import os

#install poppler from https://github.com/oschwartz10612/poppler-windows/releases/
poppler_path = r"D:\Program Files\poppler-22.04.0\Library\bin"



if __name__ == "__main__":
    try:
        for file in os.listdir():
            filename, extension = os.path.splitext(file)

            if (extension != "" and extension == ".pdf"):
                os.mkdir(filename)
                pages = convert_from_path(file, poppler_path=poppler_path)

                for page in range(len(pages)):
                    pages[page].save(filename + '/page_' + str(page+1) + '_' + filename + '.png', 'PNG')
            else:
                print("There is not pdf files to convert.")

        print("Converted successfully :)")

    except OSError as e:
            print(e)
