from Detergent import*

detergent = Detergent()
pics = detergent.ListFiles('./pic/')
prefix_dir = "./pic/"

#iterates through all the provided images within the pic folder
for pic in pics:
	img_path = prefix_dir + pic
	print(img_path)
	(blur, extent) = detergent.Get_Edge_Intensity(img_path, 35)
	detergent.is_Blurry(0.05, blur, extent) 
