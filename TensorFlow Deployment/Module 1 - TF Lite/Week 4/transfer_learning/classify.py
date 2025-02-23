# Copyright 2019 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import tensorflow as tf
# Enable eager execution for TF < 2.0
import numpy as np
import argparse


parser = argparse.ArgumentParser(description='Cat vs Dog')
parser.add_argument('--filename', type=str, help='Specify the filename', required=True)
parser.add_argument('--model_path', type=str, help='Specify the model path', required=True)

args = parser.parse_args()

filename = args.filename
model_path = args.model_path 
size = [int(item) for item in args.size.split(',')]

with open(model_path, 'rb') as f:
    tflite_model = f.read()

# Load TFLite model and allocate tensors
interpreter = tf.lite.Interpreter(model_content=tflite_model)
interpreter.allocate_tensors()

# Get input and output tensors.
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Read image
img = tf.io.read_file(filename)
img_tensor = tf.image.decode_image(img)

# Get input size
input_shape = input_details[0]['shape']
size = input_shape[:2] if len(input_shape) == 3 else input_shape[1:3]

# Preprocess image
img_tensor = tf.image.resize(img_tensor, size)
img_tensor = img_tensor / 255.0

# Add a batch dimension
input_data = tf.expand_dims(img_tensor, axis=0)

# Point the data to be used for testing and run the interpreter
interpreter.set_tensor(input_details[0]['index'], input_data)
interpreter.invoke()

# Obtain results and print the predicted category
predictions = interpreter.get_tensor(output_details[0]['index'])
predicted_label = np.argmax(predictions)
print('Cat' if predicted_label == 0 else 'Dog')
