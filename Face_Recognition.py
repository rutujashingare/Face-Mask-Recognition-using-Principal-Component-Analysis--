import cv2
import time
import numpy as np

# importing algorithms
from PCA import pca_class
from TwoDPCA import two_d_pca_class
from TwoD_Square_PCA import two_d_square_pca_class

# importing feature extraction classes
from images_to_matrix import images_to_matrix_class
from images_matrix_for_2d_square_pca import  images_to_matrix_class_for_two_d
from dataset import dataset_class

# Algo Type (pca)
algo_type = "pca"


#for single image = 0

reco_type = 0

#No of images For Training(Left will be used as testing Image)
No_of_images_train_from_each_data = 90
dataset_obj = dataset_class(No_of_images_train_from_each_data)


#Data For Training
images_names = dataset_obj.images_name_for_train
y = dataset_obj.y_for_train
no_of_elements = dataset_obj.no_of_elements_for_train
target_names = dataset_obj.target_name_as_array

#Data For Testing
images_names_for_test = dataset_obj.images_name_for_test
y_for_test = dataset_obj.y_for_test
no_of_elements_for_test = dataset_obj.no_of_elements_for_test


training_start_time = time.process_time()
img_width, img_height = 64, 64

if algo_type == "pca":
    i_t_m_c = images_to_matrix_class(images_names, img_width, img_height)
else:
    i_t_m_c = images_to_matrix_class_for_two_d(images_names, img_width, img_height)

scaled_face = i_t_m_c.get_matrix()

if algo_type == "pca": 
    cv2.imshow("Original Image" , cv2.resize(np.array(np.reshape(scaled_face[:,1],[img_height, img_width]), dtype = np.uint8),(200, 200)))
    cv2.waitKey()
else:
    cv2.imshow("Original Image" , cv2.resize(scaled_face[0],(200, 200)))
    cv2.waitKey()

#Algo
if algo_type == "pca":
    my_algo = pca_class(scaled_face, y, target_names, no_of_elements, 90)
elif algo_type == "2d-pca":
    my_algo = two_d_pca_class(scaled_face, y, target_names)
else:
    my_algo = two_d_square_pca_class(scaled_face, y, target_names)


new_coordinates = my_algo.reduce_dim()
if algo_type == "pca":
    my_algo.show_eigen_face(img_width, img_height, 64, 150, 0)
   
   
    
    
 
if algo_type == "pca": 
    cv2.imshow("After PCA Image", cv2.resize(np.array(np.reshape(my_algo.original_data(new_coordinates[1, :]), [img_height, img_width]), dtype = np.uint8), (200, 200)))
    cv2.waitKey()
else:
    cv2.imshow("After PCA Image", cv2.resize(np.array(my_algo.original_data(new_coordinates[0]), dtype = np.uint8), (200, 200)))
    cv2.waitKey()


training_time = time.process_time() - training_start_time


#Reco
if reco_type == 0:
    time_start = time.process_time()

    correct = 0
    wrong = 0
    i = 0
    net_time_of_reco = 0

    for img_path in images_names_for_test:

        time_start = time.process_time()
        find_name = my_algo.recognize_face(my_algo.new_cord(img_path, img_height, img_width))
        time_elapsed = (time.process_time() - time_start)
        net_time_of_reco += time_elapsed
        rec_y = y_for_test[i]
        rec_name = target_names[rec_y]
        if find_name is rec_name:
            correct += 1
            print("Correct", " Name:", find_name)
        else:
            wrong +=1
            print("Wrong:", " Real Name:", rec_name, "Rec Y:", rec_y, "Find Name:", find_name)
        i+=1

    
    print("Total Test Images", i)
    print("Correct", correct)
    print("Wrong", wrong)
    print("Accuracy Percent =", correct/i*100,"%")
    print("Total Train Images", No_of_images_train_from_each_data * len(target_names))
    #print("Total Time Taken for reco:", time_elapsed)
    #print("Time Taken for one reco:", time_elapsed/i)
    #print("Training Time", training_time)


