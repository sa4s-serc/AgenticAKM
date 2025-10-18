---
### ADR-002: Favor classical ML approaches (Linear Regression and SVM) over deep learning

Status: Inferred
Context: Presence of linear_reg_train.py and svm_train.py indicates reliance on classical machine learning models instead of deep neural networks for the video reconstruction problem.
Decision: Use classical ML models (e.g., linear regression and SVM) as primary learning techniques for reconstruction tasks.
Consequences:
- Positive: Lower computational requirements, faster training, easier interpretability, and simpler hyperparameter spaces.
- Negative: Potentially lower accuracy than modern deep learning methods on complex visual tasks; may limit ceiling performance without feature engineering.