from Detergent import*
import image_slicer

detergent = Detergent()
prefix_dir = './pic/'
pics = detergent.list_files(prefix_dir)
#it works for images that are high resolution all around and no blurry parts
#check if the image is blurry
for pic in pics:
	img_path = prefix_dir + pic
	print(img_path)
	print("focused: " + str(detergent.test_focus(img_path)))
	#have to play around with this threshold number (10 would work for most)
	(blur, extent) = detergent.Get_Edge_Intensity(img_path) 
	detergent.is_Blurry(blur, extent)
	print("")

<<<<<<< HEAD



=======
>>>>>>> 03202a96993b8aff5a49e5dfe6b17aaeea7ace75
