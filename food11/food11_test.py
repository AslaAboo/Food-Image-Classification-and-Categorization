# -*- coding: utf-8 -*-
"""Food11-test.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1L1gpQJJWPoZ4l6fqmkkXMKMCMewZW1uy
"""

from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import os
from keras.applications.inception_v3 import InceptionV3, preprocess_input

from google.colab import drive
drive.mount('/content/drive')

model = load_model('/content/drive/My Drive/colab/Food-11/food11_model.h5')

model.summary()

train_data_dir = '/content/drive/My Drive/colab/Food-11/dataset/train'
test_data_dir = '/content/drive/My Drive/colab/Food-11/dataset/test'

# dimensions of our images.
#Inception input size
img_width, img_height = 299, 299
batch_size = 24
image_size = (299, 299)

# we need to recompile the model for these modifications to take effect
# we use SGD with a low learning rate
from keras.optimizers import SGD
model.compile(optimizer=SGD(lr=0.0001, momentum=0.9), loss='categorical_crossentropy')

# get all the train labels
#train_labels = os.listdir(train_data_dir)

train_labels = ['bread', 'dairy', 'dessert', 'egg', 'fried_food', 'meat', 'noodles_pasta', 'rice', 'seafood', 'soup', 'vegetable_fruit']

# get all the test images paths
test_images = os.listdir(test_data_dir)
corr = 0
i = 0

len(test_images)

test_data = []
test_labels = []
y_pred_nm = []
# loop through each image in the test data
for image_path in test_images:
    path 		= test_data_dir + "/" + image_path
    img 		= image.load_img(path, target_size=image_size)
    x 			= image.img_to_array(img)
    x 			= np.expand_dims(x, axis=0)
    x /= 255. 
    test_data.append(x)
    Y_pred = model.predict(x, verbose=1)
    y_pred = np.argmax(Y_pred, axis=1)
    y_pred_nm.append(y_pred[0])
    print(y_pred[0])
    y = int(image_path.split("_")[0])
    if(y == y_pred[0]):
        corr = corr + 1
    test_labels.append(y)
    print ("Actual image:   " + train_labels[y])
    print (image_path)
    print ("I think it is a " + train_labels[y_pred[0]])
  
print ("End of testing...")
len(test_data)

acc = (corr / float(len(test_images))) * 100
print("Accuracy: " + str(acc))
#Accuracy: 72.1541679115626 (299, 299)
#Accuracy: 67.31285416045333 (224, 224)

from sklearn.metrics import precision_score, recall_score, confusion_matrix, classification_report, accuracy_score, f1_score
print(' Report: ')
print('\n Accuracy:', accuracy_score(test_labels, y_pred_nm))
print('\n F1 score:', f1_score(test_labels, y_pred_nm, average=None))
print('\n Recall:', recall_score(test_labels, y_pred_nm, average=None))
print('\n Precision:', precision_score(test_labels, y_pred_nm, average=None))
print('\n classification report:\n', classification_report(test_labels,y_pred_nm))
print('\n confusion matrix:\n',confusion_matrix(test_labels, y_pred_nm))