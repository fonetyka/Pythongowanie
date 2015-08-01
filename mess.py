from PIL import Image

def main():

    filename_a = "/home/jstudzinski/Desktop/yamaha.jpg"
    filename_b = "/home/jstudzinski/Desktop/kawasaki.jpg"
    
    image_b = Image.open(filename_b, "r")
    image_a = Image.open(filename_a, "r")
    
    image_blended = Image.blend(image_a, image_b, 1.5)  
    image_blended.show()
   
    del image_a, image_b
  
if __name__=='__main__':
    main()
