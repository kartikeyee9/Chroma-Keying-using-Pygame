


import pygame 

#the code below asks the user if they require instructions. If the user responds yes, then the program will generate the instructions for them on the screen. 
instructions = str(input("Do you require instructions to use this program?"))
if instructions == "yes" or "Yes" or "YES":
	print("When you run the program, the program will ask you to input the background image name and the name of the ghost you would like to use. After doing so, the program will ask the position of the ghost image in the background image. once you run the program, it will demonstrate the background image with the picture of the ghost inside the background image\n")



#Variables assigned to ask the user which background image and the ghost image they would like to use using the input function. 
user_background_image = input("Which background image would you like to use?") 
user_ghost_image = input("Which ghost would you like to use?")


#Variables assigned to both the images (background and ghost). pygame.image.load function loads an image. It takes a string argument and returns the loaded image as a surface. 
background_image = pygame.image.load(user_background_image)
ghost_image = pygame.image.load(user_ghost_image)


#Background width and background height are assigned as a variable to the function background_image.get_rect().size which gets the dimensions of an image. It can be called on an image and will return an ordered pair that contains the width and the height of that image. 

background_width, background_height = background_image.get_rect().size
ghost_width, ghost_height = ghost_image.get_rect().size

#Setting the window of the program using the function pygame.display.set_mode with the background width and background height which was initially set in the above function. 
window = pygame.display.set_mode((background_width, background_height))


#The function below copies one image onto another. Called on an image, it takes two arguments and has no return value. The arguments are the image to be copied and an ordered pair for
#the co-ordinates for where to start copying the image.
window.blit(background_image, (0,0))


#The program below is asking the user for the x and y coordinates of the ghost. The program evaluates if the coordinates included by user come in the parameters initially set. If they don't, the program will print "The value is incorrect and out of bound". 
ghost_x = -1
while (ghost_x < 0 or ghost_x > background_width - 1):
	ghost_x = int(input("PLease input the x coordinate of the ghost image"))
	if (ghost_x < 0 or ghost_x > background_width - 1):
		print("The value is incorrect and out of bound.\n")
		

ghost_y = -1
while (ghost_y < 0 or ghost_y > background_height - 1):
	ghost_y = int(input("Please input the y coordinate of the ghost image"))
	if (ghost_y < 0 or ghost_y > background_height - 1):
		print("The value is incorrect and out of bound.\n")





# the program below uses a for function and the range function to set the height of the ghost in the background image. 
for row in range (0, ghost_height - 1):
	#the function below uses an if function to create a statement which describes the dimensions of the height of the ghost which will fit into the background picture. 
	if (int((ghost_y + row) - (ghost_height/2)) < background_height and int((ghost_y + row) - (ghost_height/2) > 0)):
		# the program below uses a for function and the range function to set the width of the ghost in the background image. 
		for pixel in range(0, ghost_width - 1): 
			#the function below uses an if function to create a statement which describes the dimensions of the width of the ghost which will fit into the background picture. 
			if (int((ghost_x + pixel) - (ghost_width/2)) < background_width and int((ghost_x + pixel) - (ghost_width/2) > 0)):
				#the function below gets the colour of the a pixel. Called on an image, it takes an ordered pair of integers as an argument and returns an ordered quadruple 					(i.e., four values) that contains the colour of the pixel in the image at those co-ordinates.
				(ghost_red, ghost_green, ghost_blue, _) = ghost_image.get_at((pixel,row))
				
				#I used an if not function below to determine, if the colour of the pixels are not green, then the program continues further.
				if(not(ghost_red == 0 and ghost_green == 255 and ghost_blue == 0)): 
					#Below is the RGB value and the function background_image.get_at gets the colour of the pixel at that point. 
					(background_red, background_green, background_blue, _) = background_image.get_at((int((ghost_x + pixel) - (ghost_width/2)), int((ghost_y + row) - (ghost_height/2))))


			

					#Average value of the colours are used to achieve the semi transperency of the pictures or to make the image translucent.  
					average_background_red = (background_red + ghost_red)/ 2
					average_background_green = (background_green + ghost_green)/2
					average_background_blue = (background_blue + ghost_blue)/2
					
					#the function below sets the colour of a pixel. Called on an image, it takes two arguments and has no return value. It takes the width and the height of the 						pictures and picks the average colours of the RGB value found before. 
					window.set_at((int((ghost_x + pixel) - (ghost_width/2)), int((ghost_y + row) - (ghost_height/2))), (average_background_red, average_background_green, average_background_blue))


#the code below forces the pygame window to stay open until the user tries to close the window. 
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
	pygame.display.update()
