# 📊 Customer Churn Prediction & Retention Strategy

## 🔎 Business Problem

Customer churn is one of the main revenue leakage drivers in retail businesses.  
Identifying high-risk customers before they leave enables proactive retention strategies and revenue protection.

This project develops a predictive churn model and a data-driven retention strategy using transactional retail data.

---

## 🎯 Objective

- Predict customer churn probability
- Identify high-value customers at risk
- Estimate revenue exposure
- Propose actionable retention strategies

---

## 📂 Dataset

**Online Retail II Dataset (2009–2010)**  
Contains transactional data including:

- Customer ID
- Invoice Date
- Quantity
- Price
- Transaction value

---

## 🧹 Data Preparation

- Removed null Customer IDs
- Filtered returns and negative quantities
- Created `TotalPrice`
- Built RFM features:
  - **Recency**
  - **Frequency**
  - **Monetary**

Churn defined as:
> Customers inactive for more than 90 days.

---

## 🤖 Modeling Approach

Model used:
- Random Forest Classifier

Steps:
- Feature scaling
- Train/test split (80/20)
- Probability-based churn scoring

Evaluation metrics:
- ROC-AUC
- Precision
- Recall
- Confusion Matrix

---

## 📈 Key Insights

- Recency is the strongest churn predictor.
- High-monetary customers with increasing recency represent major financial risk.
- Churn probability enables segmentation and prioritization.

---

## 💰 Revenue Risk Estimation

High-risk customers (probability > 0.8) represent a significant portion of total revenue.

Proactive retention strategies could substantially reduce revenue loss.

---

## 🎯 Strategic Retention Layer

Customers classified into 3 action groups:

| Segment | Action |
|----------|--------|
| High Risk + High Value | Immediate personalized retention |
| Medium Risk | Automated re-engagement |
| Low Risk | Monitoring & nurturing |

This transforms predictive modeling into business strategy.

---

## 📊 Visualizations

- Monthly revenue trend
- Churn rate evolution
- ROC Curve
- Feature importance
- Risk distribution
- Strategic action breakdown
- Customer risk map (Recency vs Monetary)
- Cohort retention heatmap

---

## 🚀 Next Steps

- Deploy model via API
- Integrate with CRM
- Automate retention triggers
- Build real-time monitoring dashboard

---

## 🛠 Tech Stack

- Python
- Pandas
- Scikit-learn
- Matplotlib / Seaborn
- Jupyter / Google Colab

---

## 📌 Conclusion

This project demonstrates how machine learning can move beyond prediction and directly support revenue-protection strategies through actionable insights.

The combination of predictive modeling and business interpretation enables data-driven decision making.
