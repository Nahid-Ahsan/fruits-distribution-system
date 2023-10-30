from django.shortcuts import render
import numpy as np
from tensorflow.keras.utils import load_img, img_to_array
import tensorflow as tf
from tensorflow.keras.preprocessing import image

from rest_framework import viewsets
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes


model = tf.keras.models.Sequential([
    # This is the first convolution
    tf.keras.layers.Conv2D(128, (3,3), activation='relu', input_shape=(224, 224, 3)),
    tf.keras.layers.MaxPooling2D(2, 2),
    # The second convolution
    tf.keras.layers.Conv2D(128, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    # The third convolution
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    # The fourth convolution
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    # Flatten the results to feed into a DNN
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dropout(0.5),
    # 512 neuron hidden layer
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(4, activation='softmax')
])

# load weights
model.load_weights("./fruitDisease/weights.best.hdf5")
model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])



def pred(image):

    image = Image.open(image)
    img = image.resize((224, 224))
    img = img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = np.vstack([img])
    classes = model.predict(img, batch_size=10)
    return classes


@api_view(['GET','POST'])
@csrf_exempt
def result(request):
        image = request.FILES['image']

        prediction = pred(image)
        print(prediction[0])

        if prediction[0][0] == 1:
            res = "Blotch Apple"
        elif prediction[0][1] == 1:
            res = "Normal Apple"
        elif prediction[0][2] == 1:
            res = "Rot Apple"
        if prediction[0][3] == 1:
            res = "Scab Apple"

        return Response(res)