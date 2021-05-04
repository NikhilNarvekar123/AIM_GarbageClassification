import streamlit as lit
import tensorflow as tf
from tensorflow import keras
import h5py

def loadModel():
    mainModel = tf.keras.models.load_model('model.h5')
    mainModel.summary()

lit.title("Garbage Classification")
lit.text("Input an image below, and our program will identify which type of garbage it is: ")
lit.text("cardboard, glass, metal, paper, plastic, or trash")
img_file_buffer = lit.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])



loadModel()
