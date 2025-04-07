

import getopt
import sys
import os

DEFAULT_BG_PROCESSOR    = 'windowmaker'
DEFAULT_BG_INTERVAL     = '45'


def show_usage():
	print(f'{sys.argv[0]}')
	print("\th	-> Show this help")
	print("\ti	-> Show images matching an image name or partial name")
	print("\tt	-> Specify the interval between image changes")
	print("\tc	-> Specify window manager. Options are wmsetbg, nitrogen, and plasma")
	print("\td	-> Custom directory or multiples. Seperate directories with commas")


def process_options(arg_dset):
    passed_in 	= sys.argv[1:]
    opts, args 	= getopt.getopt(passed_in, 'i:t:c:d:h')

    # Now iterate over the options and store what's found the argument data set
    for opt_item in opts:
        match opt_item[0]:
            case '-i':
                arg_dset["i"] = opt_item[1]
            case '-t':
                arg_dset["t"] = opt_item[1]
            case '-c':
                arg_dset["c"] = opt_item[1]
            case '-d':
                arg_dset["d"] = opt_item[1]

        if opt_item[0] == '-h':
            show_usage()
            os._exit(1)      # If we don't exit here, we'll start showing images
            return


def process_config_file(config_dset):
    # Now try to open the config file, which is hardcoded for now
    config_path = '~/.config/bb_bg/config_py'
    with open(os.path.expanduser(config_path), 'r') as file:
        lines = file.readlines()

    # loop over the lines and either ignore or place values into the config data set
    for line in lines:
        line        =line.rstrip()
        if len(line)== 0:
            continue
        line_boom   =line.split(':')

        match line_boom[0]:
            case 'd':
                config_dset['d'] = line_boom[1]
            case 'c':
                config_dset['c'] = line_boom[1]
            case 't':
                config_dset['t'] = line_boom[1]


def determine_processor(arg_set, config_set):
    # Setup
    proc    = ''

    # Let's get that data
    if len(arg_set['c']) > 0:
        proc = arg_set['c']
    elif len(config_set['c']) > 0:
        proc = config_set['c']
    else:
        proc = DEFAULT_BG_PROCESSOR

    # Just in case
    if proc == 'wmsetbg' or proc == 'blackbox' or proc == 'fluxbox':
        proc = 'windowmaker'

    return proc


def determine_interval(arg_set, config_set):
    # Setup
    interval    = ''

    # Let's get that data
    if len(arg_set['t']) > 0:
        interval = arg_set['t']
    elif len(config_set['t']) > 0:
        interval = config_set['t']
    else:
        interval = DEFAULT_BG_INTERVAL

    return interval
