from django.db import models
import os
# your_app/utils/ml_model.py
# Load the .h5 model once to use in predictions
import tensorflow as tf
import numpy as np
from scipy.stats import mode


# Set the base directory dynamically
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Now set the relative path to your model directory
MODEL_DIR = os.path.join(BASE_DIR, 'models')

# Dictionary to hold models by type and condition
loaded_models = {
    "autoencoder": {
        "adhd": tf.keras.models.load_model(os.path.join(MODEL_DIR, 'auto_enc_adhd.h5')),
        "anxiety": tf.keras.models.load_model(os.path.join(MODEL_DIR, 'auto_enc_anxiety.h5')),
        "ptsd": tf.keras.models.load_model(os.path.join(MODEL_DIR, 'auto_enc_ptsd.h5')),
        "bipolar": tf.keras.models.load_model(os.path.join(MODEL_DIR, 'auto_enc_bipolar.h5')),
        "depression": tf.keras.models.load_model(os.path.join(MODEL_DIR, 'auto_enc_depression.h5'))
    },
    "fcnn": {
        "adhd": tf.keras.models.load_model(os.path.join(MODEL_DIR, 'fcnn_adhd.h5')),
        "anxiety": tf.keras.models.load_model(os.path.join(MODEL_DIR, 'fcnn_anxiety.h5')),
        "ptsd": tf.keras.models.load_model(os.path.join(MODEL_DIR, 'fcnn_ptsd.h5')),
        "bipolar": tf.keras.models.load_model(os.path.join(MODEL_DIR, 'fcnn_bipolar.h5')),
        "depression": tf.keras.models.load_model(os.path.join(MODEL_DIR, 'fcnn_depression.h5'))
    },
    "resnet": {
        "adhd": tf.keras.models.load_model(os.path.join(MODEL_DIR, 'resnet_adhd.h5')),
        "anxiety": tf.keras.models.load_model(os.path.join(MODEL_DIR, 'resnet_anxiety.h5')),
        "ptsd": tf.keras.models.load_model(os.path.join(MODEL_DIR, 'resnet_ptsd.h5')),
        "bipolar": tf.keras.models.load_model(os.path.join(MODEL_DIR, 'resnet_bipolar.h5')),
        "depression": tf.keras.models.load_model(os.path.join(MODEL_DIR, 'resnet_depression.h5'))
    }
}


def adhd_pred(input_data):
    ae = loaded_models["autoencoder"]["adhd"].predict(input_data)
    ae = (ae>0.25).astype(int)
    fc = loaded_models["fcnn"]["adhd"].predict(input_data)
    fc = (fc>0.25).astype(int)
    rn = loaded_models["resnet"]["adhd"].predict(input_data)
    rn = (rn>0.25).astype(int)
    predictions_adhd = np.vstack([ae, fc, rn])
    final_predictions_adhd = mode(predictions_adhd, axis=1).mode.flatten()
    return final_predictions_adhd

def anxiety_pred(input_data):
    ae = loaded_models["autoencoder"]["anxiety"].predict(input_data)
    ae = (ae>0.25).astype(int)
    fc = loaded_models["fcnn"]["anxiety"].predict(input_data)
    fc = (fc>0.25).astype(int)
    rn = loaded_models["resnet"]["anxiety"].predict(input_data)
    rn = (rn>0.25).astype(int)
    predictions_anxiety = np.vstack([ae, fc, rn])
    final_predictions_anxiety = mode(predictions_anxiety, axis=1).mode.flatten()
    return final_predictions_anxiety

def ptsd_pred(input_data):
    ae = loaded_models["autoencoder"]["ptsd"].predict(input_data)
    ae = (ae>0.25).astype(int)
    fc = loaded_models["fcnn"]["ptsd"].predict(input_data)
    fc = (fc>0.25).astype(int)
    rn = loaded_models["resnet"]["ptsd"].predict(input_data)
    rn = (rn>0.25).astype(int)
    predictions_ptsd = np.vstack([ae, fc, rn])
    final_predictions_ptsd = mode(predictions_ptsd, axis=1).mode.flatten()
    return final_predictions_ptsd

def bipolar_pred(input_data):
    ae = loaded_models["autoencoder"]["bipolar"].predict(input_data)
    ae = (ae>0.25).astype(int)
    fc = loaded_models["fcnn"]["bipolar"].predict(input_data)
    fc = (fc>0.25).astype(int)
    rn = loaded_models["resnet"]["bipolar"].predict(input_data)
    rn = (rn>0.25).astype(int)
    predictions_bipolar = np.vstack([ae, fc, rn])
    final_predictions_bipolar = mode(predictions_bipolar, axis=1).mode.flatten()
    return final_predictions_bipolar

def depression_pred(input_data):
    ae = loaded_models["autoencoder"]["depression"].predict(input_data)
    ae = (ae>0.25).astype(int)
    fc = loaded_models["fcnn"]["depression"].predict(input_data)
    fc = (fc>0.25).astype(int)
    rn = loaded_models["resnet"]["depression"].predict(input_data)
    rn = (rn>0.25).astype(int)
    predictions_depression = np.vstack([ae, fc, rn])
    final_predictions_depression = mode(predictions_depression, axis=1).mode.flatten()
    return final_predictions_depression


def make_pred(input_data):
    # Run each diagnostic prediction function
    adhd = adhd_pred(input_data)
    anxiety = anxiety_pred(input_data)
    ptsd = ptsd_pred(input_data)
    bipolar = bipolar_pred(input_data)
    depression = depression_pred(input_data)
    
    # Initialize a list to store diagnoses for each input
    diagnoses = []

    # For each data point in the input, generate diagnoses
    for i in range(len(input_data)):
        diagnosis_labels = []
        
        # Map predictions to labels
        if adhd[i] == 1:
            diagnosis_labels.append("ADHD")
        if anxiety[i] == 1:
            diagnosis_labels.append("Anxiety")
        if ptsd[i] == 1:
            diagnosis_labels.append("PTSD")
        if bipolar[i] == 1:
            diagnosis_labels.append("Bipolar")
        if depression[i] == 1:
            diagnosis_labels.append("Depression")
        
        # Join diagnoses into a single string or mark as "No Diagnosis" if empty
        if diagnosis_labels:
            diagnoses.append(" and ".join(diagnosis_labels))
        else:
            diagnoses.append("No Diagnosis")
    
    return diagnoses



class SurveyResponse(models.Model):
    # Basic fields
    age = models.CharField(max_length=50)  # Age is stored as a string for simplicity
    gender = models.CharField(max_length=50)
    relationship = models.CharField(max_length=50)
    # occupation = models.CharField(max_length=100, default='0')
    social_media = models.TextField()
    time_on_social_media = models.CharField(max_length=100)
    
    # Survey questions (1 to 5 scale or text answers)
    q6 = models.CharField(max_length=1, default='0')
    q7 = models.CharField(max_length=1, default='0')
    q8 = models.CharField(max_length=1, default='0')
    q9 = models.CharField(max_length=1, default='0')
    q10 = models.CharField(max_length=1, default='0')
    q11 = models.CharField(max_length=1, default='0')
    q12 = models.CharField(max_length=1, default='0')
    q13 = models.CharField(max_length=1, default='0')
    q14 = models.CharField(max_length=1, default='0')
    q15 = models.CharField(max_length=1, default='0')
    platform = models.TextField()  # This will store a comma-separated list of platforms


    def __str__(self):
        return f"Survey Response {self.id} - Age: {self.age}, Gender: {self.gender}"
