# Custormer Segmentation - Accuracy, F1, Recall, Which Metric to Optimize?

##### The classical trade-off of an imbalanced dataset, and why the model with the highest accuracy doesn't always make the best model. 

## Problem Statement 🏦
Our bank has been facing declining revenues lately. To combat this, they've initiated marketing campaigns to encourage more deposits. 

They opted to develop a deep-learning model to forecast the campaign's results. 
This enables the marketing team to pinpoint a customer segment with high potential, allowing for targeted marketing efforts. 
Simultaneously, it minimizes ad spending on customers who are less likely to subscribe.

## Dataset Given
![image](https://user-images.githubusercontent.com/29735171/181032729-45f45d8a-21cf-4815-8160-e62a52be8f0d.png)

## Initial Model (No Oversampling)
![Initial Model](https://user-images.githubusercontent.com/29735171/181026721-a676e5c2-5856-490a-8061-be2b10ca92d5.png)

**Accuracy at 0.91**, sounds like a fantastic model, right?

Well, not so fast! The marketing manager has some concerns.

## Model Evaluation
When customers see our campaign, they either **subscribe** to a term deposit or **don't**. 
This gives us four possible outcomes, with different weightage to the marketing team:

| Class | Description |
| ---   | ---      |
| True Positive (**TP**)| Customers subscribed, just as we predicted! :heart_eyes: |
| True Negative (**TN**)| Customers didn't subscribe, and we accurately anticipated it. This foresight optimizes our marketing budget :sunglasses: |
| False Positive (**FP**)| Oops! We expected these customers to subscribe, but they didn't. This misjudgment costs the bank :grimacing: |
| False Negative (**FN**)| Oh no! These customers subscribed, but we missed it. ***BAD***, Bank losing revenue and we're losing our job here :scream: |


## Recall - When the TP Class is Super Important 

Looking at the recall of the **TP**, it's only 0.37. 
This means that out of 1000 customers who sign up, our model mistakenly labels 630 of them as not interested! 😱

Suddenly, this model doesn't seem so great for our campaign.


# SMOTE - Oversampling Imbalanced Datasets

![image](https://user-images.githubusercontent.com/29735171/181029001-8fe0db40-d58a-421a-970d-c613ca3b7882.png)
![image](https://user-images.githubusercontent.com/29735171/181032095-edeb0fe0-e589-4973-a625-3e1e5d05c9b5.png)

After using SMOTE to resample our data, our accuracy took a hit, dropping to 0.84. 
But here's the silver lining: the recall for TP shot up to 0.91! 🥳

This means that out of 1000 customers who would subscribe, our model now catches 910 of them. 
The marketing team is ecstatic! They can now confidently use our model to segment customers and supercharge their sales funnel.



# Credits:
###### Datasource: [Kaggle](https://www.kaggle.com/datasets/kunalgupta2616/hackerearth-customer-segmentation-hackathon)

