from PIL import Image
import os
import math

# Edit the two paths below to match your own system, including what you're calling the input.jpg
export_path = "C:\\py\\image_slicer\\output/"
image = Image.open("C:/py/image_slicer/input.jpg")


imgwidth, imgheight = image.size
iterations = math.floor(imgwidth / imgheight) + 1

print("Image height: %s " % imgheight)
print("Image width: %s " % imgwidth)
print("Iterations: %s " % iterations)
print("")

for i in range(0, iterations):
    save_path = "C:\\py\\image_slicer\\img-%s.png" % i
    box = (i*imgheight, 0, min((i+1)*imgheight, imgwidth), imgheight)
    a = image.crop(box)
    
    # Debug Info
    newwidth, newheight = a.size
    print("Box {}: {}, width: {}, height: {}".format(i+1, box, newwidth, newheight))
    print("Save path: {}".format(save_path))

    try:
        a.save(save_path)
    except:
        print("Could not save image slice.")
