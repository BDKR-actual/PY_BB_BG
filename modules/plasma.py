


from time import sleep
import os

def rotate_images(img_list, interval):
	while True:
		for img in img_list:
			set_bkg(img)
			sleep(int(interval))



def set_bkg(img_proper):
	os.system('wmsetbg --maxscale '+img_proper)
