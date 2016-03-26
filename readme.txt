Detergent.py

Methods 'Get_Edge_Intensity', 'is_Blurry', 'get_emax', 'get_Edge_Map' are based on the paper 
"Blur Detection for Digital Images Using Wavelet Transform". 
('https://www.cs.cmu.edu/~htong/pdf/ICME04_tong.pdf' a paper by H. Tong, M. Li, H. Zhang, C. Zhang) 
In test.py they are used to determine which of the provided sample digital pictures are can be classified 
as blurry and which ones are sharp. (NOTE: Images that have high resolution by are focusing
on one object within the frame and thus leaving the background blurry will be classified
as blurry, hence currently working on to adding a method to separate these types of images as well and 
some other cool/useful features that deal with digital images).


(Implemented in the get_Edge_Map)
Rule1: if E max1(k,l) > threshold or
Emax2(k,l) > threshold or Emax3(k,l) > threshold ,
(k,l) is an edge point.

Rule2: For any edge point (k,l) , if
Emax1(k,l)>Emax2(k,l)>Emax3(k,l) , (k,l) is Dirac-Structure or Astep-Structure.

Rule3: For any edge point (k,l) , if Emax1(k,l)<Emax2(k,l)<Emax3(k,l) , (k,l) is
Roof-Structure or Gstep-Structure.

Rule4: For any edge point (k,l) , if
Emax2(k,l) > Emax1(k,l) and
Emax2(k,l) > Emax3(k,l) ,(k,l) isRoof-Structure. Rule5: For any Gstep-Structure or Roof-Structure edge point (k,l) , if E max1(k,l) < threshold , (k,l) is more likely to be in a blurred image.


------------------------------------------------------------------------------------------------------


Step1: Perform algorithm 1 on the given image;

Step2: Use Rule 1 to find all edge points. Let Nedge be the total number of them;

Step3: Use Rule 2 to find all Dirac-Structure and Astep-Structure edge points. Let Nda be the total
number of them;

Step4: Use Rule 3 and Rule 4 to find all Roof-
Structure and Gstep-Structure edge points. Let Nrg be
the total number of them;

Step5: Use Rule 5 to find all Roof-Structure and Gstep-Structure edge points that have lost their
sharpness. Let Nbrg be the total number of them;

Step6: Calculate the ratio of Dirac-Structure and
close to zero;

Step7: Calculate how many Roof-Structure and Gstep Structure edges are blurred:
BlurExtent = Nbrg/Nrg.
output BlurExtent as blur cofident coefficient for the image.


------------------------------------------------------------------------------------------------------

To determine if the given image is focused we use the following methods 'fft' (Fast Fourier Transform)
and 'test_focus'. NOTE: Gaussian_Laplace is not used but rather might be useful for analysis and 
future modifications/statistical analysis. NOTE: Blur test might fail on an image which is in focus,
since it might have blurry parts which would fail the blur test.

methods:

fft(image_path) -> average of highest frequencies within the provided image

test_focus(image_path, threshold = 300) -> if the provided image's average frequency is >= 300 then
										   the image is in focus



------------------------------------------------------------------------------------------------------

Folders:

'./pic/'              ->  contains sample pictures for testing purposes (NOTE: I do not own the rights 
      					  to the provided images they are for educational purposes only, all the rights 
      					  belong to the authors of the images.)

'./resources/'        ->  contains the scientific paper (pdf) for the 
                          "Blur Detection for Digital Images Using Wavelet Transform". 




------------------------------------------------------------------------------------------------------

Results based on the sample images provided within the './pic/' path (output of the test.py):

./pic/blurry.jpg
avr freq: 162.807643461
focused: False
Image is blurry. The blur extent is 1.0

./pic/blurry1.jpg
avr freq: 223.188513399
focused: False
Image is blurry. The blur extent is 0.7273909006499536

./pic/blurry2.jpg
avr freq: 293.478828637
focused: False
Image is blurry. The blur extent is 1.0

./pic/blurry3.jpg
avr freq: 275.698180133
focused: False
Image is blurry. The blur extent is 1.0

./pic/blurry_outlier.jpg
avr freq: 329.182987421
focused: True
Image is not blurry. 0.7362204724409449

./pic/focused1.jpg
avr freq: 352.073538241
focused: True
Image is blurry. The blur extent is 1.0

./pic/focused2.jpg
avr freq: 600.001343694
focused: True
Image is blurry. The blur extent is 1.0

./pic/focused3.jpg
avr freq: 322.951962732
focused: True
Image is blurry. The blur extent is 1.0

./pic/focused4.jpg
avr freq: 607.884073166
focused: True
Image is blurry. The blur extent is 1.0

./pic/focused5.jpg
avr freq: 321.428007723
focused: True
Image is blurry. The blur extent is 0.9994565873686753

./pic/focused_and_not_blurry.jpg
avr freq: 241.457562504
focused: False
Image is not blurry. 0.6414598540145985

./pic/focused_outlier.png
avr freq: 339.641709053
focused: True
Image is blurry. The blur extent is 1.0

./pic/focused_outlier1.jpg
avr freq: 115.350247097
focused: False
Image is blurry. The blur extent is 0.8317329675354367

./pic/not_blurry.jpg
avr freq: 368.804667576
focused: True
Image is not blurry. 0.01057928009289124

./pic/not_blurry1.jpg
avr freq: 223.302124968
focused: False
Image is not blurry. 0.14719726144629866

./pic/not_blurry2.jpg
avr freq: 280.04170731
focused: False
Image is not blurry. 0.009106984969053935

./pic/not_blurry3.jpg
avr freq: 208.06130711
focused: False
Image is not blurry. 0.17650657693484245

./pic/not_blurry_outlier.jpg
avr freq: 135.110730833
focused: False
Image is blurry. The blur extent is 0.6017763541059988

./pic/outlier.jpg
avr freq: 239.328366547
focused: False
Image is blurry. The blur extent is 1.0



NOTE: Further analysis might be required to further close the gap on the images marked as outliers.
       ex. 'not_blurry_outlier.jpg': should be marked as 'Not Blurry'

            'focused_outlier.jpg': marked as focused however it is based on user's opinion since
            it is not 100% focused nor definitively blurry or out of focus

            'focused_outlier.jpg': marked as not focused however the image is focused 

------------------------------------------------------------------------------------------------------
