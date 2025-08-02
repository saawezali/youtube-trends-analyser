# 🔴 Live YouTube Analytics Dashboard

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/streamlit-1.28+-red.svg)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub issues](https://img.shields.io/github/issues/saawezali/youtube-trends-analyser)](https://github.com/saawezali/youtube-trends-analyser/issues)
[![GitHub stars](https://img.shields.io/github/stars/saawezali/youtube-trends-analyser)](https://github.com/saawezali/youtube-trends-analyser/stargazers)

A powerful, real-time YouTube analytics dashboard that provides live insights into trending videos, search results, and engagement metrics using the YouTube Data API v3.

![Dashboard Preview](<Screenshot 2025-08-02 140420.png>)

## ✨ Features

🔥 **Live Trending Videos** from 15+ countries  
🔍 **Real-time Search** across YouTube's database  
📊 **Interactive Analytics** with beautiful visualizations  
📈 **Engagement Metrics** and performance tracking  
🎬 **Video Gallery** with thumbnails and details  
📥 **Data Export** in multiple formats (CSV, JSON)  
🌍 **Global Coverage** - US, CA, GB, DE, FR, IN, JP, KR, MX, RU, BR, AU, IT, ES, NL  
⚡ **Auto-refresh** capabilities for live monitoring

## 🎯 What This Dashboard Does

Transform YouTube's vast data into actionable insights with:
- **🔥 Live Trending Videos** from 15+ countries
- **🔍 Real-time Search** across YouTube's database  
- **📊 Interactive Analytics** with beautiful visualizations
- **📈 Engagement Metrics** and performance tracking
- **🎬 Video Gallery** with thumbnails and details
- **📥 Data Export** in multiple formats

## 🚀 Quick Start

### 1. Get Your YouTube API Key
1. **Visit**: [Google Cloud Console](https://console.cloud.google.com/)
2. **Create/Select Project**: Choose or create a project
3. **Enable API**: Search for "YouTube Data API v3" and enable it
4. **Create Credentials**: Go to Credentials → Create API Key
5. **Copy Key**: Save your key (looks like `AIzaSyC4K8_...`)

### 2. Install & Run
```bash
# Navigate to project folder
cd youtube_trends_analyser

# Install dependencies
pip install -r requirements.txt

# Test your API key (optional but recommended)
python test_api.py YOUR_API_KEY

# Launch dashboard
streamlit run app.py
```

### 3. Configure API Key
Choose one of these methods:

#### **Option A: Direct Input (Easiest)**
- Run the dashboard: `streamlit run app.py`
- Enter your API key in the sidebar when prompted
- ⚠️ Key is not saved between sessions

#### **Option B: Local Secrets File (Recommended)**
```bash
# Copy the example file
cp .streamlit/secrets.toml.example .streamlit/secrets.toml

# Edit the file and add your actual API key
# YOUTUBE_API_KEY = "your_actual_api_key_here"

# Run dashboard - key will be loaded automatically
streamlit run app.py
```

### 4. Start Analyzing! 
- Open http://localhost:8501 in your browser
- If using Option A, enter your API key in the sidebar
- Explore live YouTube data!

## 🎨 Dashboard Features

### 📊 **Live Metrics Dashboard**
- **Total Videos**: Current count of trending/search results
- **Average Views**: Real-time view averages
- **Engagement Rate**: Live like-to-view ratios
- **Top Category**: Most popular content category

### 🔍 **Data Sources**
- **🔥 Trending Videos**: What's hot right now in any country
- **🔍 Search Videos**: Find specific content across YouTube

### 🌍 **Global Coverage**
15+ regions including: US, CA, GB, DE, FR, IN, JP, KR, MX, RU, BR, AU, IT, ES, NL

### 📈 **Interactive Visualizations**
- **Category Distribution**: Bar charts and pie charts
- **Performance Analysis**: Scatter plots of views vs engagement
- **Channel Rankings**: Top performing channels
- **Video Gallery**: Visual browsing with thumbnails

### ⚡ **Real-time Features**
- **Auto-refresh**: Updates every 30 seconds
- **Live Status**: Connection and update indicators
- **Fresh Data**: Always current information
- **Instant Filtering**: Dynamic category and region filters

## 🎯 Use Cases

### 📺 **Content Creators**
- **Trend Spotting**: See what's viral right now
- **Content Ideas**: Find trending topics in your niche
- **Competitor Analysis**: Monitor other channels' performance
- **Optimal Timing**: Understand when content trends

### 💼 **Marketing Teams**
- **Campaign Monitoring**: Track viral marketing content
- **Audience Insights**: Understand regional preferences
- **Competitive Intelligence**: Monitor competitor strategies
- **Trend Forecasting**: Spot emerging topics early

### 🔬 **Researchers & Analysts**
- **Social Media Studies**: Analyze platform behavior
- **Cultural Research**: Compare regional content preferences
- **Trend Analysis**: Study viral content patterns
- **Data Collection**: Export data for further analysis

### 🎓 **Students & Educators**
- **Data Science Learning**: Hands-on experience with real data
- **API Integration**: Learn to work with REST APIs
- **Visualization Practice**: Create compelling charts
- **Research Projects**: Access to current social media data

## 🔧 Technical Details

### **Built With**
- **Frontend**: Streamlit (Python web framework)
- **Data Processing**: Pandas (data manipulation)
- **Visualizations**: Plotly (interactive charts)
- **API Integration**: Requests (HTTP client)
- **Styling**: Custom CSS for YouTube-themed design

### **Performance**
- **Load Time**: 5-15 seconds (API dependent)
- **Memory Usage**: 50-200MB
- **Caching**: Smart caching reduces API calls
- **Responsiveness**: Works on desktop, tablet, mobile

### **API Usage**
- **Free Tier**: 10,000 units/day
- **Trending Videos**: ~3 units per request
- **Search**: ~100 units per request
- **Categories**: ~1 unit per request
- **Optimization**: Built-in caching minimizes usage

## 📊 Dashboard Sections

### 🔍 **Sidebar Controls**
- **API Key Input**: Secure key management
- **Data Source**: Toggle between trending and search
- **Region Selection**: Choose from 15+ countries
- **Category Filter**: Filter by video categories
- **Auto-refresh**: Enable live updates
- **Manual Refresh**: Update data on demand

### 📈 **Main Dashboard**
- **Live Metrics**: Key performance indicators
- **Tabbed Analytics**: Organized visualizations
- **Video Gallery**: Visual content browser
- **Export Tools**: Download data in multiple formats

### 🎨 **Visualization Tabs**
1. **📊 Categories**: Distribution of video categories
2. **🏆 Top Videos**: Performance analysis and rankings
3. **📈 Engagement**: Engagement rate analysis
4. **🌍 Channels**: Top performing channels
5. **🎬 Video Gallery**: Visual video browser

## 🔒 Security & Best Practices

### **API Key Security**
- **Never share** your API key publicly
- **Use secrets.toml** for local development
- **Environment variables** for production
- **Restrict API key** to YouTube Data API only

### **Quota Management**
- **Monitor usage** in Google Cloud Console
- **Set up alerts** at 80% quota usage
- **Use caching** to reduce API calls
- **Optimize requests** with appropriate limits

## 🚀 Deployment Options

### **Local Development**
```bash
streamlit run app.py
```

### **Streamlit Cloud**
1. Push to GitHub repository
2. Connect to Streamlit Cloud
3. Add API key to secrets
4. Deploy automatically

### **Docker**
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

## 🔧 Troubleshooting

### **Common Issues**

#### "API Connection Failed"
- **Check**: API key is correct and complete
- **Verify**: YouTube Data API v3 is enabled
- **Monitor**: Quota usage in Google Cloud Console

#### "No data available"
- **Try**: Different regions or categories
- **Check**: Internet connection
- **Verify**: API quotas not exceeded

#### Slow Performance
- **Reduce**: Max results limit
- **Avoid**: Frequent manual refreshes
- **Use**: Auto-refresh sparingly

### **Getting Help**
- **Test API**: Use `python test_api.py YOUR_KEY`
- **Check Logs**: Look for error messages in terminal
- **Verify Setup**: Ensure all dependencies installed

## 📈 Example Insights

### **Trending Analysis**
- "Gaming videos dominate in South Korea with 45% of trending content"
- "Music videos average 2.3M views in India vs 1.1M globally"
- "Educational content peaks at 3PM EST in the US"

### **Search Intelligence**
- "Python tutorial searches return 89% programming content"
- "Music video searches show 156% higher engagement rates"
- "Gaming content averages 234K likes per video"

### **Performance Benchmarks**
- "Top 10% of videos achieve 3.2% engagement rates"
- "Trending videos average 48 hours from publish to trend"
- "Entertainment category shows highest comment rates"

## 🎉 Success Metrics

Your dashboard is working perfectly when you see:
- ✅ Green API connection status
- ✅ Live data loading without errors
- ✅ Interactive visualizations updating
- ✅ Video thumbnails displaying
- ✅ Export functions working
- ✅ Auto-refresh functioning (if enabled)

## 🔮 What's Next?

This dashboard provides a solid foundation for YouTube analytics. Potential enhancements:
- **Multi-platform**: Add Instagram, TikTok data
- **AI Insights**: Machine learning trend prediction
- **Custom Alerts**: Notifications for specific trends
- **Advanced Analytics**: Sentiment analysis, topic modeling

## 📞 Support

Need help? Here's how to get support:
1. **Test your setup**: `python test_api.py YOUR_KEY`
2. **Check documentation**: Review this README
3. **Verify API key**: Ensure it's valid and has quota
4. **Check internet**: Ensure stable connection

---

## 🚀 Ready to Explore?

Transform your understanding of YouTube trends with real-time data:

```bash
# Quick start
pip install -r requirements.txt
python test_api.py YOUR_API_KEY
streamlit run app.py
```

**Your YouTube intelligence center awaits!** 🎬📊🔴

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### Quick Contribution Steps
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **YouTube Data API v3** for providing the data
- **Streamlit** for the amazing web framework
- **Plotly** for interactive visualizations
- **Contributors** who help improve this project

## 📊 Project Stats

- **Language**: Python
- **Framework**: Streamlit
- **API**: YouTube Data API v3
- **Visualizations**: Plotly
- **License**: MIT

## 🔗 Links
- [Live Demo](https://liveyoutubetrends.streamlit.app/)
- [Documentation](README.md)
- [Issues](https://github.com/saawezali/youtube-trends-analyser/issues)
- [Contributing](CONTRIBUTING.md)

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### Quick Contribution Steps
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **YouTube Data API v3** for providing the data
- **Streamlit** for the amazing web framework
- **Plotly** for interactive visualizations
- **Contributors** who help improve this project

## 📊 Project Stats

- **Language**: Python
- **Framework**: Streamlit
- **API**: YouTube Data API v3
- **Visualizations**: Plotly
- **License**: MIT

## Author

- [Saawez Ali]([https://www.linkedin.com/in/your-link](https://www.linkedin.com/in/saawez-ali-a7016a291/)  

---
