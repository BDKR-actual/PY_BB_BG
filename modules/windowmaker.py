

from time import sleep
import os

def rotate_images(img_list, interval):
	int_actual = int(interval)
	while True:
		for img in img_list:
			set_bkg(img)
			sleep( int_actual )


# Something to note in the below is that the image name may have spaces or characters
# that gets bash pretty upset. Escaping the name solves this
def set_bkg(img_proper):
    print( img_proper )
    os.system("wmsetbg --maxscale '" + img_proper + "'")
