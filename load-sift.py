from skimage import io 
from PIL import Image
from subprocess import call


image = Image.open('sample.png')
image.save('sample.pgm')

call("./sift < book.pgm > chck.key", shell=True)

image = open('chck.key')

rv = io.load_sift(image)
print rv