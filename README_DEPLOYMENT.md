# Kidney Disease Classification - Vercel Deployment Guide

## Overview
This is a Flask-based web application for kidney disease classification using CNN (Convolutional Neural Network). The app classifies kidney CT scan images as either "Normal" or "Tumor".

## Application Structure
- **Flask Web App** (`app.py`) - Main application with prediction endpoint
- **ML Pipeline** - Complete MLOps pipeline with data ingestion, model training, and evaluation
- **CNN Model** - Trained model for kidney disease classification
- **Web Interface** - HTML template for image upload and prediction display

## Key Features
- Image upload via web interface
- Base64 image processing
- CNN model prediction
- Real-time classification results
- Responsive web design

## Deployment Files Created
1. `vercel.json` - Vercel configuration
2. `wsgi.py` - WSGI entry point
3. `requirements_vercel.txt` - Optimized requirements for Vercel
4. `.vercelignore` - Files to exclude from deployment

## Model Files
- Main model: `model/model.h5`
- Backup model: `artifacts/training/model.h5`

## API Endpoints
- `GET /` - Home page with upload interface
- `POST /predict` - Image classification endpoint
- `GET/POST /train` - Model training endpoint (for development)

## Deployment Steps

### 1. Prerequisites
- Vercel account
- Git repository with the code
- Model files in correct locations

### 2. Vercel Deployment
1. Connect your GitHub repository to Vercel
2. Vercel will automatically detect the Python app
3. The `vercel.json` configuration will handle the deployment
4. Model files will be included in the deployment

### 3. Environment Variables
No special environment variables required for basic deployment.

### 4. File Structure for Deployment
```
├── app.py                 # Main Flask application
├── wsgi.py               # WSGI entry point
├── vercel.json           # Vercel configuration
├── requirements_vercel.txt # Dependencies
├── .vercelignore         # Files to exclude
├── model/
│   └── model.h5         # Trained model
├── templates/
│   └── index.html       # Web interface
└── src/                  # Source code
    └── CNNClassifier/    # ML pipeline code
```

## Testing Locally
1. Install dependencies: `pip install -r requirements_vercel.txt`
2. Run the app: `python app.py`
3. Open browser to `http://localhost:8080`

## Usage
1. Upload a kidney CT scan image
2. Click "Predict" to get classification
3. Results will show "Normal" or "Tumor"

## Troubleshooting
- Ensure model files are in correct locations
- Check that all dependencies are installed
- Verify image format is supported (JPEG, PNG)
- Check logs for any TensorFlow loading issues

## Model Information
- Input size: 224x224 pixels
- Classes: Normal, Tumor
- Framework: TensorFlow/Keras
- Architecture: CNN (Convolutional Neural Network)
