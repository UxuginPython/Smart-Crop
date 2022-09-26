#!/usr/bin/env python3
print('Uxugin Smart Crop')
from PIL import Image
import numpy as np
def toNumpy(image):
    img_numpy=np.array(image, dtype=np.uint8)
    return img_numpy
def toList(image):
    img_numpy=np.array(image, dtype=np.uint8)
    img_list=img_numpy.tolist()
    return img_list
def toFile(image):
    img_numpy=np.array(image, dtype=np.uint8)
    img_file=Image.fromarray(img_numpy)
    return img_file
def _open(path):
    image_file=Image.open(path)
    #image_file.rotate(90, expand=1).show()
    image_list=toList(image_file)
    #toFile(image_list).rotate(90, expand=1).show()
    return image_list
def save(image, path):
    img_file=toFile(image)
    img_file.save(path)
def checkList(list_, color):
    for i in list_:
        if i!=color:
            return False
    return True
#def rowsToColumns(list_):
#    output=[]
#    row=[]
#    for i in range(len(list_)):
#        row.append(None)
#    for i in range(len(list_[0])):
#        output.append(row)
#    for x in output:
#        for y in x:
#    return output
#print(rowsToColumns([[1, 2, 3], [4, 5, 6]]))
#def rotateList(list_):
#    file=toFile(list_)
#    #output=file.transpose(Image.Transpose.ROTATE_90)
#    file_rot=file.rotate(90, expand=1)
#    file_rot.show()
#    output=toList(file_rot)
#    return output
def rotateList(list_):
    output=toNumpy(list_)
    output=np.rot90(output, 1)
    output=output.tolist()
    return output
path=input('Path of Image: ')
print('Importing...')
image=_open(path)
image=toList(image)
#print(image[0][0])
print('Cropping... 0%', end='')
while checkList(image[0], image[0][0]):
    del(image[0])
image=rotateList(image)
print('\rCropping... 25%', end='')
while checkList(image[0], image[0][0]):
    del(image[0])
image=rotateList(image)
print('\rCropping... 50%', end='')
while checkList(image[0], image[0][0]):
    del(image[0])
image=rotateList(image)
print('\rCropping... 75%', end='')
while checkList(image[0], image[0][0]):
    del(image[0])
image=rotateList(image)
print('\rCropping... 100%')
savepath=input('Path to Save: ')
save(image, savepath)
print('Saved')
