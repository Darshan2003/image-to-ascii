import PIL
from PIL import Image,ImageOps

# ascii characters used to build the output text
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

# resize image according to a new width
def resize_image(image, new_width):
    width, height = image.size
    ratio = (height/width)/2.7
    
    new_height = int(new_width * ratio)
   
    resized_image = image.resize((new_width, new_height))
    return(resized_image)

# convert each pixel to grayscale
def grayify(image):
    mode=input("Enter mode (L/P/1) : ")

    grayscale_image = image.convert(mode)
    return(grayscale_image)
    
# convert pixels to a string of ascii characters
def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return(characters)    

def main():
    # attempt to open image from user-input
    path = input("Enter a valid pathname to an image: ")
    try:
        imaget = PIL.Image.open(path)
    except Exception as e:
        print(e, "is not a valid pathname to an image.")
        return
  
    # convert image to ascii    
    new_width=int(input("Enter width : "))
    if input("Do want to invert the image? y/n :") == "y":
        image=ImageOps.invert(imaget)
    else:
        image=imaget

    new_image_data = pixels_to_ascii(grayify(resize_image(image,new_width)))
    
    # format
    pixel_count = len(new_image_data)  
    ascii_image = "\n".join([new_image_data[index:(index+new_width)] for index in range(0, pixel_count, new_width)])
    filename=input("Enter filename: ")
    # print result
    print(ascii_image)
    
    
    with open(filename, "w") as f:
        f.write(ascii_image)
 
# run program
main()