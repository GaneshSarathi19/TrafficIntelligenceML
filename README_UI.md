# 🚗 Traffic Analytics ML Platform

A beautiful, interactive web application for traffic analysis using Machine Learning with three distinct tracks: Clustering, Classification, and Regression.

## 🌟 Features

### 📊 Clustering Track
- Identify traffic patterns based on road conditions
- Input features: Road ID, Hour, Day, Traffic Delay
- Predicts: Traffic congestion levels (FREE, LIGHT, MODERATE, HEAVY)
- Interactive gauge visualization

### 🎯 Classification Track
- Predict Level of Service (LOS) for urban areas
- Multiple features including socioeconomic, transportation, and land use data
- Predicts: LOS categories (Good, Medium, Poor)
- Confidence scores and probability distributions
- Supports 50+ input features

### 📈 Regression Track
- Forecast hourly traffic volume
- Weather conditions: Temperature, Rain, Snow, Cloud coverage
- Temporal factors: Date, Time, Day of week, Holiday status
- Visual 24-hour traffic pattern analysis
- Detailed weather and temporal insights

## 🚀 Quick Start

### Installation

1. **Install required packages:**
```bash
pip install -r requirements.txt
```

2. **Run the application:**
```bash
streamlit run app.py
```

3. **Open your browser:**
The app will automatically open at `http://localhost:8501`

## 📖 How to Use

### Step 1: Select Your Track
Use the sidebar to choose between:
- 🏠 **Home** - Overview and getting started
- 📊 **Clustering** - Pattern recognition
- 🎯 **Classification** - LOS prediction
- 📈 **Regression** - Volume forecasting

### Step 2: Enter Input Values

#### For Clustering:
- **Road ID**: Select from R1, R2, R3, R4
- **Hour**: 0-23 (24-hour format)
- **Day**: Monday through Sunday
- **Delay**: Traffic delay in minutes (-5 to 10)

#### For Classification:
- **Basic Tab**: Congestion index, average height, transportation data
- **Advanced Tab**: Land use percentages, infrastructure distances
- Total of 50+ features available for comprehensive analysis

#### For Regression:
- **Weather**: Temperature (K), Rain (mm), Snow (mm), Cloud coverage (%)
- **Temporal**: Date, hour, day of week, holiday status
- **Conditions**: Main weather description

### Step 3: Get Predictions
Click the "Predict" button to:
- Get instant ML-powered predictions
- View confidence scores and metrics
- Explore interactive visualizations
- Understand key insights and factors

## 🎨 UI Features

### Modern Design
- Gradient color schemes
- Responsive layout
- Interactive charts with Plotly
- Clean, professional interface

### User Experience
- Real-time input validation
- Helpful tooltips and descriptions
- Clear metric displays
- Visual feedback for predictions

### Visualizations
- Gauge charts for clustering
- Bar charts for classification probabilities
- Line charts for regression patterns
- Interactive hover information

## 📊 Data Sources

- **Clustering Dataset**: 437 records from LA traffic data
- **Classification Dataset**: 28,092 records with LOS causal features
- **Regression Dataset**: 48,204 hourly traffic volume records

## 🔧 Technical Stack

- **Frontend**: Streamlit
- **Visualization**: Plotly
- **Data Processing**: Pandas, NumPy
- **ML Framework**: Scikit-learn (for model integration)
- **Styling**: Custom CSS for enhanced UI

## 🎯 Model Integration

Currently, the app uses simulated predictions for demonstration. To integrate your trained models:

1. **Save your trained models:**
```python
import joblib
joblib.dump(clustering_model, 'models/clustering_model.pkl')
joblib.dump(classification_model, 'models/classification_model.pkl')
joblib.dump(regression_model, 'models/regression_model.pkl')
```

2. **Load models in app.py:**
```python
import joblib

# At the top of app.py
clustering_model = joblib.load('models/clustering_model.pkl')
classification_model = joblib.load('models/classification_model.pkl')
regression_model = joblib.load('models/regression_model.pkl')
```

3. **Replace simulated predictions:**
Replace the simulated prediction code with actual model predictions:
```python
# Example for regression
prediction = regression_model.predict([[temp, rain_1h, snow_1h, clouds_all, ...]])
```

## 📁 Project Structure

```
.
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── README_UI.md           # This file
├── data/                  # Data directory
│   ├── clustering/
│   │   └── ml_dataset.xlsx
│   ├── LOS_CausalFeatures_LosAngeles.csv
│   └── Metro_Interstate_Traffic_Volume.csv
├── notebooks/             # Jupyter notebooks
│   ├── clustering/
│   │   └── traffic_clustering.ipynb
│   ├── classification.ipynb
│   └── regression.ipynb
└── models/               # Saved ML models (create this)
    ├── clustering_model.pkl
    ├── classification_model.pkl
    └── regression_model.pkl
```

## 🌐 Deployment

### Deploy to Streamlit Cloud

1. Push your code to GitHub
2. Visit [share.streamlit.io](https://share.streamlit.io)
3. Connect your repository
4. Deploy!

### Deploy to Heroku

1. Create a `Procfile`:
```
web: streamlit run app.py --server.port=$PORT
```

2. Deploy:
```bash
heroku create your-app-name
git push heroku main
```

## 🎓 Use Cases

- **Urban Planning**: Predict traffic patterns for city development
- **Transportation Management**: Forecast traffic volume for resource allocation
- **Traffic Engineering**: Analyze Level of Service for road improvements
- **Research**: Study relationships between urban features and traffic

## 💡 Tips

1. **Best Times to Use Each Track:**
   - Clustering: Pattern analysis and congestion identification
   - Classification: Urban planning and LOS assessment
   - Regression: Real-time traffic forecasting

2. **Input Recommendations:**
   - Use realistic values based on your location
   - Consider peak hours (7-9 AM, 4-6 PM) for higher accuracy
   - Include weather data when available

3. **Interpreting Results:**
   - Higher confidence scores indicate more reliable predictions
   - Consider multiple factors when making decisions
   - Use visualizations to understand patterns

## 🐛 Troubleshooting

**App won't start:**
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Check Python version (3.8 or higher recommended)

**Predictions seem inaccurate:**
- Remember: Current version uses simulated models
- Integrate your trained models for real predictions

**Visualizations not showing:**
- Clear browser cache
- Try a different browser
- Check Plotly installation

## 📧 Support

For questions or issues:
1. Check existing notebooks for model training details
2. Review the data files in the `data/` directory
3. Consult Streamlit documentation: [docs.streamlit.io](https://docs.streamlit.io)

## 🔮 Future Enhancements

- [ ] Real-time data integration
- [ ] Model comparison dashboard
- [ ] Historical data visualization
- [ ] Batch prediction upload
- [ ] Export prediction reports
- [ ] A/B testing for models
- [ ] Interactive map visualization
- [ ] API endpoint creation

## 📝 License

This project is part of a Machine Learning capstone project.

---

**Built with ❤️ using Streamlit | Traffic Analytics ML Platform v1.0**
