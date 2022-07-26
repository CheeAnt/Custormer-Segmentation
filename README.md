# Custormer Segmentation - Accuracy, F1, Recall, Precision, Which to Optimize On?

###### The classical trade-off of an imbalanced dataset, and why the model with the highest accuracy doesn't always make the best model. 


# The Problem
A bank experienced decline in revenues and decided to conduct marketing campaigns to persuade more clients to deposit money into the bank.

They decided to build a deep learning model that predicts the campaign outcome. This will help the marketing team to identify a high potential customer pool, empowering them to perform precise marketing to the target group. At the same time, reducing the advertisement spent on customers that have a low chance of signing up.


# The Output
![image](https://user-images.githubusercontent.com/29735171/181032729-45f45d8a-21cf-4815-8160-e62a52be8f0d.png)


Either a custormer **subscribe** a term deposit (+ve), or **not** (-ve).

That gives us 4 classes of output, with different weightage to the marketing team.

- True Positive (**TP**): Customer subscribe and the prediction is +ve, the highest value class for this campaign :heart_eyes:
- True Negative (**TN**): Customer do not subscribe and the prediction is -ve, filtering them helps to maximise our marketing budget :sunglasses:
- False Positive (**FP**): Customer do not subscribe but the prediction is +ve, wasting some of the bank's resources here :grimacing:
- False Negative (**FN**): Customer subscribe but the prediction is -ve, ***BAD*** , bank losing revenue and we're losing our job here :scream:



# Model Building - Without Oversampling the Data
![image](https://user-images.githubusercontent.com/29735171/181026721-a676e5c2-5856-490a-8061-be2b10ca92d5.png)

**Accuracy at 0.91**, a very good model, right?

Not really, says the marketing manager.



# Recall -  When the TP class is way more important than the others

If we study the recall of the **TP**, which is at 0.37.
It means that, of 1000 customers that actually signs up, our model will mark 630 of them as negative! 

This model now seems ridiculous for the campaign. 

# SMOTE - Oversampling Imbalanced Datasets


![image](https://user-images.githubusercontent.com/29735171/181029001-8fe0db40-d58a-421a-970d-c613ca3b7882.png)
![image](https://user-images.githubusercontent.com/29735171/181032095-edeb0fe0-e589-4973-a625-3e1e5d05c9b5.png)

After resampling, our accuracy dropped to merely 0.84.

But hey! The sensitivity of TP now became 0.91!

That means, of 1000 customers that would subscribe, our model is managed to catch 910 of them!

The marketing team is very happy about the model, they can now confidently use our model to segment a customer pool for their sales funnel. 


# Credits:
###### Datasource: [Kaggle](https://www.kaggle.com/datasets/kunalgupta2616/hackerearth-customer-segmentation-hackathon)

