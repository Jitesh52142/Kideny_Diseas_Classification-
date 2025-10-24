# 🏥 Kidney Disease Classification System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.16+-orange.svg)
![Flask](https://img.shields.io/badge/Flask-2.3+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

**Advanced AI-powered medical imaging analysis for kidney disease detection and classification**

[![Deploy to Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/your-username/kidney-disease-classification)

</div>

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Deployment](#deployment)
- [Project Structure](#project-structure)
- [Medical Disclaimer](#medical-disclaimer)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

The **Kidney Disease Classification System** is a state-of-the-art AI-powered medical imaging application that uses Convolutional Neural Networks (CNN) to analyze kidney CT scan images and classify them as either "Normal" or "Tumor". This system is designed for healthcare professionals and medical institutions to assist in preliminary kidney disease assessment.

### 🎨 Professional Medical Interface

The application features a **medical-grade user interface** with:
- Professional healthcare design
- Comprehensive medical terminology
- Detailed analysis reports
- HIPAA-compliant security features
- Responsive design for all devices

## ✨ Features

### 🤖 AI-Powered Analysis
- **CNN Deep Learning**: Advanced Convolutional Neural Network for image classification
- **High Accuracy**: State-of-the-art deep learning models for medical imaging
- **Real-time Processing**: Fast analysis with immediate results
- **Medical Grade**: Clinical-grade analysis capabilities

### 🏥 Professional Medical Interface
- **Medical-Grade UI**: Professional healthcare design
- **Comprehensive Reports**: Detailed medical analysis reports
- **Clinical Terminology**: Proper medical language throughout
- **Responsive Design**: Works on desktop, tablet, and mobile
- **Accessibility**: High contrast and readable fonts

### 🔒 Security & Compliance
- **HIPAA Compliant**: Medical data protection standards
- **Secure Processing**: No permanent image storage
- **Privacy Focused**: Patient data protection
- **Medical Disclaimers**: Proper legal and safety information

### 📊 Advanced Results Display
- **Clinical Assessment**: Professional medical evaluation
- **Morphological Analysis**: Technical structural analysis
- **Medical Recommendations**: Appropriate next steps
- **Confidence Scores**: AI confidence percentages
- **Technical Parameters**: Model specifications and processing details

## 🛠 Technology Stack

### Backend
- **Python 3.8+**: Core programming language
- **Flask 2.3+**: Web framework
- **TensorFlow 2.16+**: Deep learning framework
- **Keras**: High-level neural network API
- **NumPy**: Numerical computing
- **Pandas**: Data manipulation

### Frontend
- **HTML5**: Modern markup
- **CSS3**: Advanced styling with CSS Grid and Flexbox
- **JavaScript**: Interactive functionality
- **Bootstrap 4**: Responsive framework
- **Font Awesome**: Professional icons

### AI/ML
- **CNN Architecture**: Convolutional Neural Networks
- **Image Processing**: 224x224 pixel input resolution
- **Binary Classification**: Normal vs Tumor detection
- **Deep Learning**: State-of-the-art medical imaging AI

### Deployment
- **Vercel**: Cloud deployment platform
- **Docker**: Containerization support
- **WSGI**: Production server interface
- **REST API**: Standardized API endpoints

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git

### Local Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/kidney-disease-classification.git
   cd kidney-disease-classification
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements_vercel.txt
   pip install -e .
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the application**
   - Open your browser and go to `http://localhost:8080`
   - Upload a kidney CT scan image
   - Get AI-powered analysis results

### Docker Setup

1. **Build the Docker image**
   ```bash
   docker build -t kidney-disease-classification .
   ```

2. **Run the container**
   ```bash
   docker run -p 8080:8080 kidney-disease-classification
   ```

## 📖 Usage

### Web Interface

1. **Upload Image**
   - Click "Select Medical Image" button
   - Choose a kidney CT scan image (JPG, PNG, DICOM, TIFF)
   - Ensure image shows clear kidney structures

2. **AI Analysis**
   - Click "Start AI Analysis" button
   - Wait for AI processing (typically 1-3 seconds)
   - View comprehensive medical report

3. **Results Interpretation**
   - Review clinical assessment
   - Check morphological analysis
   - Follow medical recommendations
   - Consult healthcare professionals for final diagnosis

### API Usage

#### Predict Endpoint
```bash
curl -X POST http://localhost:8080/predict \
  -H "Content-Type: application/json" \
  -d '{"image": "base64_encoded_image_data"}'
```

**Response:**
```json
[
  {
    "image": "Normal"
  }
]
```

## 📚 API Documentation

### Endpoints

#### `GET /`
- **Description**: Home page with medical image upload interface
- **Response**: HTML page with professional medical UI

#### `POST /predict`
- **Description**: AI-powered kidney disease classification
- **Request Body**: 
  ```json
  {
    "image": "base64_encoded_image_data"
  }
  ```
- **Response**: 
  ```json
  [
    {
      "image": "Normal" | "Tumor"
    }
  ]
  ```

#### `GET/POST /train`
- **Description**: Model training endpoint (development use)
- **Response**: Training status message

### Error Handling

The API includes comprehensive error handling:
- **400 Bad Request**: Invalid image data
- **500 Internal Server Error**: Model loading or processing errors
- **CORS Support**: Cross-origin requests enabled

## 🌐 Deployment

### Vercel Deployment (Recommended)

1. **Connect to Vercel**
   - Push code to GitHub repository
   - Connect repository to Vercel
   - Vercel will auto-detect Python configuration

2. **Automatic Deployment**
   - Vercel uses `vercel.json` configuration
   - Dependencies installed from `requirements_vercel.txt`
   - Model files included in deployment

3. **Environment Variables**
   - No special environment variables required
   - All configuration handled automatically

### Manual Deployment

1. **Install Vercel CLI**
   ```bash
   npm i -g vercel
   ```

2. **Deploy**
   ```bash
   vercel
   ```

3. **Follow prompts** to configure project

## 📁 Project Structure

```
kidney-disease-classification/
├── app.py                          # Main Flask application
├── wsgi.py                         # WSGI entry point for Vercel
├── vercel.json                     # Vercel deployment configuration
├── requirements_vercel.txt         # Production dependencies
├── .vercelignore                   # Files to exclude from deployment
├── Dockerfile                      # Docker configuration
├── README.md                       # This file
├── model/
│   └── model.h5                    # Trained CNN model
├── templates/
│   └── index.html                  # Professional medical UI
├── src/
│   └── CNNClassifier/              # ML pipeline source code
│       ├── components/             # ML components
│       ├── config/                 # Configuration management
│       ├── entity/                 # Data entities
│       ├── pipeline/               # ML pipelines
│       └── utils/                  # Utility functions
├── artifacts/                      # ML artifacts and data
├── config/                         # Configuration files
└── research/                       # Jupyter notebooks for research
```

## 🏥 Medical Disclaimer

### Important Medical Information

**⚠️ CRITICAL DISCLAIMER**: This AI-powered analysis tool is designed to assist healthcare professionals in preliminary assessment. It should **NOT** replace professional medical diagnosis, consultation, or treatment.

### Key Points:
- **For Healthcare Professionals**: Designed to assist in preliminary assessment
- **Not a Replacement**: Cannot replace professional medical diagnosis
- **Consultation Required**: Always consult qualified medical professionals
- **Clinical Correlation**: Results should be interpreted with clinical findings
- **Patient Safety**: Patient safety is the top priority

### Privacy & Security:
- **HIPAA Compliant**: Medical data protection standards
- **No Permanent Storage**: Images processed securely and not stored
- **Privacy Focused**: Patient data protection prioritized
- **Secure Processing**: All data handled with medical-grade security

## 🤝 Contributing

We welcome contributions to improve the Kidney Disease Classification System!

### How to Contribute:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Commit changes**: `git commit -m 'Add amazing feature'`
4. **Push to branch**: `git push origin feature/amazing-feature`
5. **Open a Pull Request**

### Development Guidelines:
- Follow PEP 8 Python style guide
- Write comprehensive tests
- Update documentation
- Ensure medical accuracy
- Maintain HIPAA compliance

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Medical Community**: For guidance on clinical requirements
- **AI/ML Community**: For open-source deep learning frameworks
- **Healthcare Professionals**: For domain expertise and validation
- **Open Source Contributors**: For the amazing tools and libraries

## 📞 Support

For support, questions, or medical inquiries:

- **Technical Issues**: Create an issue on GitHub
- **Medical Questions**: Consult qualified healthcare professionals
- **Security Concerns**: Report security issues responsibly

---

<div align="center">

**🏥 Built with ❤️ for the Medical Community 🏥**

*Advanced AI for Better Healthcare*

</div>