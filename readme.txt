Detergent.py

Methods 'Get_Edge_Intensity', 'is_Blurry', 'get_emax', 'get_Edge_Map' are based on the paper 
"Blur Detection for Digital Images Using Wavelet Transform". 
('https://www.cs.cmu.edu/~htong/pdf/ICME04_tong.pdf' a paper by H. Tong, M. Li, H. Zhang, C. Zhang) 
In test.py they are used to determine which of the provided sample digital pictures are can be classified 
as blurry and which ones are sharp. (NOTE: Images that have high resolution by are focusing
on one object within the frame and thus leaving the background blurry will be classified
as blurry, hence currently working on to adding a method to separate these types of images as well and 
some other cool/useful features that deal with digital images).