# Phishing Website Detection using Machine Learning

## Overview
This project focuses on detecting phishing websites using machine learning techniques applied to URL and webpage-based features. The goal is to build a **security-aware model** that minimizes missed phishing attempts, which are more critical than false alarms in real-world cybersecurity scenarios.

The project is being developed incrementally, following a **structured learning plan toward AI Engineering**.

---

## Dataset

**Source:** Kaggle – Web Page Phishing Dataset  

**Description:**  
The dataset contains extracted URL and webpage-based features commonly used for phishing detection.

**Target Variable:**
- `phishing = 1` → Phishing website  
- `phishing = 0` → Legitimate website  

---

## Models Implemented

### Day 1 – Baseline Model
- **Model:** Decision Tree Classifier  
- **Accuracy:** ~88.3%  
- **Purpose:** Establish a baseline for phishing detection  

---

### Day 2 – Model Comparison & Evaluation
To improve performance, a **Random Forest model with class-weight balancing** was trained and compared with the baseline Decision Tree.

#### Models Compared
- Decision Tree Classifier  
- Random Forest Classifier (`class_weight='balanced'`)  (**Accuracy**: 88.9%)

#### Evaluation Approach
Rather than relying only on accuracy, **confusion matrices** were analyzed to prioritize reducing **false negatives**, since missed phishing websites pose higher security risks.

#### Confusion Matrix Summary
- **Decision Tree**
  - False Negatives: **1393**
- **Random Forest (Balanced)**
  - False Negatives: **890**

#### Key Insight
The Random Forest model had better accuracy among the two models and the **Random Forest model significantly reduced false negatives**. This makes it more suitable for real-world cybersecurity applications where **recall for malicious activity is critical**.

✅ **Final Model Selected:** Random Forest Classifier (Balanced)

---

## Tools & Technologies
- Python  
- pandas  
- scikit-learn  
- Jupyter Notebook / Kaggle Notebook  

---
