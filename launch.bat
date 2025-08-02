@echo off
echo 🔴 Live YouTube Analytics Dashboard
echo ===================================
echo.

echo 📦 Installing required packages...
pip install -r requirements.txt

echo.
echo 🔑 Make sure you have your YouTube API key ready!
echo Get it from: https://console.cloud.google.com/
echo.

echo 🌐 Starting dashboard...
echo 📱 Opening in browser at: http://localhost:8501
echo 🔑 Enter your API key in the sidebar when prompted
echo 🛑 Press Ctrl+C to stop
echo.

streamlit run app.py

pause