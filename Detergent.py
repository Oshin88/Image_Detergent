from PIL import Image
from imutils import paths
import argparse
import glob, os
import cv2
import numpy
import pywt

class Detergent:
	pass

	#returns the list of all the images with known formats
	def ListFiles(self, path):
		#considering both capital and normal size font for exntension
		extension_list = [ "JPG", ".jpg",  ".TIFF", ".tiff", ".PNG", ".png"] 
		img_list = [file for file in os.listdir(path) if file.endswith(tuple(extension_list))]
		return img_list


	# determines the laplacian variance value of the given image path
	def Get_Laplacian_Variance(self, image_path):
		img = cv2.imread(image_path)
		laplacian_variance = cv2.Laplacian(img, cv2.CV_64F).var()
		return laplacian_variance


	#calculating local maxima in each window (intensity of the edge)
	def Get_Edge_Intensity(self, image_path, threshold):
		image = cv2.imread(image_path)
		pic_file = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		x = numpy.asarray(pic_file)
		x_cropped=x[0:(numpy.shape(x)[0]/16)*16 - 1,0:(numpy.shape(x)[1]/16)*16 - 1]
		LL1,(LH1,HL1,HH1) = pywt.dwt2(x_cropped, 'haar')
		LL2,(LH2,HL2,HH2) = pywt.dwt2(LL1, 'haar')
		LL3,(LH3,HL3,HH3) = pywt.dwt2(LL2, 'haar')
		#calculate Emap for each of the 3 quadrants
		Emap1 = numpy.sqrt(numpy.square(LH1) + numpy.square(HL1) + numpy.square(HH1))
		Emap2 = numpy.sqrt(numpy.square(LH2) + numpy.square(HL2) + numpy.square(HH2))
		Emap3 = numpy.sqrt(numpy.square(LH3) + numpy.square(HL3) + numpy.square(HH3))
		#based on the calculated emap values calc emax for each of the 8*8 4*4 and 2*2
		Emax1 = self.get_emax(Emap1, 8, 8)
		Emax2 = self.get_emax(Emap2, 4, 4)
		Emax3 = self.get_emax(Emap3, 2, 2)
		return self.get_Edge_Map(Emax1, Emax2, Emax3, threshold)


	#determine blurriness based on the blur and the extent
	def is_Blurry(self, min_zero, blur, extent):
		if blur < min_zero:
			print('Image is blurry. The blur extent is ' + str(extent))
			return True
		else:
			print('Image is not blurry.' + str(extent))
			return False


	# returns a matrix with maximum emap values based on the window size and the scale
	def get_emax(self, emap, scale, window_size):
		h = int(numpy.shape(emap)[0] / scale)		
		w = int(numpy.shape(emap)[1] / scale)
		Emax = numpy.zeros(shape=(h, w))
		vertical_index = 0
		increment = window_size - 1

		for i in range(0, h):
			#print("i: " + str(i))
			horizontal_index = 0
			for j in range(0, w):
				#print("j: " + str(j))
				#get maximum window value within the given window
				#size of the window range is determined by the increment
				max_window = numpy.max(numpy.max(emap[vertical_index : vertical_index + 
							 increment, horizontal_index : horizontal_index + increment]))
				Emax[i, j] = max_window
				horizontal_index += 1
			vertical_index += 1

		return Emax


	#given the Emax1, Emax2, and Emax3 construct an Edge Map
	#threshold is the level of tolerance towards the extent of the image sharpeness
	def get_Edge_Map(self, Emax1, Emax2, Emax3, threshold):
		edge = 0
		da   = 0
		rg   = 0
		brg  = 0
		h = numpy.shape(Emax3)[0]
		w = numpy.shape(Emax3)[1]
		
		for i in range(0, h - 1):
			for j in range(0, w):
				emax1 = Emax1[i, j]
				emax2 = Emax2[i, j]
				emax3 = Emax3[i, j]
				emax = max(max(emax1, emax2), emax3)
				#print('emax: ' + str(emax))
				if emax > threshold:
					edge += 1
					if emax1 > emax2 and emax2 > emax3:
						da += 1
					if emax1 < emax2 and emax2 < emax3:
						rg += 1
						if emax1 < threshold:
							brg += 1
					if emax2 > emax1 and emax2 > emax3:
						rg += 1
						if emax1 < threshold:
							brg += 1

		if edge == 0:
			blur = 0
		else:
			blur = da / edge

		#for some blurry images yield rg = 0 and to avoid division by 0 we set extent = 0
		if rg == 0:
			#print('rg = 0')
			extent = 1.0
		else:
			extent = brg / rg					
		return (blur, extent)



	if __name__ == "__main__":
		main()
