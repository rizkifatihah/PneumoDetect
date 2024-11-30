# PneumoDetect: Chest X-Ray Pneumonia Detection System

A deep learning-based web application for automated detection of pneumonia from chest X-ray images using YOLOv11 model.

## Project Overview

PneumoDetect is an AI-powered web application that helps medical professionals detect pneumonia from chest X-ray images. The system uses a deep learning model trained on a comprehensive dataset of pediatric chest X-rays to provide quick and accurate pneumonia detection.

## Dataset Information

This project uses the Chest X-Ray Images (Pneumonia) dataset:
- **Source**: Kermany, Daniel; Zhang, Kang; Goldbaum, Michael (2018), "Large Dataset of Labeled Optical Coherence Tomography (OCT) and Chest X-Ray Images", Mendeley Data
- **Dataset Link**: [Chest X-Ray Images (Pneumonia) on Kaggle](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia)

Dataset characteristics:
- 5,856 X-Ray images (JPEG)
- 2 categories: PNEUMONIA and NORMAL
- Dataset organization:
  - Train: 4,009 images
  - Test: 624 images
  - Val: 16 images
- Images sourced from pediatric patients at Guangzhou Women and Children's Medical Center

## System Requirements

- Python 3.8 or higher
- CUDA-capable GPU (recommended for faster inference)
- Windows/Linux/MacOS

## Project Structure
PneumoDetect/
<br>
├── app.py 
<br>
├── requirements.txt 
<br>
├── best.pt 
<br>
├── README.md 
<br>
└── static/ 
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── uploads/
<br>
└── templates/ 
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── index.html


## Installation Guide

### 1. Clone the Repository
git clone <repository-url>
cd PneumoDetect

### 2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Running the Application
python app.py
http://127.0.0.1:5000

