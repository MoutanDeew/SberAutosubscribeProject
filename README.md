<h1 align="center">Hi there, I'm German Kataev 
<img src="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" height="32"/></h1>
<h3 align="center">I am a junior Data Scientist from Russia</h3>
<h3 align="center">Here you can see the developed model for predicting the target action, the model is built on the data of the site https://podpiska.sberauto.com/</h3>
<h3 align="center">Database file are in releases</h3>
<h2 align="center">How to run the model?</h2>
<h3 align="center">Step 1. Download the "model" folder and the "main.py" file.</h3>
<h3 align="center">Step 2. Because this is localhost web app. Download and install Postman.</h3>
<h3 align="center">Step 3. Insert a JSON data file like this in the request body. Data can be taken from the database file, which is in the releases for the project.</h3>
<h3 align="center">{
    "utm_source": "fDLlAcSmythWSCVMvqvL",
    "utm_medium": "cpa",
    "utm_campaign": "LTuZkdKfxRGVceoWkVyg",
    "utm_adcontent": "JNHcPlZPxEMWDnRiyoBf",
    "utm_keyword": "puhZPIYqKXeFPaUviSjo",
    "device_category": "mobile",
    "device_os": "iOS",
    "device_brand": "Apple",
    "device_screen_resolution": "428x926",
    "device_browser": "Safari",
    "geo_country": "Russia",
    "geo_city": "Moscow"
}</h3>
<h3 align="center">Step 4. For prediction, select the post request type and enter the command 127.0.0.1:8000/predict.</h3>
<h3 align="center">Step 5. Get the prediction result. Conclusion 0 or 1. Where 1 is the completion of the target action. (a person has purchased a subscription, etc.).</h3>
<h3 align="center">Step 6. Invite me for an interview to make useful and effective ML models together. =) </h3>

