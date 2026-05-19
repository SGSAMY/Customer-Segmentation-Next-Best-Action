# Customer Segmentation & Next Best Action Model

## Overview

This project demonstrates a Python-based customer segmentation and conversion propensity model using behavioural analytics and CACI Fresco-style demographic segmentation.

The solution prioritises customers for outbound marketing campaigns and recommends the most suitable next-best-action based on customer behaviour, engagement, financial value, and product maturity indicators.

---

## Business Problem

Financial services organisations require targeted customer engagement strategies to improve campaign conversion rates and prioritise high-value customers.

This project analyses:

* Fresco customer segments
* Product maturity timelines
* Account value
* Direct Debit behaviour
* Online engagement
* Complaint history
* Previous campaign responses
* Email and web activity

to identify customers with the highest conversion potential.

---

## Technologies Used

* Python
* pandas
* matplotlib
* Excel
* Jupyter Notebook

---

## Model Logic

The model uses rule-based scoring to calculate a conversion propensity score for each customer.

Customers are scored using the following factors:

Fresco segment: Higher scores are given to segments with stronger expected product suitability or affluence.
Maturity date: Customers closer to maturity receive higher priority.
Account value: Higher-value customers receive higher scores.
Direct Debit status: Active DD increases the score; failed DD reduces it.
Online engagement: Recent online login activity increases the score.
Complaints history: Customers with multiple complaints receive a lower score.
Previous campaign response: Customers who previously responded receive a higher score.
Email and web engagement: Higher email open rates and website visits increase the score.
Adviser relationship: Customers with an adviser receive an additional score.

The final score is converted into priority bands:

90+     Very High Priority
70–89   High Priority
40–69   Medium Priority
<40     Low Priority

The model then recommends a next-best-action based on the customer’s product type and priority level.

---

## Key Features

* Customer propensity scoring
* Fresco-style segmentation weighting
* Priority classification
* Next-best-action recommendation
* Campaign targeting logic
* Automated Excel output generation
* Visualisation and analytics

---

## Example Use Cases

* ISA maturity campaigns
* JISA conversion campaigns
* Retention targeting
* High-value customer prioritisation
* Outbound call centre optimisation
* Marketing segmentation

---

## Project Structure

```text
Customer-Segmentation-Next-Best-Action/
│
├── data/
├── notebooks/
├── output/
├── scripts/
└── README.md
```


## Author
Satheesh Gurusamy

GitHub:
https://github.com/SGSAMY
