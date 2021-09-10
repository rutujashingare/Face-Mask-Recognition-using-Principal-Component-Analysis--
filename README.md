# Face Mask Recognition using Principal Component Analysis

## Introduction
Face mask Recognition is a Biometric Technology of identifying an individual wearing a mask by comparing live capture or digital image data with the stored record for that person.

The COVID–19 virus can be spread through contact and contaminated surfaces. There are so many essential equipment’s needed to fight against the Corona virus. One of such most essential is Face Mask. Firstly, a face mask was not mandatory for everyone but as the day progresses scientists and Doctors have recommended everyone to wear a face mask. So to detect whether a person is wearing Face Mask or not is an essential process to implement in the society currently which can be used for various applications like at the airport, hospitals, offices, schools, etc. This system can be of great importance at airports to detect travelers whether they are wearing a mask or not and at schools to ensure students are wearing a face mask for their safety. Face masks have been employed as a public and  personal health control measure against the spread of the COVID-19 pandemic. In both community and healthcare settings, their use is intended as a source control to limit transmission of the virus and personal protection to prevent infection.


## Dataset
We collected total 300 face images each of 150 for people wearing masks and not wearing masks.
https://drive.google.com/drive/folders/1M9n5s423Gr-xjNZWQgl2nWXuwrni4R23

## Pre-processed data
![image](https://user-images.githubusercontent.com/70087327/130550778-1896608c-b28a-4410-8ea4-19103bf606da.png)
![image](https://user-images.githubusercontent.com/70087327/130550802-b713c7c5-3c33-4576-993b-648a3e8f3422.png)


## Viola Jones Algorithm
We used Viola-Jones algorithm to detect faces from images. Viola-Jones algorithm is an object-recognition framework that allows the detection of image features in real-time. It first detects the face on the grayscale image and then finds the location on the colored image. It outlines a box and searches for a face within the that box. 

## Create a face vector
We created a face vector of 64x64 = 4096 components by converting two dimensional images into  a one face vector by aligning the pixels. From the numerical point of view, this large number of components i.e. 4096 components may be exaggerated for representing such images. Hence, in order to reduce the size of the data, we applied PCA method to select only the main components of our images.

## Steps of Principal Component Analysis algorithm 
Step 1: Input data 
Step 2: Calculate mean value of data 
Step 3: Subtract the mean value from each input data 
Step 4: Calculate Covariance matrix 
Step 5: Calculate Eigen vectors and Eigen values 
Step 6: Finding the greatest eigenvalue(s) 
Step 7: Calculate Weight

## Normalization of a face vector
After creating a face vector, next step is to normalize all the faces of training set. We performed normalization of all the face of training set by removing common features between these faces, so that every face was left with only its unique features. For this, we removed the average face (mean face/mean of pixels) from each of face image of the dataset. Now, we are ready with our normalized face vector.

## Covariance Matrix, Eigen vectors and Eigen values 
After normalizing, we calculated the covariance matrix of the normalized lower dimensional vector. The relative variance between pixels in images is represented by the covariance matrix. Later for efficient and accurate calculation with reduction of huge face space vector, we calculated eigen vectors from the covariance matrix. Eigen vectors with the highest eigen values are considered as the principal components.

## Weight calculation
Now, for the recognition, we calculated weights for each of input images and compared with the test images weight. In this way, system recognized the masked faces with the matching closest face from the training set.
