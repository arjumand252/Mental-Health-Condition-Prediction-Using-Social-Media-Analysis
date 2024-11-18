The primary objective of this project is to develop a deep learning-based system capable of predicting potential mental health conditions, such as depression, ADHD, and anxiety, by analyzing user responses to a detailed questionnaire. This system aims to identify patterns in the data that are indicative of specific mental health concerns, providing an accurate and data-driven assessment of the user's mental well-being.  

A critical aspect of this project is understanding how social media usage patterns contribute to or exacerbate mental health issues. By incorporating insights into social media habits, the system will explore correlations between online behaviors, such as screen time, interaction patterns, and exposure to certain types of content, with mental health outcomes. This dual focus on questionnaire responses and social media analysis ensures a holistic approach to mental health prediction.  

To make this system accessible and user-friendly, a secure web application will be developed. This platform will allow individuals to complete the questionnaire with ease and receive personalized predictions about their mental health. The application will present the results in an intuitive and actionable format, offering users a clear understanding of their mental health status and potential areas of concern.  

**Literature Review**

Open Access Deep learning in mental health outcome research: a scoping review. (2020) 									       [Review Article]	
Chang Su, Zhenxing Xu, Jyotishman Pathak and Fei Wang.
The paper focuses on reviewing deep learning algorithms for mental health outcomes. Key findings are:
DL studies mainly focused on stress detection, depression identification and estimation of suicide risk.
Text mining has been the main source of data collection for the predictive task, along with image properties (e.g., color theme, saturation and brightness) to provide cues on the users’ mental health status.
Some studies also focus on the users’ network graphs and content to discover underlying cues.
Adapting Deep Learning Methods for Mental Health Prediction on Social Media. (2020) 									   [Predictive Model]
The research focuses on the binary classification task of predicting if a user suffers from one of nine mental health disorders using a Hierarchical Attention Network (HAN). The SMHD (Self-diagnosed Mental Health Disorder) dataset is used, which contains the textual reddit data of users who mention their diagnosis in their posts. 

This project proposes a multi-label classification model created using the ensemble method to improve predictive accuracy. The classification will be multi-label due to the fact that a person suffering from one mental health condition is likely to suffer from others as well. Our models will be trained on a survey dataset, where users diagnosed with a variety of mental health conditions answer questions regarding their social media usage and its impact on their mental well-being.

**Features**
* Ensemble Method
* Fully Connected Neural Network
* Autoencoder Model
* ResNet Implementation
* Multi-label classification using Majority Voting Technique

**Requirements**
* Numpy
* Pandas
* Matplotlib
* Seaborn
* Tensorflow
* Django
  
