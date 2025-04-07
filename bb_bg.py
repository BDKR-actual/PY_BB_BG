#!/usr/bin/env python3

# import getopt
import os
import sys
import random
sys.path.append("modules/")

import bbbg_utility
import images
import nitrogen
import plasma
import windowmaker

DEFAULT_IMG_DIR = '~/Downloads/safe_bgs/'

def main():
    # Setup
    img_list    = []
    arg_set     = {"i":"", "t":"", "c":"", "d":""}
    config_set  = {"t":"", "c":"", "d":""}
    processor   = ""
    interval    = 45                                        # A default

    # Now time for real work
    bbbg_utility.process_options(arg_set)
    bbbg_utility.process_config_file(config_set)
    images.load_images(img_list, arg_set, config_set)       # Get images from the directory, search, and shuffle
    interval = bbbg_utility.determine_interval(arg_set, config_set)

    # Determine the bg processor then hand off
    processor = bbbg_utility.determine_processor(arg_set, config_set)
    match processor:
        case "cinnamon":
           nitrogen     .rotate_images(img_list, interval)
        case "windowmaker":
           windowmaker  .rotate_images(img_list, interval)
        case 'plasma':
           plasma       .rotate_images(img_list, interval)



# Go!
main()
