I used python 3.5 for this dont judge me :|

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
