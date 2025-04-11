

from time import sleep
import os


def rotate_images(img_list, interval):
	int_actual = int(interval)
	while True:
		for img in img_list:
			set_bkg(img)
			sleep(int_actual)


def set_bkg(img_proper):
	os.system("nitrogen --set-zoom --head=0 '" + img_proper + "'")
	os.system("nitrogen --set-zoom --head=1 '" + img_proper + "'")
