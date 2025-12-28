from flask import Flask, render_template, request
import requests
from datetime import datetime

app = Flask(__name__, template_folder="../templates")
@app.route("/", methods=["GET", "POST"])

def home():
    weather_data = None
    not_found = None
    timestamp = ""
    period = ""
    
    url = "https://api-open.data.gov.sg/v2/real-time/api/two-hr-forecast"
    response = requests.get(url).json()
    forecasts = response["data"]["items"][0]["forecasts"]
    timestamp = datetime.fromisoformat(response["data"]["items"][0]["timestamp"]).date()
    period = response["data"]["items"][0]["valid_period"]["text"]
    
    if request.method == "POST":
        location = request.form.get("location")

        for area in forecasts:
            if area["area"].lower() == location.lower():
                weather_data=area
                break

        if not weather_data:
            not_found=f"{location} Not Found"

    return render_template("index.html", weather_data=weather_data, not_found=not_found, timestamp=timestamp, period=period)

if __name__ == "__main__":
    app.run(debug=True)