import thresholding
import image
import os
import cv2
import pathlib
from pathlib import Path


typ = "map"
n = "London.png"


def image_getter(typ, n):
    parent = ""  # statement declaration
    typ = str(typ)  # to turn it into a tring just incase the use a key like type= "map"

    if typ == "map":        # if type is a map change the sting variable
        parent = "images\Maps"

    elif typ == "button":
        parent = "images\Buttons"

    elif typ == "save":
        parent = "images\Saved"

    else:
        # TODO make a return to menu or end program function
        # prolly wnt be used but here just so i will code it properly. spelling will most likely trigger this clause
        print("image Doesnt exist")

    # joins the parent_name and name together intelligently, so you don't have to include /\ to break the program.
    joined_path = os.path.join(parent,n)
    print(joined_path, "joined path")

    parent_directory = Path(joined_path).parent # finds the parent directory
    print(parent_directory, "parent dir")


    absolute_path = str(parent_directory.absolute())  # finds the absollute path so regardless of the os its works
    print(absolute_path, "abso")

    full_path = os.path.join(absolute_path, n)  # joins the absolute path of the parent and name together
    print(full_path, "full path")

    # for some reason open cv have a hard time reading multiple directories # inside one another so the i had to
    # remove the parent
    full_path = full_path.replace('\computer vision','')

    print(full_path, "full path")

    # converts the path by switching the backslash\ to Fforwar dslash to make it universal for all computers
    full_path = str(pathlib.PureWindowsPath(full_path).as_posix())


    return full_path

# map1 = image.get_image("map", 'London.png')#
# # print(map1, 72727)
# im = thresholding.im
# map2 = image.image_reader(map1)
# print(im[0][234])

# map = 'M:/22-23_CE301_olaoye_emmanuel_o\SourceFile/images/Maps/London.png'
#
# cv2.imread(map)

# im1 = image_getter(typ, n)
# print(im1)



# cv = cv2.imread(im1)
#
# print(cv)
#

# img = image.image_reader(im1)
# show = image.show_image(img)
# save = image_getter("save", "test.png")
# print(save, "save")
#
# cv2.imwrite(save, img)

# C:/Users/Manny/Documents/Capstone_Repo/22-23_CE301_olaoye_emmanuel_o\SourceFile/images/London.png
# C:\Users\Manny\Documents\Capstone_Repo\22-23_CE301_olaoye_emmanuel_o\SourceFile\images\Maps\London.png
# fixed version:
# C:\Users\Manny\Documents\Capstone_Repo\22-23_CE301_olaoye_emmanuel_o\SourceFile\images\Maps\london.png
#                                     M:\22-23_CE301_olaoye_emmanuel_o\SourceFile\images\Saved\enter.jpg
# C:\Users\Manny\Documents\Capstone_Repo\22-23_CE301_olaoye_emmanuel_o\SourceFile\computerVision\images\Maps\london.png 4

# M:\22-23_CE301_olaoye_emmanuel_o\SourceFile\images\Saved\test.png
# M:\22-23_CE301_olaoye_emmanuel_o\SourceFile\images\Saved\Lonn.png

# ggg = image.show_image(res)

# imgg = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
# assert imgg is not None, "file could not be read, check with os.path.exists()"
# plt.hist(imgg.ravel(), 256, [0, 256]);
# plt.show()

# print(np.unique(mask))


# cv2.namedWindow("orig", cv2.WINDOW_NORMAL)


# skel = cv2.imshow("skel", res)

# saving the image
# cv2.imwrite("skeleton.png", res)
# cv2.imwrite("original.png", img)
# cv2.imwrite("read_road.png", res)

# displaying on
# f = plt.subpl(1, 2)
# f = "hello"
# cv2.imshow("hellow", res)
# ax1.imshow(, cmap='gray', interpolation='nearest')

# plt.imshow(res, cmap=plt.cm.gray)
# plt.axis("off")
# plt.savefig('test2png.png', dpi=100)

# cv2.imshow("histo", gray_image)
# cv2.imshow("mask", mask)
# cv2.imshow("cam", img)
# cv2.imshow('res', res)


# image.image_reader()
# save_path = "SourceFile/computerVision/"
# image_name = "new image.png"


# path = "C:\Users\Manny\Documents\Capstone_Repo\22-23_CE301_olaoye_emmanuel_o\SourceFile\computerVision\original.png"

# img = cv2.imread(path, 0)
# thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)


# to remove the roads

# (img, (900, 650)

# img = image.resize_image(img, "absolute", 1000, 600)

spain = image.get_image("Button", 'Spain Flag.png')
text = r'M:\22-23_CE301_olaoye_emmanuel_o\Algorithims\images\Buttons\Spain Flag.png'
print(spain)
print(text)

# spain = image.image_reader(spain)
#
# image.show_image(spain)