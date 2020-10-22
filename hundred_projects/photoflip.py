from PIL import Image
import glob, os

def createdir(newpath):
    if not os.path.exists(newpath):
        os.makedirs(newpath)

def implement(filetype):

    createdir("output")

    for infile in glob.glob(filetype):
        
        file, ext = os.path.splitext(infile)
        im = Image.open(infile)
        out= im.transpose(Image.FLIP_LEFT_RIGHT)
        
        if filetype == "*.jpeg":
            out.save("output/" + file + ".jpeg", "JPEG")
        if filetype == "*.jpg":
            out.save("output/" + file + ".jpg", "JPEG")

def main():

    filetypes = ["*.jpeg","*.jpg"]  

    for filetype in filetypes:
     implement(filetype)

if __name__ == "__main__":
    main()