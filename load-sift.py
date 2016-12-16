from skimage import io 

image = open('book.key')
rv = io.load_sift(image)

print rv