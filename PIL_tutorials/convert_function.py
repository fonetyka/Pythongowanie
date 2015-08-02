from PIL import Image

def main():

    filename = "/home/jstudzinski/Desktop/yamaha.jpg"

    image = Image.open(filename)
    converted_image = image.convert("1")
    converted_image.show()

    del image 


if __name__=='__main__':
    main()
