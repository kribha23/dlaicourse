# Classifying Cats and Dogs in Raspberry Pi

This is the code repository of performing Transfer Learning on a pretrained model for Cats vs Dogs Image Classification task to be run on Edge device of Raspberry Pi. To get started, go through [this](https://colab.research.google.com/drive/1Fl7Fk20-G6KVg400bhCZOWlJHNNQiDiv) Python notebook. Generate the required TFLite assets from it. 

Next, to run the code on Raspberry Pi, paste the following command

```
python3 classify.py --filename input.jpg --model_path converted_model.tflite
```
