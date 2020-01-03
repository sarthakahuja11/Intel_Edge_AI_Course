# Source ENV:

#pip install requests pyyaml -t /usr/local/lib/python3.5/dist-packages && clear && source /opt/intel/openvino/bin/setupvars.sh -pyver 3.5

import cv2
import numpy as np

def pose_estimation(input_image):
    '''
    Given some input image, preprocess the image so that
    it can be used with the related pose estimation model
    you downloaded previously. You can use cv2.resize()
    to resize the image.
    '''
    preprocessed_image = np.copy(input_image)

    # TODO: Preprocess the image for the pose estimation model
    
    preprocessed_image = cv2.resize(preprocessed_image,(456,256))
    preprocessed_image = preprocessed_image.transpose((2,0,1))
    preprocessed_image = preprocessed_image.reshape(1,3,256,456)

    return preprocessed_image


def text_detection(input_image):
    '''
    Given some input image, preprocess the image so that
    it can be used with the related text detection model
    you downloaded previously. You can use cv2.resize()
    to resize the image.
    '''
    preprocessed_image = np.copy(input_image)

    # TODO: Preprocess the image for the text detection 
    
    preprocessed_image = cv2.resize(preprocessed_image,(1280,768))
    preprocessed_image = preprocessed_image.transpose((2,0,1))
    preprocessed_image = preprocessed_image.reshape(1,3,768,1280)

    return preprocessed_image


def car_meta(input_image):
    '''
    Given some input image, preprocess the image so that
    it can be used with the related car metadata model
    you downloaded previously. You can use cv2.resize()
    to resize the image.
    '''
    preprocessed_image = np.copy(input_image)
    
    preprocessed_image = cv2.resize(preprocessed_image,(72,72))
    preprocessed_image = preprocessed_image.transpose((2,0,1))
    preprocessed_image = preprocessed_image.reshape(1,3,72,72)

    # TODO: Preprocess the image for the car metadata model

    return preprocessed_image

#OFFICIAL:

#python3 test.py

##ALTER - EFFICIENT 

import cv2
import numpy as np


 	'''
    Given an input image, height and width:
    - Resize to height and width
    - Transpose the final "channel" dimension to be first
    - Reshape the image to add a "batch" of 1 at the start 
    '''

def preproc(image, height,width):

	image = cv2.resize(image,(width,height))
    image = image.transpose((2,0,1))
    image = image.reshape(1,3,height,width)
	return image



def pose_estimation(input_image):
    '''
    Given some input image, preprocess the image so that
    it can be used with the related pose estimation model
    you downloaded previously. You can use cv2.resize()
    to resize the image.
    '''
    preprocessed_image = np.copy(input_image)

    # TODO: Preprocess the image for the pose estimation model
    
    preprocessed_image = preproc(preprocessed_image, 256,456)

    return preprocessed_image


def text_detection(input_image):
    '''
    Given some input image, preprocess the image so that
    it can be used with the related text detection model
    you downloaded previously. You can use cv2.resize()
    to resize the image.
    '''
    preprocessed_image = np.copy(input_image)

    # TODO: Preprocess the image for the text detection 
    

    preprocessed_image = preproc(preprocessed_image, 768,1280)

    return preprocessed_image


def car_meta(input_image):
    '''
    Given some input image, preprocess the image so that
    it can be used with the related car metadata model
    you downloaded previously. You can use cv2.resize()
    to resize the image.
    '''
    preprocessed_image = np.copy(input_image)
    
    preprocessed_image = preproc(preprocessed_image, 72,72)
    # TODO: Preprocess the image for the car metadata model

    return preprocessed_image