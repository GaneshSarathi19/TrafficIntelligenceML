import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import plotly.graph_objects as go
import plotly.express as px
import time
import joblib
from pathlib import Path

# Page config
st.set_page_config(page_title="Traffic Analytics ML", page_icon="🚗", layout="wide", initial_sidebar_state="expanded")

# Model loading function
@st.cache_resource
def load_models():
    """Load trained models if they exist, otherwise return None"""
    models = {}
    model_dir = Path("models")
    
    if not model_dir.exists():
        return None
    
    try:
        # Try to load clustering models + preprocessors
        kmeans_path = model_dir / "clustering_kmeans.pkl"
        if kmeans_path.exists():
            models['clustering_kmeans'] = joblib.load(kmeans_path)
        
        agglomerative_path = model_dir / "clustering_agglomerative.pkl"
        if agglomerative_path.exists():
            models['clustering_agglomerative'] = joblib.load(agglomerative_path)
        
        # Load clustering preprocessors
        le_road_path = model_dir / "clustering_le_road.pkl"
        if le_road_path.exists():
            models['clustering_le_road'] = joblib.load(le_road_path)
            
        le_day_path = model_dir / "clustering_le_day.pkl"
        if le_day_path.exists():
            models['clustering_le_day'] = joblib.load(le_day_path)
            
        scaler_cluster_path = model_dir / "clustering_scaler.pkl"
        if scaler_cluster_path.exists():
            models['clustering_scaler'] = joblib.load(scaler_cluster_path)
        
        # Try to load classification models
        for algo in ['logistic', 'knn', 'naive_bayes', 'decision_tree', 'svm', 
                     'random_forest', 'adaboost', 'gradient_boosting', 'bagging', 'mlp']:
            model_path = model_dir / f"classification_{algo}.pkl"
            if model_path.exists():
                models[f'classification_{algo}'] = joblib.load(model_path)
        
        # Load classification scaler
        scaler_class_path = model_dir / "classification_scaler.pkl"
        if scaler_class_path.exists():
            models['classification_scaler'] = joblib.load(scaler_class_path)
        
        # Try to load regression models
        for algo in ['linear', 'ridge', 'lasso', 'elasticnet', 'decision_tree',
                     'random_forest', 'gradient_boosting', 'adaboost', 'xgboost', 'svr']:
            model_path = model_dir / f"regression_{algo}.pkl"
            if model_path.exists():
                models[f'regression_{algo}'] = joblib.load(model_path)
        
        # Load regression scaler
        scaler_reg_path = model_dir / "regression_scaler.pkl"
        if scaler_reg_path.exists():
            models['regression_scaler'] = joblib.load(scaler_reg_path)
        
        return models if models else None
    except Exception as e:
        st.warning(f"Error loading models: {e}")
        return None

# Load models at startup
#loaded_models = load_models()
loaded_models = None
using_real_models = loaded_models is not None and len(loaded_models) > 0

# Count only algorithm models (exclude scalers/encoders)
algorithm_model_count = 0
if loaded_models:
    algorithm_models = [k for k in loaded_models.keys() if not any(x in k for x in ['scaler', 'le_', '_encoder'])]
    algorithm_model_count = len(algorithm_models)

