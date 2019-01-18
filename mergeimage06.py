# ============================================================
#                                                             
# Student Name (as it appears on cuLearn): Yiming He     
# Student ID (9 digits in angle brackets): <101090748>        
# Course Code (for this current semester): COMP1405A          
#                                                             
# ============================================================

#import the function from the pygame library
import pygame

#ask the user if they require instructions.
introduction=input("Do you need instructions?(yes/no)").upper()

#introduce when user answer yes.
if introduction=="YES":
	print("In this program, you can choice one background image and one ghost image, you can put this ghost image anywhere you want on top of the background .")

#start when user answer no.
elif introduction=="NO":
	print("ok,let's start!")

#start when user answer others.
else:
	print("ok,let's start!")

#this initializes pygame
pygame.init()

#this ask user to input the ghost image name they want.
ghi=input("which ghost image you want?")

#this ask user to input the background image name they want.
bgi=input("which background image you want?")

#this load the background image
bg=pygame.image.load(bgi)

#this find the width and height of background image
(w,h)=bg.get_rect().size

#this creats a surface
#the dimensions of this surface are same as background image's.
bgs=pygame.display.set_mode((w,h))

#this set the width of background as bw
bw=w

#this set the height of background as bh
bh=h

#this copys background image onto the surface.
bgs.blit(bg,(0,0))

#this actually updates the screen what have done.
pygame.display.update()

#this use postcondition loop by boolean flag to check if the width that user input is not overside.
flag=True
while flag:
	cx=int(input("what is the x co-ordinates of the center to put the ghost image?("+str(bw)+","+str(bh)+")"))
	if 0<=cx<=bw:
		flag=False

#this use postcondition loop by boolean flag to check if the height that user input is not overside.
flag=True
while flag:
	cy=int(input("what is the y co-ordinates of the center to put the ghost image?("+str(bw)+","+str(bh)+")"))
	if 0<=cy<=bh:
		flag=False

#this load the ghost image
gh=pygame.image.load(ghi)

#this find the width and height of background image
(ghw,ghh)=gh.get_rect().size

#use nested loop to check of the pixels. and copy the pixel that average the red,green,and blue values of the non-green from the ghost onto background image.
for y in range(ghh):
	for x in range(ghw):
		bgx=cx-int(ghw/2)+x
		bgy=cy-int(ghh/2)+y
		(redg,greeng,blueg, _)=gh.get_at((x,y))
		if (not(redg,greeng,blueg,)==(0,255,0)) and ((0<=bgx<bw) and (0<=bgy<bh)):
			(redb,greenb,blueb, _)=bg.get_at((bgx,bgy))
			bgs.set_at((bgx,bgy),((redg+redb)/2,(greeng+greenb)/2,(blueg+blueb)/2))

#this actually updates the screen what have done.
pygame.display.update()

#this force the pygame window to stay open until the user tries to close the window
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
	pygame.display.update()
