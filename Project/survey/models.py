from django.db import models

class SurveyResponse(models.Model):
    # Basic fields
    age = models.CharField(max_length=3)  # Age is stored as a string for simplicity
    gender = models.CharField(max_length=50)
    relationship = models.CharField(max_length=50)
    occupation = models.CharField(max_length=100)
    organization = models.TextField(max_length=100)
    social_media = models.TextField()
    platform = models.TextField()  # This will store a comma-separated list of platforms
    time_on_social_media = models.CharField(max_length=100)
    
    # Survey questions (1 to 5 scale or text answers)
    q9 = models.CharField(max_length=1)
    q10 = models.CharField(max_length=1)
    q11 = models.CharField(max_length=1)
    q12 = models.CharField(max_length=1)
    q13 = models.CharField(max_length=1)
    q14 = models.CharField(max_length=1)
    q15 = models.CharField(max_length=1)
    q16 = models.TextField()
    q17 = models.CharField(max_length=1)
    q18 = models.CharField(max_length=1)
    q19 = models.CharField(max_length=1)
    q20 = models.CharField(max_length=1)

    def __str__(self):
        return f"Survey Response {self.id} - Age: {self.age}, Gender: {self.gender}"
