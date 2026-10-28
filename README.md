# 💵 Bank Authentication System

A Machine Learning-based web application that predicts whether a banknote is **genuine or fake** based on its statistical features.

The project uses a **Random Forest Classifier** for prediction and **Streamlit** to provide an interactive web interface.

---

## 📌 Project Overview

Counterfeit banknotes are a major concern for financial institutions and businesses.

This project uses Machine Learning to analyze numerical characteristics extracted from banknote images and classify the banknote as genuine or counterfeit.

The system takes four input features:

- Variance
- Skewness
- Curtosis
- Entropy

and provides a predicted authentication result.

---

## 🎯 Objective

The main objective of this project is to build a Machine Learning classification system that can:

- Analyze banknote characteristics
- Identify patterns associated with genuine and counterfeit notes
- Predict the authenticity of a banknote
- Provide predictions through an easy-to-use web application

---

## 🧠 Machine Learning Approach

The project uses:

**Algorithm:** Random Forest Classifier

### Workflow

Banknote Dataset
       ↓
Data Loading
       ↓
Data Preprocessing
       ↓
Train-Test Split
       ↓
Random Forest Classifier
       ↓
Model Evaluation
       ↓
Model Serialization
       ↓
Streamlit Application
       ↓
Banknote Prediction
