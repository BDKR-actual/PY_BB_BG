

import os
import random

DEFAULT_IMG_DIR = '/home/bdkr/Downloads/safe_bgs/'


# We are going to load, search, and shuffle images here
def load_images(img_list_final, arg_set, config_set):
    # Setup
    img_dir     = ""
    img_list    = []
    # path_list   = []
    is_list     = False

    # Get directory information
    if len(arg_set['d']) > 0:
        img_dir = arg_set['d']
    elif len(config_set['d']) > 0:
        img_dir = config_set['d']
    else:
        img_dir = DEFAULT_IMG_DIR

    # See if we have been passed more than one directory, then check that it/they are good.
    if ',' in img_dir:
        img_dir = img_dir.split(',')
        is_list = True
    check_dir_exists(img_dir)

    # Get images from the directory
    if is_list:
        for i_d in img_dir:
            path_actual = os.path.expanduser(i_d)
            for l_img in (os.listdir( path_actual )):
               img_list.append(path_actual+l_img)
    else:
        path_actual = os.path.expanduser(img_dir)
        for l_img in (os.listdir( path_actual )):
            img_list.append(path_actual+l_img)

    # Search the images if requested, while also making sure they actually are images
    for img in img_list:
        if 'png' in img.lower() or 'jpg' in img.lower() or 'jpeg' in img.lower():

            if arg_set['i'] != "":
                if arg_set['i'].lower() in img.lower():
                    img_list_final.append(img)
            else:
                img_list_final.append(img)

    # Shuffle and return
    random.shuffle(img_list_final)




def check_dir_exists(dir_path):
    if isinstance(dir_path, list):
        for path in dir_path:
            # path = os.path.expanduser(path)
            if os.path.isdir( os.path.expanduser(path) ):
                ...
            else:
                raise ValueError("One of the provided image directories doesn't exist!")
    else:
        if os.path.isdir( os.path.expanduser(dir_path) ):
            ...
        else:
            raise ValueError("The image directory doesn't exist!")

    return True







# awesome
