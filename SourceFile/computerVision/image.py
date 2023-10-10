import cv2
import time
import os
import pathlib
from pathlib import Path


# def get_image(typ, nme):  # parameters: type to depreciate file location and nme to get the name
# parent_directory = ""  # statement declaration
# typ = str(typ)
#
# if typ == "map":
#     parent_directory = "images\Maps"
# elif typ == "button":
#     parent_directory = "images\Buttonsa"
# else:

#     print("image Doesnt exist")
#
# full_path = parent_directory + nme
#
# print(full_path, 1)
#
# path = Path(full_path).parent
# print(path, 2)
# absolute = str(path.absolute()) + nme
#
# p = pathlib.PureWindowsPath(parent_directory).joinpath(nme).as_posix()
# #
# print(p, 3)
#
# absolute = absolute.replace('\computerVision', '')
#
#
#
# return absolute

def get_image(typ, n):
    parent = ""  # statement declaration
    typ = str(typ)  # to turn it into a tring just incase the use a key like type= "map"

    if typ.lower() == "map":
        parent = "images\Maps"  # if type is a map change the sting variable
    elif typ.lower() == "button":
        parent = "images\Buttons"
    elif typ.lower() == "save":
        parent = "images\Saved"
    else:
        # TODO make a return to menu or end program function
        # prolly wnt be used but here just so i will code it properly. spelling will most likely trigger this clause
        print("image Doesnt exist")

    # joins the parent_name and name together intelligently, so you don't have to include /\ to break the program.
    joined_path = os.path.join(parent, n)
    #print()

    parent_directory = Path(joined_path).parent  # finds the parent directory

    absolute_path = str(parent_directory.absolute())  # finds the absollute path so regardless of the os its works
    #print(absolute_path, 2)

    full_path = os.path.join(absolute_path, n)  # joins the absolute path of the parent and name together

    full_path = full_path.replace('\Gui',
                                  '')

    full_path = full_path.replace('\computerVision',
                                  '')  # for some reason open cv have a hard time reading multiple directories # inside one another so the i had to remove the parent
   #print(full_path, 5)

    if typ.lower() == "button":
        return repr(full_path)
    else:
        full_path = pathlib.PureWindowsPath(full_path).as_posix()  # converts the path by switching the backslash\ to Fforwardslash to make it universal for all computers

        return full_path


def image_reader(name):
    img = cv2.imread(name)

    return img


def show_image(img):
    cv2.imshow("hh", img)
    cv2.waitKey(0)

    # closing all open windows
    cv2.destroyAllWindows()


def resize_image(image, res_type, width, length):
    ln = image.shape[0]
    wd = image.shape[1]

    if res_type == "relative":
        return cv2.resize(image, ((wd // width), (ln // length)), interpolation=cv2.INTER_CUBIC)

    elif res_type == "absolute":
        return cv2.resize(image, (width, length), interpolation=cv2.INTER_CUBIC)


def save_image(name):  # type, img, nme
    parent_name = "images\Saved"
    to_remove = '\computerVision'

    path = Path(parent_name).parent
    hello = Path(str(path)).parent

    absolute = str(path.absolute())
    absolute = absolute.replace(to_remove, parent_name)

    absolute = pathlib.PureWindowsPath(absolute).joinpath(name+"png").as_posix()

    return absolute


#
# home = r'\home\build\test\sandboxes'
# todaystr = '042118'
# new = 'new_sandbox/'
#
#
# p = pathlib.PureWindowsPath(home).joinpath(new).as_posix()
#
# print(p)

# save_image("hello")
#
# img1 = get_image("map", '\London.png')
#
# print(img1, 77)
#
# print()
# print()
#
# print()
# print()
#
# img = cv2.imread(img1)
# print(img)
