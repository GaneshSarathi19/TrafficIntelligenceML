"""
Demo Examples for Traffic Analytics ML Platform

This file contains example inputs for testing each track.
Use these in the UI to see realistic predictions.
"""

# ============================================================================
# CLUSTERING EXAMPLES
# ============================================================================

clustering_examples = {
    "Morning Rush - Heavy Traffic": {
        "road_id": "R1",
        "hour": 8,
        "day": "Monday",
        "delay": 3.5,
        "expected": "HEAVY"
    },
    "Afternoon Light Traffic": {
        "road_id": "R2",
        "hour": 14,
        "day": "Wednesday",
        "delay": 0.5,
        "expected": "LIGHT"
    },
    "Evening Rush - Moderate": {
        "road_id": "R3",
        "hour": 17,
        "day": "Friday",
        "delay": 1.8,
        "expected": "MODERATE"
    },
    "Late Night - Free Flow": {
        "road_id": "R4",
        "hour": 23,
        "day": "Sunday",
        "delay": -0.5,
        "expected": "FREE"
    },
    "Weekend Morning - Free": {
        "road_id": "R1",
        "hour": 10,
        "day": "Saturday",
        "delay": 0.2,
        "expected": "FREE"
    }
}

# ============================================================================
# CLASSIFICATION EXAMPLES
# ============================================================================

classification_examples = {
    "Dense Urban Area - Poor LOS": {
        "congestion_index": 5,
        "ave_height": 8.5,
        "b08301_002e": 1200,
        "b08301_003e": 1000,
        "b19013_001e": 65000,
        "p1_001n": 3500,
        "residential_pct": 90,
        "commercial_pct": 5,
        "to_fire": 3.5,
        "to_hospital": 8.0,
        "expected": "Poor"
    },
    "Suburban Area - Good LOS": {
        "congestion_index": 1,
        "ave_height": 3.2,
        "b08301_002e": 350,
        "b08301_003e": 300,
        "b19013_001e": 95000,
        "p1_001n": 800,
        "residential_pct": 85,
        "commercial_pct": 8,
        "to_fire": 1.5,
        "to_hospital": 4.0,
        "expected": "Good"
    },
    "Mixed Use Area - Medium LOS": {
        "congestion_index": 3,
        "ave_height": 5.0,
        "b08301_002e": 700,
        "b08301_003e": 550,
        "b19013_001e": 80000,
        "p1_001n": 1500,
        "residential_pct": 70,
        "commercial_pct": 20,
        "to_fire": 2.0,
        "to_hospital": 6.0,
        "expected": "Medium"
    },
    "High-Rise District - Poor LOS": {
        "congestion_index": 6,
        "ave_height": 15.0,
        "b08301_002e": 2000,
        "b08301_003e": 1800,
        "b19013_001e": 55000,
        "p1_001n": 5000,
        "residential_pct": 95,
        "commercial_pct": 3,
        "to_fire": 4.5,
        "to_hospital": 10.0,
        "expected": "Poor"
    },
    "Low Density Area - Good LOS": {
        "congestion_index": 0,
        "ave_height": 2.5,
        "b08301_002e": 200,
        "b08301_003e": 180,
        "b19013_001e": 110000,
        "p1_001n": 450,
        "residential_pct": 75,
        "commercial_pct": 5,
        "to_fire": 1.0,
        "to_hospital": 3.0,
        "expected": "Good"
    }
}

# ============================================================================
# REGRESSION EXAMPLES
# ============================================================================

