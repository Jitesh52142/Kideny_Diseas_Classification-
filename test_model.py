#!/usr/bin/env python3
"""
Test script to verify model loading and basic functionality
"""

import os
import sys

def test_model_exists():
    """Test if model file exists"""
    model_path = "model/model.h5"
    if os.path.exists(model_path):
        print(f"✅ Model found at: {model_path}")
        return True
    else:
        print(f"❌ Model not found at: {model_path}")
        return False

def test_imports():
    """Test if required modules can be imported"""
    try:
        import tensorflow as tf
        print(f"✅ TensorFlow version: {tf.__version__}")
    except ImportError as e:
        print(f"❌ TensorFlow import failed: {e}")
        return False
    
    try:
        from CNNClassifier.pipeline.prediction import PredictionPipeline
        print("✅ PredictionPipeline import successful")
    except ImportError as e:
        print(f"❌ PredictionPipeline import failed: {e}")
        return False
    
    return True

def test_model_loading():
    """Test if model can be loaded"""
    try:
        from CNNClassifier.pipeline.prediction import PredictionPipeline
        classifier = PredictionPipeline("test.jpg")
        print("✅ Model loading successful")
        return True
    except Exception as e:
        print(f"❌ Model loading failed: {e}")
        return False

if __name__ == "__main__":
    print("🧪 Testing Kidney Disease Classification App")
    print("=" * 50)
    
    # Test model file existence
    model_exists = test_model_exists()
    
    # Test imports
    imports_ok = test_imports()
    
    # Test model loading (only if imports work)
    model_loading_ok = False
    if imports_ok and model_exists:
        model_loading_ok = test_model_loading()
    
    print("=" * 50)
    if model_exists and imports_ok and model_loading_ok:
        print("🎉 All tests passed! App is ready for deployment.")
    else:
        print("⚠️  Some tests failed. Check the issues above.")
        sys.exit(1)
