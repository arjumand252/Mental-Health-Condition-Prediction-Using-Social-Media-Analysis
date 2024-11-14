import numpy as np  # Import numpy for creating numpy array
from django.shortcuts import render, redirect
from .models import SurveyResponse, loaded_models, make_pred
# import models  # Import your external model (make sure this is accessible)

#mappings for all the fields
gender_map = {'Male': 0, 'Female': 1, 'Other': 2}
relationship_map = {'Single': 0, 'Married': 1, 'In a relationship': 2, 'Divorced': 3}
social_media_map = {'Yes':0, 'No':1}
time_on_sm_map = {'Less than an Hour':0, 'Between 1 and 2 hours':1, 'Between 2 and 3 hours':2, 'Between 3 and 4 hours':3, 'Between 4 and 5 hours':4, 'More than 5 hour':5}
# q6_map = {1:0, 2:1, 3:2, 4:3, 5:4}
# q7_map = {1:0, 2:1, 3:2, 4:3, 5:4}
# q8_map = {1:0, 2:1, 3:2, 4:3, 5:4}        
# q9_map = {1:0, 2:1, 3:2, 4:3, 5:4}
# q10_map = {1:0, 2:1, 3:2, 4:3, 5:4}
# q11_map = {1:0, 2:1, 3:2, 4:3, 5:4}
# q12_map = {1:0, 2:1, 3:2, 4:3, 5:4}
# q13_map = {1:0, 2:1, 3:2, 4:3, 5:4}
# q14_map = {1:0, 2:1, 3:2, 4:3, 5:4}
# q15_map = {1:0, 2:1, 3:2, 4:3, 5:4}
platform_map = {'Discord':0, 'Facebook':1, 'Instagram':2, 'Pinterest':3, 'Reddit':4, 'SnapChat':5, 'TikTok':6, 'Twitter':7, 'YouTube':8}


def survey_show(request):
    if request.method == 'POST':
        # Fetching form data using POST
        age = float(request.POST.get('age'))  #age
        gender = int(gender_map.get(request.POST.get('gender')))   #gender
        relationship = int(relationship_map.get(request.POST.get('relationship')))  #relationshipStatus
        # occupation = request.POST.get('occupation')
        # organization = request.POST.get('organization')
        social_media = int(social_media_map.get(request.POST.get('social_media')))  #use_sm
        time_on_social_media = float(time_on_sm_map.get(request.POST.get('time')))   #avg time
        
        # Other form responses (questions 7-17)
        q6 = int(request.POST.get('q6')) #sm_without_purpose
        q7 = int(request.POST.get('q7'))  #sm_distraction
        q8 = int(request.POST.get('q8'))  #sm_restless
        q9 = int(request.POST.get('q9'))  #worried
        q10 = int(request.POST.get('q10'))  #concentration
        q11 = int(request.POST.get('q11'))  #comparison
        q12 = int(request.POST.get('q12'))  #seek_validation
        # q15 = request.POST.get('q15')
        q13 = int(request.POST.get('q13'))   #depressed
        q14 = int(request.POST.get('q14'))   #interest_fluctuation
        q15 = int(request.POST.get('q15'))  #sleep_issues
        platform_list = request.POST.getlist('platform')  # For checkboxes, use getlist


        # Example encoding for platforms
        platforms = ['Discord', 'Facebook', 'Instagram', 'Pinterest', 'Reddit', 'SnapChat', 'TikTok', 'Twitter', 'YouTube']
        platform_data = [1 if int(plat in platform_list) else 0 for plat in platforms]

        # Example of saving data to the SurveyResponse model
        response = SurveyResponse(
            age=age,
            gender=gender,
            relationship=relationship,
            # occupation=occupation,
            # organization=organization,
            social_media=social_media,
            #platform=', '.join(platform),  # Save platforms as a comma-separated string
            time_on_social_media=time_on_social_media,
            q6=q6, q7=q7, q8=q8, q9=q9, q10=q10, q11=q11, q12=q12, q13=q13,
            q14=q14, q15=q15, platform = platform_data
        )
        response.save()

        # After saving the form data, fetch the response data from the form
        response_data = [
            age, gender, relationship, social_media,
            time_on_social_media,
            q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, *platform_data
        ]

        print(response_data)
        # Convert response data to a numpy.array
        response_data_1 = response_data[1:]
        response_array = np.array(response_data_1)
        # Reshape the array to have shape (1, 23) where 1 is the batch size (one sample)
        response_array = response_array.reshape(1, -1)

        # Pass the numpy array to your external model
        result = make_pred(response_array)  # Assuming your_model has a `predict` function

        # Store prediction in session
        request.session['prediction'] = str(result)

        # Optionally, you can store the result in the response object or process it further
        # Example: Store the result of the prediction (optional)
        # response.prediction = result
        response.save()

        # Redirect to the output page after submission
        return redirect('survey_output')

    else:
        # Display the survey form when the page is first accessed (GET request)
        return render(request, 'survey/surveyform.html')

def survey_output(request):
    # Optionally, you can pass the prediction result or any other context to output.html

     # Get the prediction from the session if it exists
    prediction = request.session.get('prediction', "No prediction available")
    
    # Render the output page with the prediction
    return render(request, 'survey/output.html', {'prediction': prediction})
    # return render(request, 'survey/output.html')  # Render the output page after form submission