regression_examples = {
    "Typical Weekday Morning Rush": {
        "temp": 285.0,  # 12°C
        "rain_1h": 0.0,
        "snow_1h": 0.0,
        "clouds_all": 40,
        "hour": 8,
        "day_of_week": "Monday",
        "holiday": False,
        "weather_main": "Clear",
        "expected_range": "5000-6000 vehicles"
    },
    "Rainy Evening Commute": {
        "temp": 282.0,  # 9°C
        "rain_1h": 8.5,
        "snow_1h": 0.0,
        "clouds_all": 90,
        "hour": 17,
        "day_of_week": "Thursday",
        "holiday": False,
        "weather_main": "Rain",
        "expected_range": "3500-4500 vehicles"
    },
    "Snowy Winter Morning": {
        "temp": 270.0,  # -3°C
        "rain_1h": 0.0,
        "snow_1h": 2.5,
        "clouds_all": 100,
        "hour": 7,
        "day_of_week": "Tuesday",
        "holiday": False,
        "weather_main": "Snow",
        "expected_range": "2000-3000 vehicles"
    },
    "Weekend Afternoon - Clear": {
        "temp": 295.0,  # 22°C
        "rain_1h": 0.0,
        "snow_1h": 0.0,
        "clouds_all": 20,
        "hour": 14,
        "day_of_week": "Saturday",
        "holiday": False,
        "weather_main": "Clear",
        "expected_range": "3000-4000 vehicles"
    },
    "Holiday Evening - Low Traffic": {
        "temp": 288.0,  # 15°C
        "rain_1h": 0.0,
        "snow_1h": 0.0,
        "clouds_all": 50,
        "hour": 18,
        "day_of_week": "Thursday",
        "holiday": True,
        "weather_main": "Clouds",
        "expected_range": "2000-2500 vehicles"
    },
    "Late Night - Minimal Traffic": {
        "temp": 278.0,  # 5°C
        "rain_1h": 0.0,
        "snow_1h": 0.0,
        "clouds_all": 30,
        "hour": 2,
        "day_of_week": "Wednesday",
        "holiday": False,
        "weather_main": "Clear",
        "expected_range": "500-1000 vehicles"
    },
    "Midday Clear Weather": {
        "temp": 292.0,  # 19°C
        "rain_1h": 0.0,
        "snow_1h": 0.0,
        "clouds_all": 15,
        "hour": 12,
        "day_of_week": "Tuesday",
        "holiday": False,
        "weather_main": "Clear",
        "expected_range": "3500-4000 vehicles"
    },
    "Thunderstorm Rush Hour": {
        "temp": 286.0,  # 13°C
        "rain_1h": 25.0,
        "snow_1h": 0.0,
        "clouds_all": 100,
        "hour": 17,
        "day_of_week": "Friday",
        "holiday": False,
        "weather_main": "Thunderstorm",
        "expected_range": "2500-3500 vehicles"
    }
}

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def print_examples():
    """Print all examples in a readable format"""
    
    print("=" * 80)
    print("TRAFFIC ANALYTICS ML PLATFORM - DEMO EXAMPLES")
    print("=" * 80)
    
    # Clustering
    print("\n📊 CLUSTERING EXAMPLES")
    print("-" * 80)
    for name, data in clustering_examples.items():
        print(f"\n{name}:")
        print(f"  Road: {data['road_id']}")
        print(f"  Time: {data['hour']}:00 on {data['day']}")
        print(f"  Delay: {data['delay']} minutes")
        print(f"  Expected: {data['expected']}")
    
    # Classification
    print("\n\n🎯 CLASSIFICATION EXAMPLES")
    print("-" * 80)
    for name, data in classification_examples.items():
        print(f"\n{name}:")
        print(f"  Congestion Index: {data['congestion_index']}")
        print(f"  Average Height: {data['ave_height']}m")
        print(f"  Workers: {data['b08301_002e']}")
        print(f"  Median Income: ${data['b19013_001e']:,}")
        print(f"  Expected LOS: {data['expected']}")
    
    # Regression
    print("\n\n📈 REGRESSION EXAMPLES")
    print("-" * 80)
    for name, data in regression_examples.items():
        temp_c = data['temp'] - 273.15
        print(f"\n{name}:")
        print(f"  Temperature: {data['temp']}K ({temp_c:.1f}°C)")
        print(f"  Rain: {data['rain_1h']}mm, Snow: {data['snow_1h']}mm")
        print(f"  Time: {data['hour']}:00 on {data['day_of_week']}")
        print(f"  Weather: {data['weather_main']}")
        print(f"  Holiday: {'Yes' if data['holiday'] else 'No'}")
        print(f"  Expected Volume: {data['expected_range']}")
    
    print("\n" + "=" * 80)
    print("Copy these values into the UI to test predictions!")
    print("=" * 80)

def get_example(track, scenario_name):
    """
    Get a specific example by track and scenario name
    
    Args:
        track: 'clustering', 'classification', or 'regression'
        scenario_name: Name of the scenario
    
    Returns:
        dict: Example data or None if not found
    """
    examples = {
        'clustering': clustering_examples,
        'classification': classification_examples,
        'regression': regression_examples
    }
    
    return examples.get(track, {}).get(scenario_name)

def get_random_example(track):
    """Get a random example for testing"""
    import random
    
    examples = {
        'clustering': clustering_examples,
        'classification': classification_examples,
        'regression': regression_examples
    }
    
    track_examples = examples.get(track, {})
    if track_examples:
        scenario = random.choice(list(track_examples.keys()))
        return scenario, track_examples[scenario]
    return None, None

# ============================================================================
# TEMPERATURE CONVERSION HELPER
# ============================================================================

def kelvin_to_celsius(kelvin):
    """Convert Kelvin to Celsius"""
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    """Convert Kelvin to Fahrenheit"""
    return (kelvin - 273.15) * 9/5 + 32

def celsius_to_kelvin(celsius):
    """Convert Celsius to Kelvin"""
    return celsius + 273.15

# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    print_examples()
    
    print("\n" + "=" * 80)
    print("TEMPERATURE CONVERSION REFERENCE")
    print("=" * 80)
    
    temps = [260, 270, 273, 280, 285, 290, 295, 300, 310]
    for k in temps:
        c = kelvin_to_celsius(k)
        f = kelvin_to_fahrenheit(k)
        print(f"{k}K = {c:.1f}°C = {f:.1f}°F")
    
    print("\n" + "=" * 80)
    print("\nTo use a specific example in Python:")
    print("  from demo_examples import get_example")
    print("  data = get_example('clustering', 'Morning Rush - Heavy Traffic')")
    print("\nTo get a random example:")
    print("  from demo_examples import get_random_example")
    print("  name, data = get_random_example('regression')")
    print("=" * 80)
