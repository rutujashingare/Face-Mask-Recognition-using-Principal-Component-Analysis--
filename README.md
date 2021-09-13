# Face Mask Recognition using Principal Component Analysis

## Objective
To create a face mask recognition algorithm that can be deployed by banks, airports and educational institutes using Principal Component Analysis.

## Principal Component Analysis
PCA is a dimensions reduction technique where in the data is compressed in a way that the main features of the data are preserved.
PCA reduces dimensions of the data and accurately decompose the face structure into the orthogonal principal components known as ‘Eigenfaces’.
PCA explains the variance-covariance structure among a set of variables through a few linear combination of these variables.

## Steps of Principal Component Analysis Algorithm 

Step 1: Input data 

Step 2: Calculate mean value of data 

Step 3: Subtract the mean value from each input data 

Step 4: Calculate Covariance matrix

Step 5: Calculate Eigen vectors and Eigen values 

Step 6: Finding the greatest eigenvalue(s) 

Step 7: Calculate Weight

## Dataset
We collected total 300 face images each of 150 for people wearing masks and not wearing masks.
https://drive.google.com/drive/folders/1M9n5s423Gr-xjNZWQgl2nWXuwrni4R23

## Pre-processed Data

![image](https://user-images.githubusercontent.com/70087327/132878408-749ce553-84da-4b00-b5a2-c3ebdc2877a7.png)


## Viola Jones Algorithm
We used Viola-Jones algorithm to detect faces from images. Viola-Jones algorithm is an object-recognition framework that allows the detection of image features in real-time. It first detects the face on the grayscale image and then finds the location on the colored image. It outlines a box and searches for a face within the that box. 

## Create a Face Vector
We created a face vector of 64x64 = 4096 components by converting two dimensional images into  a one face vector by aligning the pixels. From the numerical point of view, this large number of components i.e. 4096 components may be exaggerated for representing such images. Hence, in order to reduce the size of the data, we applied PCA method to select only the main components of our images.

## Normalization of a Face Vector
After creating a face vector, next step is to normalize all the faces of training set. We performed normalization of all the face of training set by removing common features between these faces, so that every face was left with only its unique features. For this, we removed the average face (mean face/mean of pixels) from each of face image of the dataset. Now, we are ready with our normalized face vector.

![image](https://user-images.githubusercontent.com/70087327/132878627-cc1af24d-1ce4-43a6-8d9b-c8cd3b39c69a.png)


## Covariance Matrix, Eigen Vectors and Eigen Values 
After normalizing, we calculated the covariance matrix of the normalized lower dimensional vector. The relative variance between pixels in images is represented by the covariance matrix. Later for efficient and accurate calculation with reduction of huge face space vector, we calculated eigen vectors from the covariance matrix. Eigen vectors with the highest eigen values are considered as the principal components. Below are the examples of eigenfaces which is nothing but the set of eigenvectors.

![image](https://user-images.githubusercontent.com/70087327/132878715-5efbab6a-ec69-4320-9edc-da08fcff3310.png)


## Recognition
After the successful computation of PCA representation of images and performing identification of potential facial components, we calculated weights for each of input images and compared with the test images weight. The eigen face were selected and used for the recognition. The recognition was carried out by comparing the selected features from the target image against selected features from the corresponding images. 
