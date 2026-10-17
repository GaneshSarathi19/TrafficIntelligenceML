"""
Model Integration Helper Script

This script helps you integrate your trained models from Jupyter notebooks
into the Streamlit application.

Usage:
    1. Train and save your models using the provided template
    2. Update app.py to load and use the saved models
"""

import joblib
import pandas as pd
import numpy as np
from pathlib import Path

# Create models directory if it doesn't exist
models_dir = Path("models")
models_dir.mkdir(exist_ok=True)

print("=" * 60)
print("ML Model Integration Helper")
print("=" * 60)

# ============================================================================
# STEP 1: Example of how to save models from your notebooks
# ============================================================================

print("\n📝 STEP 1: Save Your Trained Models")
print("-" * 60)
print("""
In your Jupyter notebooks, after training your models, save them like this:

# Example for Clustering
import joblib
joblib.dump(kmeans_model, 'models/clustering_model.pkl')
joblib.dump(scaler, 'models/clustering_scaler.pkl')  # If you used scaling

# Example for Classification
joblib.dump(best_classifier, 'models/classification_model.pkl')
joblib.dump(feature_scaler, 'models/classification_scaler.pkl')
joblib.dump(label_encoder, 'models/classification_encoder.pkl')

# Example for Regression
joblib.dump(best_regressor, 'models/regression_model.pkl')
joblib.dump(preprocessor, 'models/regression_preprocessor.pkl')
""")

# ============================================================================
# STEP 2: Model loading template for app.py
# ============================================================================

print("\n📦 STEP 2: Load Models in app.py")
print("-" * 60)
print("""
Add this code at the beginning of app.py (after imports):

import joblib
from pathlib import Path

# Load models
@st.cache_resource
def load_models():
    models = {}
    
    try:
        # Clustering models
        models['clustering'] = joblib.load('models/clustering_model.pkl')
        models['clustering_scaler'] = joblib.load('models/clustering_scaler.pkl')
        
        # Classification models
        models['classification'] = joblib.load('models/classification_model.pkl')
        models['classification_scaler'] = joblib.load('models/classification_scaler.pkl')
        models['classification_encoder'] = joblib.load('models/classification_encoder.pkl')
        
        # Regression models
        models['regression'] = joblib.load('models/regression_model.pkl')
        models['regression_preprocessor'] = joblib.load('models/regression_preprocessor.pkl')
        
        return models
    except FileNotFoundError as e:
        st.warning(f"Model file not found: {e}. Using simulated predictions.")
        return None

# Load all models at startup
models = load_models()
""")

# ============================================================================
# STEP 3: Prediction examples
# ============================================================================

print("\n🎯 STEP 3: Make Predictions")
print("-" * 60)
print("""
Replace the simulated prediction code with actual predictions:

# ========== CLUSTERING ==========
if models and 'clustering' in models:
    # Prepare input
    input_data = pd.DataFrame({
        'road_id': [road_id],
        'hour': [hour],
        'day': [day],
        'delay': [delay]
    })
    
    # Encode categorical variables if needed
    # input_encoded = encoder.transform(input_data)
    
    # Scale if needed
    input_scaled = models['clustering_scaler'].transform(input_data)
    
    # Predict
    cluster = models['clustering'].predict(input_scaled)[0]
    
    # Map cluster to congestion level
    cluster_map = {0: 'FREE', 1: 'LIGHT', 2: 'MODERATE', 3: 'HEAVY'}
    result = cluster_map.get(cluster, 'UNKNOWN')

# ========== CLASSIFICATION ==========
if models and 'classification' in models:
    # Prepare input features
    input_features = np.array([[
        congestion_index, ave_height, b08301_002e, b08301_003e,
        b19013_001e, p1_001n, residential_pct, commercial_pct,
        to_fire, to_hospital
        # ... add all 50+ features
    ]])
    
    # Scale features
    input_scaled = models['classification_scaler'].transform(input_features)
    
    # Predict
    prediction = models['classification'].predict(input_scaled)[0]
    probabilities = models['classification'].predict_proba(input_scaled)[0]
    
    # Decode prediction
    los = models['classification_encoder'].inverse_transform([prediction])[0]
    confidence = probabilities.max()

# ========== REGRESSION ==========
if models and 'regression' in models:
    # Prepare input
    input_data = pd.DataFrame({
        'holiday': [holiday],
        'temp': [temp],
        'rain_1h': [rain_1h],
        'snow_1h': [snow_1h],
        'clouds_all': [clouds_all],
        'weather_main': [weather_main],
        'hour': [hour_reg],
        'day_of_week': [day_of_week]
        # ... add other features
    })
    
    # Preprocess (encoding, scaling, etc.)
    input_processed = models['regression_preprocessor'].transform(input_data)
    
    # Predict
    predicted_volume = models['regression'].predict(input_processed)[0]
    predicted_volume = int(max(0, predicted_volume))  # Ensure non-negative
""")

