import requests
import matplotlib.pyplot as plt
import pandas as pd

# ==============================
# OpenWeatherMap API Integration
# ==============================

API_KEY = "1a36cfc634fcb0c18bc19d85ae22b50d"   # Keep your key private in GitHub
CITY = "Bhubaneswar"

# Forecast API Endpoint
url = f"https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

# Check for API errors
if data.get("cod") != "200":
    print("Error from API:")
    print(data)
else:
    dates = []
    temperatures = []

    # Extract first 10 forecast records
    for item in data["list"][:10]:
        dates.append(item["dt_txt"])
        temperatures.append(item["main"]["temp"])

    # Create DataFrame
    df = pd.DataFrame({
        "Date & Time": dates,
        "Temperature (°C)": temperatures
    })

    print("\nWeather Forecast Data:\n")
    print(df)

    # Plot temperature trend
    plt.figure(figsize=(10,5))
    plt.plot(df["Date & Time"], df["Temperature (°C)"], marker="o")
    plt.xticks(rotation=45)
    plt.title(f"5-Day Temperature Forecast for {CITY}")
    plt.xlabel("Date & Time")
    plt.ylabel("Temperature (°C)")
    plt.grid(True)
    plt.tight_layout()

    import os
    print("Saved in folder:", os.getcwd())

    # Save graph as image (Important for submission)
    plt.savefig("weather_forecast.png")

    plt.show()

    print("\nGraph saved as 'weather_forecast.png'")