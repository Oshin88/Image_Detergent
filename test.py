from Detergent import*

detergent = Detergent()
pics = detergent.ListFiles('./pic/')
prefix_dir = "./pic/"

'''
for pic in pics:
	img_path = prefix_dir + pic
	print(img_path)
	(blur, extent) = detergent.Get_Edge_Intensity(img_path, 35)
	detergent.is_Blurry(0.05, blur, extent) 
'''

img_path = './pic/blurry4.jpg'
(blur, extent) = detergent.Get_Edge_Intensity(img_path, 35)
detergent.is_Blurry(0.05, blur, extent) 