# ============================================================================
# STEP 4: Feature preparation templates
# ============================================================================

print("\n🔧 STEP 4: Feature Preparation Tips")
print("-" * 60)
print("""
Make sure your feature preparation matches your training process:

1. CATEGORICAL ENCODING:
   - Use the same encoder you used during training
   - Keep the same column order
   
2. SCALING:
   - Apply the same scaler (StandardScaler, MinMaxScaler, etc.)
   - Scale only the features you scaled during training
   
3. FEATURE ORDER:
   - Ensure features are in the exact same order as training
   - Check feature names if using DataFrames
   
4. MISSING VALUES:
   - Handle the same way as during training
   - Use the same imputation strategy
""")

# ============================================================================
# STEP 5: Testing your integration
# ============================================================================

print("\n✅ STEP 5: Test Your Integration")
print("-" * 60)
print("""
Create a test script to verify everything works:

# test_integration.py
import joblib
import numpy as np
import pandas as pd

# Load model
model = joblib.load('models/clustering_model.pkl')

# Test prediction
test_input = np.array([[1, 14, 2, 0.5]])  # Example input
prediction = model.predict(test_input)
print(f"Test prediction: {prediction}")

# If it works here, it should work in the app!
""")

# ============================================================================
# Summary
# ============================================================================

print("\n" + "=" * 60)
print("📋 INTEGRATION CHECKLIST")
print("=" * 60)
print("""
✓ Train your models in Jupyter notebooks
✓ Save models using joblib.dump()
✓ Create 'models/' directory
✓ Update app.py with model loading code
✓ Replace simulated predictions with real predictions
✓ Match feature preprocessing exactly
✓ Test with sample inputs
✓ Handle errors gracefully (model not found, etc.)
✓ Add loading indicators with st.spinner()
✓ Display confidence scores when available
""")

print("\n🚀 Once completed, run: streamlit run app.py")
print("=" * 60)

# ============================================================================
# Create a template for model info
# ============================================================================

model_info_template = {
    'clustering': {
        'input_features': ['road_id', 'hour', 'day', 'delay'],
        'output': 'cluster_label (0-3)',
        'output_mapping': {0: 'FREE', 1: 'LIGHT', 2: 'MODERATE', 3: 'HEAVY'}
    },
    'classification': {
        'input_features': [
            'congestion_index', 'ave_height', 'b08301_002e', 'b08301_003e',
            'b19013_001e', 'p1_001n', 'residential_pct', 'commercial_pct',
            'to_fire', 'to_hospital'
            # Add all 50+ features
        ],
        'output': 'LOS category',
        'output_mapping': {0: 'Good', 1: 'Medium', 2: 'Poor'}
    },
    'regression': {
        'input_features': [
            'holiday', 'temp', 'rain_1h', 'snow_1h', 'clouds_all',
            'weather_main', 'weather_description', 'hour', 'day_of_week'
        ],
        'output': 'traffic_volume (continuous)'
    }
}

# Save model info as reference
import json
with open('models/model_info.json', 'w') as f:
    json.dump(model_info_template, f, indent=2)

print(f"\n✅ Created model_info.json in models/ directory")
print("   Use this as reference for feature names and order")
