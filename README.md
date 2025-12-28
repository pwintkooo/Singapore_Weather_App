# 🌤 Singapore Weather App

A modern, responsive web application that provides real-time 2-hour weather forecasts for Singapore locations using data from Singapore's Open Data API.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.1.2-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

- **Real-Time Weather Data**: Fetches live 2-hour weather forecasts from Singapore's official Open Data API
- **Location Search**: Search weather forecasts by Singapore location/area name
- **Modern UI/UX**: Clean, gradient-based design with smooth animations
- **Weather Icons**: Dynamic weather emojis based on forecast conditions (☀️ 🌧️ ⛈️ ☁️)
- **Responsive Design**: Mobile-friendly interface that adapts to all screen sizes
- **Timestamp Display**: Shows when the forecast was last updated and valid period
- **Error Handling**: User-friendly messages when locations are not found

## 🚀 Demo

The app is deployed on Vercel and can be accessed at: [Your Vercel URL]

## 📋 Prerequisites

Before running this application, make sure you have:

- Python 3.8 or higher
- pip (Python package manager)
- Internet connection (for API calls)

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/weather-app.git
   cd weather-app
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🎮 Usage

### Running Locally

1. **Start the Flask application**
   ```bash
   python api/app.py
   ```

2. **Open your browser** and navigate to:
   ```
   http://localhost:5000
   ```

3. **Search for weather**
   - Enter a Singapore location name (e.g., "Jurong East", "Tampines", "Woodlands")
   - Click "🔍 Search Weather" button
   - View the weather forecast, timestamp, and valid period

### Available Singapore Locations

The app supports all official Singapore weather forecast areas including:
- Ang Mo Kio
- Bedok
- Bishan
- Boon Lay
- Bukit Batok
- Bukit Merah
- Bukit Panjang
- Bukit Timah
- Central Water Catchment
- Changi
- Choa Chu Kang
- Clementi
- City
- Geylang
- Hougang
- Jurong East
- Jurong West
- Kallang
- Marine Parade
- Novena
- Pasir Ris
- Paya Lebar
- Punggol
- Queenstown
- Sembawang
- Sengkang
- Serangoon
- Tampines
- Toa Payoh
- Woodlands
- Yishun

## 📁 Project Structure

```
Weather_App/
├── api/
│   └── app.py              # Flask application and API routes
├── templates/
│   └── index.html          # HTML template with embedded CSS
├── requirements.txt        # Python dependencies
├── vercel.json            # Vercel deployment configuration
└── README.md              # Project documentation
```

## 🔌 API Reference

This app uses the **Singapore Government Open Data API**:

- **Endpoint**: `https://api-open.data.gov.sg/v2/real-time/api/two-hr-forecast`
- **Method**: GET
- **Response**: JSON containing 2-hour weather forecasts for all Singapore areas
- **Update Frequency**: Updated every few minutes
- **Documentation**: [data.gov.sg](https://data.gov.sg)

## 🌐 Deployment

### Deploy to Vercel

1. **Install Vercel CLI**
   ```bash
   npm install -g vercel
   ```

2. **Deploy**
   ```bash
   vercel
   ```

3. **Follow the prompts** to complete deployment

The `vercel.json` file is already configured for deployment.

### Deploy to Other Platforms

This Flask app can also be deployed to:
- **Heroku**: Add a `Procfile` with `web: gunicorn api.app:app`
- **Railway**: Connect your GitHub repository
- **PythonAnywhere**: Upload files and configure WSGI
- **AWS/GCP/Azure**: Use their respective Python hosting services

## 🛡️ Technologies Used

- **Backend**: Flask 3.1.2 (Python web framework)
- **Frontend**: HTML5, CSS3 (with embedded styles)
- **Templating**: Jinja2
- **API**: Singapore Open Data API
- **HTTP Client**: Requests library
- **Deployment**: Vercel

## 🎨 UI/UX Features

- Gradient purple background (667eea to 764ba2)
- Google Fonts (Poppins) for modern typography
- Card-based layout with soft shadows
- Smooth hover animations and transitions
- Dynamic weather emoji icons
- Mobile-responsive grid system
- Empty state for first-time users

## 📝 Code Highlights

### Weather Icon Logic
The app intelligently displays weather emojis based on forecast keywords:
- ⛈️ Thundery weather
- 🌧️ Showers/Rain
- ☁️ Cloudy
- ☀️ Fair/Sunny
- ⛅ Partly Cloudy
- 🌫️ Hazy
- 💨 Windy

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🙏 Acknowledgments

- Weather data provided by [data.gov.sg](https://data.gov.sg)
- Singapore Government Open Data API
- Flask framework and community
- Google Fonts (Poppins)

## 📧 Contact

For questions or feedback, please open an issue on GitHub.

---

**Made with ❤️ for Singapore Weather**