# Enhanced CSS with animations
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    * { font-family: 'Poppins', sans-serif; }
    .main-header {
        font-size: 3.5rem; font-weight: 700;
        background: linear-gradient(120deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        text-align: center; padding: 2rem 0;
        animation: gradient 3s ease infinite; background-size: 200% 200%;
    }
    @keyframes gradient { 0% { background-position: 0% 50%; } 50% { background-position: 100% 50%; } 100% { background-position: 0% 50%; } }
    .subtitle { text-align: center; color: #666; font-size: 1.2rem; margin-bottom: 2rem; animation: fadeIn 1s ease-in; }
    @keyframes fadeIn { from { opacity: 0; transform: translateY(-10px); } to { opacity: 1; transform: translateY(0); } }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem; border-radius: 15px; color: white;
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
        transition: all 0.3s ease; animation: slideUp 0.5s ease;
    }
    .metric-card:hover { transform: translateY(-10px); box-shadow: 0 15px 40px rgba(102, 126, 234, 0.5); }
    @keyframes slideUp { from { opacity: 0; transform: translateY(30px); } to { opacity: 1; transform: translateY(0); } }
    .stButton>button {
        width: 100%; background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white; border: none; padding: 1rem; border-radius: 12px;
        font-weight: 600; font-size: 1.1rem; transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
    }
    .stButton>button:hover {
        transform: translateY(-3px); box-shadow: 0 8px 25px rgba(102, 126, 234, 0.5);
        background: linear-gradient(90deg, #764ba2 0%, #667eea 100%);
    }
    .prediction-box {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        padding: 2.5rem; border-radius: 15px; border-left: 6px solid #667eea;
        margin: 1.5rem 0; box-shadow: 0 5px 20px rgba(0,0,0,0.1); animation: popIn 0.5s ease;
    }
    @keyframes popIn { 0% { transform: scale(0.8); opacity: 0; } 100% { transform: scale(1); opacity: 1; } }
    .feature-box {
        background: white; padding: 1.5rem; border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08); margin: 1rem 0;
        border-left: 4px solid #667eea; transition: all 0.3s ease;
    }
    .feature-box:hover { box-shadow: 0 8px 25px rgba(0,0,0,0.12); transform: translateX(5px); }
    .info-badge {
        background: linear-gradient(90deg, #667eea, #764ba2);
        color: white; padding: 0.5rem 1rem; border-radius: 20px;
        display: inline-block; font-size: 0.9rem; font-weight: 600;
        margin: 0.3rem; box-shadow: 0 3px 10px rgba(102, 126, 234, 0.3);
    }
    .success-box {
        background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
        padding: 2rem; border-radius: 12px; color: white; text-align: center;
        animation: pulse 2s infinite;
    }
    @keyframes pulse { 0%, 100% { transform: scale(1); } 50% { transform: scale(1.02); } }
    .warning-box {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 1.5rem; border-radius: 12px; color: white; margin: 1rem 0;
    }
    .model-status {
        background: linear-gradient(90deg, #11998e, #38ef7d);
        color: white; padding: 0.8rem 1.5rem; border-radius: 25px;
        display: inline-block; font-weight: 600; margin: 1rem 0;
        box-shadow: 0 4px 15px rgba(17, 153, 142, 0.3);
    }
    .stMetric { background: white; padding: 1rem; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.05); }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<p class="main-header">🚗 Traffic Analytics ML Platform</p>', unsafe_allow_html=True)

# Model status indicator
if using_real_models:
    st.markdown(f"""
    <div class="model-status">
        ✅ Using Trained Models ({algorithm_model_count} algorithms loaded)
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <div class="warning-box">
        ⚠️ <strong>Demo Mode:</strong> Using simulated predictions. Train and save your models to enable real ML predictions!
        <br><small>Place your trained models in the 'models/' folder. See EXPORT_MODELS_FROM_NOTEBOOKS.md for instructions.</small>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<p class="subtitle">🎯 Advanced Machine Learning • Real-time Predictions • Multiple Algorithms</p>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("### 🎨 Navigation")
    track = st.radio("", ["🏠 Home", "📊 Clustering", "🎯 Classification", "📈 Regression"], label_visibility="collapsed")
    
    st.markdown("---")
    st.markdown("### 🤖 Model Status")
    if using_real_models:
        st.success(f"✅ {algorithm_model_count} algorithms loaded")
        st.metric("Mode", "Real ML", delta="Active")
    else:
        st.warning("⚠️ Demo Mode")
        st.metric("Mode", "Simulated", delta="Train models")
    
    st.markdown("---")
    st.markdown("### 📊 Algorithm Stats")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("🔵 Clustering", "2", delta="algos")
    with col2:
        st.metric("🟢 Classification", "10", delta="algos")
    st.metric("🟣 Regression", "10", delta="algos")

# HOME PAGE
if track == "🏠 Home":
    st.markdown("## 🎉 Welcome to Traffic Analytics Platform")
    
    # Instructions based on model status
    if not using_real_models:
        st.markdown("""
        ### 📋 To Enable Real ML Predictions:
        
        1. **Train Your Models** in Jupyter notebooks
        2. **Save Models** using joblib:
           ```python
           import joblib
           joblib.dump(model, 'models/clustering_kmeans.pkl')
           ```
        3. **Restart App** - Models will auto-load!
        
        **Currently showing simulated predictions for demonstration.**
        """)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h2 style="text-align:center">📊</h2>
            <h3 style="text-align:center">Clustering</h3>
            <p style="text-align:center;font-size:1.1rem">Identify traffic patterns</p>
            <hr style="border-color:rgba(255,255,255,0.3)">
            <p><strong>Algorithms:</strong></p>
            <ul>
                <li>✓ K-Means Clustering</li>
                <li>✓ Agglomerative Clustering</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h2 style="text-align:center">🎯</h2>
            <h3 style="text-align:center">Classification</h3>
            <p style="text-align:center;font-size:1.1rem">Predict Level of Service</p>
            <hr style="border-color:rgba(255,255,255,0.3)">
            <p><strong>10 Algorithms:</strong></p>
            <ul>
                <li>✓ Logistic Regression</li>
                <li>✓ Random Forest</li>
                <li>+ 8 more algorithms</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h2 style="text-align:center">📈</h2>
            <h3 style="text-align:center">Regression</h3>
            <p style="text-align:center;font-size:1.1rem">Forecast traffic volume</p>
            <hr style="border-color:rgba(255,255,255,0.3)">
            <p><strong>10 Algorithms:</strong></p>
            <ul>
                <li>✓ XGBoost Regressor</li>
                <li>✓ Random Forest</li>
                <li>+ 8 more algorithms</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# CLUSTERING TRACK
elif track == "📊 Clustering":
    st.markdown("## 📊 Traffic Pattern Clustering")
    
    # Algorithm selection
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔵 K-Means Clustering", use_container_width=True):
            st.session_state.clustering_algo = "K-Means Clustering"
    with col2:
        if st.button("🟢 Agglomerative Clustering", use_container_width=True):
            st.session_state.clustering_algo = "Agglomerative Clustering"
    
    if 'clustering_algo' not in st.session_state:
        st.session_state.clustering_algo = "K-Means Clustering"
    
    algo = st.session_state.clustering_algo
    
    # Check if this specific model is loaded
    model_key = 'clustering_kmeans' if 'K-Means' in algo else 'clustering_agglomerative'
    model_available = using_real_models and model_key in loaded_models
    
    if model_available:
        st.markdown(f"""
        <div class="success-box">
            <h3>✅ Using: {algo}</h3>
            <p style="font-size:0.9rem;">Trained model: {model_key}.pkl</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="success-box">
            <h3>🎮 Demo Mode: {algo}</h3>
            <p style="font-size:0.9rem;">Using rule-based simulation</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Inputs
    col1, col2 = st.columns(2)
    with col1:
        road = st.selectbox("Road ID", ["R1", "R2", "R3", "R4"])
        hour = st.slider("Hour", 0, 23, 12)
    with col2:
        day = st.selectbox("Day", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
        delay = st.number_input("Delay (min)", -5.0, 10.0, 0.0, 0.1)
    
    if st.button("🔍 PREDICT CLUSTER", use_container_width=True):
        with st.spinner("🔄 Analyzing..."):
            progress_bar = st.progress(0)
            for i in range(100):
                time.sleep(0.01)
                progress_bar.progress(i + 1)
            
            # REAL MODEL PREDICTION or SIMULATED
            if model_available:
                try:
                    # Encode categorical variables
                    road_encoded = loaded_models['clustering_le_road'].transform([road])[0]
                    day_encoded = loaded_models['clustering_le_day'].transform([day])[0]
                    
                    # Prepare input
                    input_data = np.array([[road_encoded, hour, day_encoded, delay]])
                    
                    # Scale features
                    if 'clustering_scaler' in loaded_models:
                        input_data_scaled = loaded_models['clustering_scaler'].transform(input_data)
                    else:
                        input_data_scaled = input_data
                    
                    # Predict
                    prediction = loaded_models[model_key].predict(input_data_scaled)[0]
                    
                    # Map prediction to cluster name
                    cluster_map = {0: 'FREE', 1: 'LIGHT', 2: 'MODERATE', 3: 'HEAVY'}
                    cluster = cluster_map.get(prediction, f'CLUSTER_{prediction}')
                    
                    source = f"✅ {algo}"
                except Exception as e:
                    st.error(f"Model prediction failed: {e}. Using fallback.")
                    # Fallback to simulated
                    cluster = "HEAVY" if delay > 2 else ("MODERATE" if delay > 1 else ("LIGHT" if delay > 0 else "FREE"))
                    source = "⚠️ Fallback (Error)"
            else:
                # SIMULATED PREDICTION
                cluster = "HEAVY" if delay > 2 else ("MODERATE" if delay > 1 else ("LIGHT" if delay > 0 else "FREE"))
                source = "🎮 Simulated"
            
            color = {"HEAVY": "#dc3545", "MODERATE": "#ffc107", "LIGHT": "#28a745", "FREE": "#17a2b8"}[cluster]
            
            st.markdown(f"""
            <div class="prediction-box">
                <h2 style="color:{color};text-align:center">Cluster: {cluster}</h2>
                <p style="text-align:center">Source: <strong>{source}</strong></p>
            </div>
            """, unsafe_allow_html=True)

# CLASSIFICATION TRACK
elif track == "🎯 Classification":
    st.markdown("## 🎯 LOS Classification")
    
    algos = ["Logistic Regression", "K-Nearest Neighbors", "Gaussian Naive Bayes", "Decision Tree",
             "Support Vector Machine", "Random Forest", "AdaBoost", "Gradient Boosting", "Bagging", "Neural Network (MLP)"]
    
    # Map display names to model keys
    algo_key_map = {
        "Logistic Regression": "logistic",
        "K-Nearest Neighbors": "knn",
        "Gaussian Naive Bayes": "naive_bayes",
        "Decision Tree": "decision_tree",
        "Support Vector Machine": "svm",
        "Random Forest": "random_forest",
        "AdaBoost": "adaboost",
        "Gradient Boosting": "gradient_boosting",
        "Bagging": "bagging",
        "Neural Network (MLP)": "mlp"
    }
    
    cols = st.columns(5)
    for idx, algo_name in enumerate(algos[:5]):
        with cols[idx]:
            if st.button(f"{algo_name[:10]}...", use_container_width=True, key=f"c{idx}"):
                st.session_state.class_algo = algo_name
    
    cols2 = st.columns(5)
    for idx, algo_name in enumerate(algos[5:]):
        with cols2[idx]:
            if st.button(f"{algo_name[:10]}...", use_container_width=True, key=f"c{idx+5}"):
                st.session_state.class_algo = algo_name
    
    if 'class_algo' not in st.session_state:
        st.session_state.class_algo = "Random Forest"
    
    algo = st.session_state.class_algo
    
    # Check if this specific model is loaded
    model_key = f'classification_{algo_key_map[algo]}'
    model_available = using_real_models and model_key in loaded_models
    
    if model_available:
        st.markdown(f"""
        <div class="success-box">
            <h3>✅ Using: {algo}</h3>
            <p style="font-size:0.9rem;">Trained model: {model_key}.pkl</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="success-box">
            <h3>🎮 Demo Mode: {algo}</h3>
            <p style="font-size:0.9rem;">Using rule-based simulation</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        cong = st.slider("Congestion", 0, 6, 3)
    with col2:
        workers = st.number_input("Workers", 0, 3000, 500)
    with col3:
        income = st.number_input("Income", 0, 300000, 90000, 1000)
    
    if st.button("🎯 PREDICT LOS", use_container_width=True):
        with st.spinner("Classifying..."):
            progress_bar = st.progress(0)
            for i in range(100):
                time.sleep(0.01)
                progress_bar.progress(i + 1)
            
            # REAL MODEL PREDICTION or SIMULATED
            if model_available:
                try:
                    # Prepare input (Congestion_Index, Workers, Income)
                    input_data = np.array([[cong, workers, income]])
                    
                    # Scale features
                    if 'classification_scaler' in loaded_models:
                        input_data_scaled = loaded_models['classification_scaler'].transform(input_data)
                    else:
                        input_data_scaled = input_data
                    
                    # Predict
                    prediction = loaded_models[model_key].predict(input_data_scaled)[0]
                    
                    # Map prediction to LOS name
                    los_map = {0: 'Good', 1: 'Medium', 2: 'Poor'}
                    los = los_map.get(prediction, 'Unknown')
                    
                    source = f"✅ {algo}"
                except Exception as e:
                    st.error(f"Model prediction failed: {e}. Using fallback.")
                    # Fallback to simulated
                    los = "Poor" if cong >= 5 else ("Medium" if cong >= 3 else "Good")
                    source = "⚠️ Fallback (Error)"
            else:
                # SIMULATED PREDICTION
                los = "Poor" if cong >= 5 else ("Medium" if cong >= 3 else "Good")
                source = "🎮 Simulated"
            
            color = {"Poor": "#dc3545", "Medium": "#ffc107", "Good": "#28a745"}.get(los, "#6c757d")
            
            st.markdown(f"""
            <div class="prediction-box">
                <h2 style="color:{color};text-align:center">LOS: {los}</h2>
                <p style="text-align:center">Source: <strong>{source}</strong></p>
            </div>
            """, unsafe_allow_html=True)

# REGRESSION TRACK
elif track == "📈 Regression":
    st.markdown("## 📈 Traffic Volume Prediction")
    
    reg_algos = ["Linear Regression", "Ridge", "Lasso", "ElasticNet", "Decision Tree",
                 "Random Forest", "Gradient Boosting", "AdaBoost", "XGBoost", "Support Vector Regression"]
    
    # Map display names to model keys
    reg_algo_key_map = {
        "Linear Regression": "linear",
        "Ridge": "ridge",
        "Lasso": "lasso",
        "ElasticNet": "elasticnet",
        "Decision Tree": "decision_tree",
        "Random Forest": "random_forest",
        "Gradient Boosting": "gradient_boosting",
        "AdaBoost": "adaboost",
        "XGBoost": "xgboost",
        "Support Vector Regression": "svr"
    }
    
    cols = st.columns(5)
    for idx, algo_name in enumerate(reg_algos[:5]):
        with cols[idx]:
            if st.button(f"{algo_name[:8]}...", use_container_width=True, key=f"r{idx}"):
                st.session_state.reg_algo = algo_name
    
    cols2 = st.columns(5)
    for idx, algo_name in enumerate(reg_algos[5:]):
        with cols2[idx]:
            if st.button(f"{algo_name[:8]}...", use_container_width=True, key=f"r{idx+5}"):
                st.session_state.reg_algo = algo_name
    
    if 'reg_algo' not in st.session_state:
        st.session_state.reg_algo = "XGBoost"
    
    algo = st.session_state.reg_algo
    
    # Check if this specific model is loaded
    model_key = f'regression_{reg_algo_key_map[algo]}'
    model_available = using_real_models and model_key in loaded_models
    
    if model_available:
        st.markdown(f"""
        <div class="success-box">
            <h3>✅ Using: {algo}</h3>
            <p style="font-size:0.9rem;">Trained model: {model_key}.pkl</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="success-box">
            <h3>🎮 Demo Mode: {algo}</h3>
            <p style="font-size:0.9rem;">Using rule-based simulation</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    with col1:
        temp = st.slider("Temperature (K)", 250.0, 315.0, 285.0)
        hr = st.slider("Hour", 0, 23, 12)
    with col2:
        rain = st.number_input("Rain (mm)", 0.0, 100.0, 0.0)
        holiday = st.checkbox("Holiday?")
    
    if st.button("📊 PREDICT VOLUME", use_container_width=True):
        with st.spinner("Forecasting..."):
            progress_bar = st.progress(0)
            for i in range(100):
                time.sleep(0.01)
                progress_bar.progress(i + 1)
            
            # REAL MODEL PREDICTION or SIMULATED
            if model_available:
                try:
                    # Prepare input (temp, hour, rain_1h, holiday_binary)
                    holiday_binary = 1 if holiday else 0
                    input_data = np.array([[temp, hr, rain, holiday_binary]])
                    
                    # Scale features
                    if 'regression_scaler' in loaded_models:
                        input_data_scaled = loaded_models['regression_scaler'].transform(input_data)
                    else:
                        input_data_scaled = input_data
                    
                    # Predict
                    prediction = loaded_models[model_key].predict(input_data_scaled)[0]
                    
                    # Ensure positive volume
                    vol = max(0, int(prediction))
                    
                    source = f"✅ {algo}"
                except Exception as e:
                    st.error(f"Model prediction failed: {e}. Using fallback.")
                    # Fallback to simulated
                    base = 3500
                    factor = 1.5 if (7 <= hr <= 9 or 16 <= hr <= 18) else 1.0
                    if rain > 5:
                        factor *= 0.8
                    vol = int(base * factor)
                    source = "⚠️ Fallback (Error)"
            else:
                # SIMULATED PREDICTION
                base = 3500
                factor = 1.5 if (7 <= hr <= 9 or 16 <= hr <= 18) else 1.0
                if rain > 5:
                    factor *= 0.8
                vol = int(base * factor)
                source = "🎮 Simulated"
            
            st.markdown(f"""
            <div class="prediction-box">
                <h2 style="text-align:center">{vol:,} vehicles/hr</h2>
                <p style="text-align:center">Source: <strong>{source}</strong></p>
            </div>
            """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align:center;padding:2rem;background:linear-gradient(90deg,#667eea,#764ba2);color:white;border-radius:15px'>
    <h3>🚗 Traffic Analytics ML Platform</h3>
    <p>Powered by Machine Learning | 22 Algorithms | Smart Model Integration</p>
</div>
""", unsafe_allow_html=True)
