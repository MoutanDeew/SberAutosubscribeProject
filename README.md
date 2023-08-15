<h1 align="center">Here you can see the developed model for predicting the target action, the model is built on the data of the site https://podpiska.sberauto.com/</h1>
<h3 align="center">Project goals:
1) Learn to predict the user's target action (approximate ROC-AUC value ~ 0.65).
2) Pack the resulting model into a service that will take all attributes like utm_*, device_*, geo_* as input, and give the output 0/1 (1 - if the user performs any target action).

What is to be done?
Solve the classification problem.

What were the difficulties in the process?
Due to the low power of the computer. Calculations were not performed or were performed for a very long time.

How could it be decided?
1). Reduce the dataset on which the manipulations were performed. For example, instead of 15,000,000 lines, take only 400,000.
2). Split values ​​in all columns except geo_city, utm_medium, device_category, device_os, device_browser into classes. I chose how to break the values ​​into classes based on the target user action. For 1, I took the most frequent value of the column for the user who performed the target action, and the remaining values ​​of the column as 0.

I chose the second solution because I wanted to train the model on a larger sample. The sample was 3369072 lines.
As a result, the best Ml-model for finding the optimal function is Random Forest. With ROC-AUC = 0.65.
<img src="https://github.com/MoutanDeew/SberAutosubscribeProject/raw/main/charts/ROC-AUC_0.65.png" height="32"/>

To better understand which features are more influential in determining the target user action, I used SHAP.

SHAP (SHapley Additive exPlanations) is a game theoretic approach to explain the output of any machine learning model. It connects optimal credit allocation with local explanations using the classic Shapley values from game theory and their related extensions (see papers for details and citations).

To get an overview of which features are most important for a model we can plot the SHAP values of every feature for every sample. The plot below sorts features by the sum of SHAP value magnitudes over all samples, and uses SHAP values to show the distribution of the impacts each feature has on the model output. The color represents the feature value (red high, blue low). This shows, for example, that a value of 1 in the utm_adcontent_0_1 field means that the user is highly likely to take the targeted action. 
<img src="https://github.com/MoutanDeew/SberAutosubscribeProject/raw/main/charts/beswar_plot.png" height="32"/>

We can also just take the mean absolute value of the SHAP values for each feature to get a standard bar plot (produces stacked bars for multi-class outputs):
<img src="https://github.com/MoutanDeew/SberAutosubscribeProject/raw/main/charts/shap_plots_bar.png" height="32"/>
</h3>
<h2 align="center">How to run the model?</h2>
<h3 align="center">Step 1. Download the "model" folder and the "main.py" file.</h3>
<h3 align="center">Step 2. Because this is localhost web app. Download and install Postman.</h3>
<h3 align="center">Step 3. Run linux or gitbash command prompt. Go to the folder with the project files and run the application with the command "uvicorn main:app --reload".</h3>
<h3 align="center">Step 4. Run Postman. Insert a JSON data file like this in the request body. Data can be taken from the database file, which is in the releases for the project.</h3>
<h3 align="left">{</h3>
<h3 align="left">    "utm_source": "fDLlAcSmythWSCVMvqvL",</h3>
<h3 align="left">    "utm_medium": "cpa",</h3>
    <h3 align="left">    "utm_campaign": "LTuZkdKfxRGVceoWkVyg",</h3>
    <h3 align="left">    "utm_adcontent": "JNHcPlZPxEMWDnRiyoBf",</h3>
    <h3 align="left">    "utm_keyword": "puhZPIYqKXeFPaUviSjo",</h3>
    <h3 align="left">    "device_category": "mobile",</h3>
    <h3 align="left">    "device_os": "iOS",</h3>
    <h3 align="left">    "device_brand": "Apple",</h3>
    <h3 align="left">    "device_screen_resolution": "428x926",</h3>
    <h3 align="left">    "device_browser": "Safari",</h3>
    <h3 align="left">    "geo_country": "Russia",</h3>
    <h3 align="left">    "geo_city": "Moscow"</h3>
<h3 align="left">}</h3>
<h3 align="center">Step 5. For prediction, select the post request type and enter the command 127.0.0.1:8000/predict.</h3>
<h3 align="center">Step 6. Get the prediction result. Conclusion 0 or 1. Where 1 is the completion of the target action. (a person has purchased a subscription, etc.).</h3>
<h3 align="center">Step 7. Invite me for an interview to make useful and effective ML models together. =) </h3>

