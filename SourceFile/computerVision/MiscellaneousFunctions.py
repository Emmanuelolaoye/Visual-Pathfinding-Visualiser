import os
import cv2

def displayPathOnimage(image, Path):
    #image = cv2.resize(image, ((900), (900)), interpolation=cv2.INTER_CUBIC)
    for Pixels in Path:
        cv2.circle(image, (Pixels[1], Pixels[0]), 1, (255, 100, 200), 3)

    return image

def getClosestIntersection(target, points):
    import math

    return min(points, key=lambda point: math.hypot(target[1] - point[1], target[0] - point[0]))

def get_filepaths(directory):
    """
    This function will generate the file names in a directory
    tree by walking the tree either top-down or bottom-up. For each
    directory in the tree rooted at directory top (including top itself),
    it yields a 3-tuple (dirpath, dirnames, filenames).
    """
    file_paths = []  # List which will store all of the full filepaths.

    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  # Add it to the list.

    return file_paths  # Self-explanatory.


# Run the above function and store its results in a variable.
# full_file_paths = get_filepaths(r"M:\22-23_CE301_olaoye_emmanuel_o")

# for path in full_file_paths:
#     print(path)
