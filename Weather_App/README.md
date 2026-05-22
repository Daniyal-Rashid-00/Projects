# 🌤️ Python CLI Weather Application

A lightweight, robust Command Line Interface (CLI) application built in Python that interfaces with external REST APIs to fetch and parse real-time meteorological data.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/REST_API-005571?style=for-the-badge&logo=openapi-initiative" alt="REST API">
</p>

---

## 🏗️ Technical Highlights

This project demonstrates strong fundamental backend skills, specifically focusing on network requests, JSON data traversal, and environment variable management in Python.

### Features
- **RESTful API Integration:** Utilizes the `requests` library to interface with third-party Weather APIs (e.g., OpenWeatherMap/WeatherAPI), handling GET requests and URL parameter encoding.
- **Data Parsing:** Demonstrates efficient traversal of complex nested JSON payloads to extract relevant data points (Temperature, Humidity, Conditions).
- **Secure Configuration:** Employs `python-dotenv` to manage secrets, keeping sensitive API keys entirely out of version control.
- **Robust Error Handling:** Features `try/except` blocks to gracefully catch and handle `HTTP 404` (City Not Found), network timeouts, and authentication errors.

---

## 🛠️ Local Setup

1. **Clone the repository:**
```bash
git clone https://github.com/YOUR_USERNAME/Weather_App.git
cd Weather_App
```

2. **Install requirements:**
Ensure you have the `requests` and `python-dotenv` packages installed.
```bash
pip install requests python-dotenv
```

3. **Configure API Keys:**
Create a `.env` file in the root directory and add your weather service API key:
```env
# Example .env configuration
API_KEY=your_secured_api_key_here
```

4. **Run the Application:**
```bash
python Weather_App_2.py
```

---

## 👨‍💻 About The Developer

Built by **Daniyal Rashid** as a demonstration of clean Python scripting and external API integration. 

🔗 **[View My Portfolio & Resume](https://daniyal-rashid.vercel.app/)**
