

# Python variant of Blackbox Background (bb_bg). Also written in Rust and PHP. 

## So what is BlackBox Background? 

This is something I originally wrote a long time ago ('02 I think) in PHP. And again in Python and Ruby but I lost those files. This is a complete new write of the project and now very similar (in terms of 
logic and ability) to the Rust variant. What it does is loop over a list of images and resets the desktop background at a specified interval. And of course, there are arguments that allow specifying the interval and searching images based on search criteria.

At the time, I used Blackbox and Windowmaker window managers. They both use the [wmsetbg](https://www.windowmaker.org/docs/manpages/wmsetbg.html) tool for setting the background. Now with this version in
Rust, it works using Cinnamon, Fluxbox, Blackbox, Windowmaker, and KDE Plasma.

Something to note here... Cinnamon uses a tool called Nitrogen to set backgrounds. Expensive (LOL), but powerful. It, by itself can do most of what this little application can do. BUT IT IS EXPENSIVE!
THIS IS A WARNING! Setting low intervals (less than 10 seconds) while on Cinnamon (using Nitrogen) will affect how responsive your system is, or stops being. Over 10 seconds should be fine, but your
system is likely different than mine so your mileage may vary. I'm running this on a refurb'ed Dell T3600 Workstation with 32gigs and 6 cores. With memory usage as low as 6gb, I'm seeing affects on
system responsiveness when running intervals less than 10 seconds. So don't do it. You've been warned. :-)

Usage is simple. Here is the help output:

```
	h	-> Show this help
	i	-> Show images matching an image name or partial name
	t	-> Specify the interval between image changes
	c	-> Specify window manager. Options are wmsetbg, nitrogen, and plasma
	d	-> Custom directory or multiples. Seperate directories with commas
```

There is a config file. It should live in /home/you/.config/bb_bg/ and is named config_py. An example:

```
d:~/Downloads/images/,~/Downloads/BGS/world_super_bike/
c:wmsetbg
t:45
h:2

```

Yes, you need to create the file and store it at the location mentioned above. You could copy the example above as the contents of the file. Note the "~" at the start of those paths. Those are not 
required and probably better not used if you don't understand what they are. The last thing concerning the directory entries is that there should be no spaces around the commas.

"c" is important. The options are nitrogen, wmsetbg, and plasma. Not too interested in doing any others but we can add the functionality here if you write it.

If the config file isn't present, the application will exit.

As you are are likely pretty smart (since you've read this far), it's prolly obvious that the app will use config file settings unless you specify them as arguments. The
only thing not represented in the config file is the "-i" argument. With this argument you can specify that images that match a search string will be used.

>bb_bg -t 15 -i vel

The above command will change the background every 15 seconds and only use images where the name matches (in some way) the search term "vel" (for [Vel Sartha](https://duckduckgo.com/?t=h_&q=vel+sartha&iax=image>
The match is fuzzy so you don't have to know the exact name of the image or match case. Image titles like VeL_s_01.png will be matched when using "VEL", "vel", or even "vE". "Ve" is likely to match more than
you were interested in however.


## So where are we? / Change log

* All of the processors for the different window managers have the same logic. Each can be changed based on what that procressor is capable of. The intent is to update the Cinnamon / Nitrogen processor 
to show different images on different monitors as it's capable of doing AND currently does in the Rust version. After this one, I'll likely explore doing the same with Windowmaker. 
* For KDE Plasma, there is currently a tool written in Python that sets backgrounds. I'd like to incorporate it's logic into this (with the permission of the owner of course). 


## In closing

I hope this is fun for you. I enjoy it. I initially wrote this because too me it's cool to be spun on coffee and write code in a transparent terminal with the background changing every minute or so.
Cool music playing, cool code being written, and cool pics of cars, bikes, planes, or peeps cycling in the background.

Drop me a line! :-)\
Cheers


















