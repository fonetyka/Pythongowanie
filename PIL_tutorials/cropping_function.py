from PIL import Image


def main():

    filename = "/home/jstudzinski/Desktop/yamaha.jpg"

    image = Image.open(filename)
    cropped_image = image.crop((10,10,100,100))
    cropped_image.show()
    

    del image

if __name__=='__main__':
    main()
