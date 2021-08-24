# Face Mask Recognition using Principal Component Analysis
Face mask Recognition is a Biometric Technology of identifying an individual wearing a mask by comparing live capture or digital image data with the stored record for that person.

The COVID–19 virus can be spread through contact and contaminated surfaces. There are so many essential equipment’s needed to fight against the Corona virus. One of such most essential is Face Mask. Firstly, a face mask was not mandatory for everyone but as the day progresses scientists and Doctors have recommended everyone to wear a face mask. So to detect whether a person is wearing Face Mask or not is an essential process to implement in the society currently which can be used for various applications like at the airport, hospitals, offices, schools, etc. This system can be of great importance at airports to detect travelers whether they are wearing a mask or not and at schools to ensure students are wearing a face mask for their safety. Face masks have been employed as a public and  personal health control measure against the spread of the COVID-19 pandemic. In both community and healthcare settings, their use is intended as a source control to limit transmission of the virus and personal protection to prevent infection.

Face masks have been employed as a public and  personal health control measure against the spread of the COVID-19 pandemic. In both community and healthcare settings, their use is intended as a source control to limit transmission of the virus and personal protection to prevent infection.
Types of Face Mask Recognition :
1. Based on Local Regions                                    2. Based on Global Appearance

## Dataset
https://drive.google.com/drive/folders/1M9n5s423Gr-xjNZWQgl2nWXuwrni4R23

## Pre-processed data
![image](https://user-images.githubusercontent.com/70087327/130550778-1896608c-b28a-4410-8ea4-19103bf606da.png)
![image](https://user-images.githubusercontent.com/70087327/130550802-b713c7c5-3c33-4576-993b-648a3e8f3422.png)

## Haar Cascade Classifier 
Haar Cascade Classifier is based on the Viola-Jones Recognition algorithm which is trained by giving some input images and training a classifier that identifies a face with mask.  Haar Cascade Classifier is a machine learning object Recognition algorithm used to identify objects in an image trained by superimposing the positive image over a set of negative images.

## Processed data
![image](https://user-images.githubusercontent.com/70087327/130550669-31eafe5b-cd30-45bb-95e5-64a3136b9083.png)
![image](https://user-images.githubusercontent.com/70087327/130550699-49859d61-1f8a-4d38-bba0-647f914aef5a.png)

# Principal Component Analysis
PCA is a dimensions reduction technique where in the data is compressed in a way that the main features of the data are preserved.
PCA reduces dimensions of the data and accurately decompose the face structure into the orthogonal principal components known as ‘Eigenfaces’.
PCA explains the variance-covariance structure among a set of variables through a few linear combination of these variables.

## Steps for Face Mask Recognition
STEP 1

A : PREPARING THE TRAINING IMAGES
Obtain training face images of with mask and without mask I1, I2, I3, I4, . . . . . ., IK

B: PREPARING THE DATASET
Each image is transformed into a face vector (𝚪𝐢) of dimension N2x1 and placed into a set 
 𝑆= {𝛤1, 𝛤2, ……, 𝛤𝐾}  
Here, K depends on the number of train images and S is a variable which loads all images. 

STEP 2 : COMPUTE THE MEAN FACE VECTOR     
x̄=  1/𝐾  ∑2▒Г 𝐾               
Here x̄ is a mean face vector 

STEP 3 : SUBTRACT THE MEAN FACE VECTOR
We subtract the mean face from each image of the dataset which is called normalization.
𝝓_𝒏= 𝜞𝒏−"x̄"
                           D = {φ1 , φ2, φ3,….φK }
 Here D is a new matrix generated.
 
STEP 4 : CALCULATE THE COVARIANCE MATRIX
           𝐂      = DDT
                    = {D (N2 X K) DT (Kx N2) } (N2xN2)
Here 𝑫 = [𝝓_𝟏, 𝝓_𝟐, ……..,φ𝐾] (N2 X K)

STEP 5 : CALCULATE EIGENVECTOR & EIGENVALUES REDUCING HUGE FACE VECTOR 
Since ‘ C ’ is a Covariance matrix, we have to find the eigenvectors of it.
Calculating eigenvectors of ‘ C ‘ is tedious task as it is a huge matrix and its dimension is N2xN2  
Now, we need to calculate weight which is compared with test image weight.

STEP 6: KEEP EIGENVECTORS CORRESPONDING TO THE K LARGEST EIGENVALUES
We have 130 principal components and each principal component is a linear combination of all variables. 

STEP 7 : CALCULATE WEIGHTS FOR THE TRAINING IMAGES
The feature weight for the training image can be calculated as 
ω_𝑘= 𝑣_^𝑇 (Γn−"x̄" )
The weights obtained above form a vector as 
Ωi = [ω_1, ω_2, ……, ω_𝐾]

## Euclidean Distance
The distance between two points defined as the square root of the sum of the squares of the differences between the corresponding coordinates of the points
The distance between two groups can be computed based on the length of the straight line drawn from one groups to another. This is commonly known as the Euclidean distance. 
𝝎_𝒕𝒆𝒔𝒕= 𝒗_^𝑻 (𝜞_𝒕𝒆𝒔𝒕−"x̄")
         Ωtest =[𝝎_𝟏, 𝝎_(𝟐 ), ………,𝝎_𝒌 ]
𝜺_𝒌=√(〖‖𝛀_𝐭𝐞𝐬𝐭− 𝜴_𝒊 ‖〗^𝟐  )

## Eigenface Approach
Eigenfaces which are also referred to as Ghostly images are the Eigenvectors of Covariance Matrix of the dataset.
This approach is mainly used to represent the input data efficiently where each individual can be represented in terms of linear combination of eigenfaces.
This approach transforms faces into a small set of essential characteristics, eigenfaces which are the main components of the initial set of learning images i.e. training set.

## Training Image:
![image](https://user-images.githubusercontent.com/70087327/130551265-120aa6f3-776d-43cf-8f1f-2fc09d9c0ced.png)

## Eigenface:
![image](https://user-images.githubusercontent.com/70087327/130551296-c5b3f15f-f205-46ad-8cdd-fbd0628a1fe9.png)

## Conclusion
The Euclidean approach classifies 75% of the tests correctly.
The feature extracted from masked face is less than non-masked face.
PCA gives a good recognition rate for masked images.
