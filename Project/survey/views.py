import numpy as np  # Import numpy for creating numpy array
from django.shortcuts import render, redirect
from .models import SurveyResponse, loaded_models, make_pred
# import models  # Import your external model (make sure this is accessible)

def survey_show(request):
    if request.method == 'POST':
        # Fetching form data using POST
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        relationship = request.POST.get('relationship')
        occupation = request.POST.get('occupation')
        # organization = request.POST.get('organization')
        social_media = request.POST.get('social_media')
        platform = request.POST.getlist('platform')  # For checkboxes, use getlist
        time_on_social_media = request.POST.get('time')
        
        # Other form responses (questions 8-18)
        q8 = request.POST.get('q8')
        q9 = request.POST.get('q9')
        q10 = request.POST.get('q10')
        q11 = request.POST.get('q11')
        q12 = request.POST.get('q12')
        q13 = request.POST.get('q13')
        # q15 = request.POST.get('q15')
        q14 = request.POST.get('q14')
        q15= request.POST.get('q15')
        q16 = request.POST.get('q16')
        q17 = request.POST.get('q17')
        q18 = request.POST.get('q18')


        # Example encoding for platforms
        platforms = ['Facebook', 'Twitter', 'Instagram', 'YouTube', 'Discord', 'Reddit', 'Pinterest', 'SnapChat', 'TikTok']
        platform_data = [1 if plat in platform else 0 for plat in platforms]

        # Example of saving data to the SurveyResponse model
        response = SurveyResponse(
            age=age,
            gender=gender,
            relationship=relationship,
            occupation=occupation,
            # organization=organization,
            social_media=social_media,
            #platform=', '.join(platform),  # Save platforms as a comma-separated string
            platform = platform_data,
            time_on_social_media=time_on_social_media,
            q8=q8, q9=q9, q10=q10, q11=q11, q12=q12, q13=q13,
            q14=q14, q15=q15, q16=q16, q17=q17, q18=q18
        )
        response.save()

        # After saving the form data, fetch the response data from the form
        response_data = [
            age, gender, relationship, occupation, social_media,
            *platform_data, time_on_social_media,
            q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18
        ]

        # Convert response data to a numpy.array
        response_array = np.array(response_data)

        # Pass the numpy array to your external model
        result = make_pred(response_array)  # Assuming your_model has a `predict` function

        # Optionally, you can store the result in the response object or process it further
        # Example: Store the result of the prediction (optional)
        response.prediction = result
        response.save()

        # Redirect to the output page after submission
        return redirect('survey_output')

    else:
        # Display the survey form when the page is first accessed (GET request)
        return render(request, 'survey/surveyform.html')

def survey_output(request):
    # Optionally, you can pass the prediction result or any other context to output.html
    return render(request, 'survey/output.html')  # Render the output page after form submission
