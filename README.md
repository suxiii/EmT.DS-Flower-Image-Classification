
# Image Classification Model for Flower Recognition

This repository contains a TensorFlow-based image classification model designed to recognize different species of flowers. The model is trained on a custom dataset and includes data augmentation, a convolutional neural network (CNN) architecture, and the ability to predict the class of new flower images.

---
## Installation

To get started, you'll need to install TensorFlow:

```bash
!pip install tensorflow
```

---
## Dataset

The `Set_Y.zip` file, containing the flower images, is automatically downloaded and extracted. The dataset is split into training and validation sets for model development.

---
## Model Architecture

The model is a Sequential Keras model with the following key components:

* **Data Augmentation:** Includes `RandomFlip`, `RandomRotation`, and `RandomZoom` layers to enhance the training data.
* **Rescaling:** Normalizes pixel values to be between 0 and 1.
* **Convolutional Layers:** Three `Conv2D` layers with `relu` activation and `MaxPooling2D` for feature extraction.
* **Flatten Layer:** Converts the 2D feature maps into a 1D vector.
* **Dense Layers:** Two fully connected layers, with a `Dropout` layer for regularization.
* **Output Layer:** A `Dense` layer with `num_classes` outputs for classification.

---
## Training

The model is compiled with the Adam optimizer (learning rate 0.0001), `SparseCategoricalCrossentropy` loss, and `accuracy` as a metric. It is trained for 50 epochs with early stopping and model checkpointing configured to save the best performing model.

---
## Prediction

After training, the model can predict the class of new flower images. The prediction script processes images from a `Test` directory, displays the image, and outputs the predicted flower class along with a confidence score. If the confidence is below 70%, it suggests the flower might not be in the training dataset.

---
## Saved Model

The trained model is saved as `flowers_model.keras` for future use.

---
