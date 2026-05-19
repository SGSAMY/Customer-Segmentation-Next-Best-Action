#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pandas as pd

# Read Excel file
df = pd.read_excel(
    r"C:\& Satheesh\Outbound-Calling-Conversion-Model\data\Customer_Segmentation_Next_Best_Action.xlsx"
)

# Display first 5 rows
df.head()


# In[57]:


print(df.columns)


# In[43]:


# ---------------------------------------------------------
# Customer Segmentation & Next Best Action Model
# Includes Fresco-style segmentation scoring
# ---------------------------------------------------------


def calculate_conversion_score(row):
    score = 0

    # 1. Fresco segment scoring
    if row["fresco_segment"] == "Affluent Families":
        score += 25
    elif row["fresco_segment"] == "Mature Wealth":
        score += 20
    elif row["fresco_segment"] == "Retired Comfort":
        score += 18
    elif row["fresco_segment"] == "Digital Achievers":
        score += 15
    elif row["fresco_segment"] == "Budget Households":
        score += 5

    # 2. Maturity date scoring
    if row["days_to_maturity"] <= 30:
        score += 30
    elif row["days_to_maturity"] <= 90:
        score += 20
    elif row["days_to_maturity"] <= 180:
        score += 10

    # 3. Account value scoring
    if row["account_value"] >= 15000:
        score += 30
    elif row["account_value"] >= 10000:
        score += 25
    elif row["account_value"] >= 5000:
        score += 15

    # 4. Direct Debit scoring
    if row["active_dd"] == "Yes":
        score += 20

    if row["failed_dd"] == "Yes":
        score -= 15

    # 5. Online engagement
    if row["online_login_days"] <= 30:
        score += 15
    elif row["online_login_days"] <= 90:
        score += 10

    # 6. Complaints
    if row["complaints"] == 0:
        score += 10
    elif row["complaints"] >= 2:
        score -= 20

    # 7. Previous campaign response
    if row["previous_campaign_response"] == "Yes":
        score += 20

    # 8. Email engagement
    if row["email_open_rate"] >= 60:
        score += 15
    elif row["email_open_rate"] >= 30:
        score += 10

    # 9. Web engagement
    if row["web_visits_30d"] >= 5:
        score += 15
    elif row["web_visits_30d"] >= 2:
        score += 10

    # 10. Adviser relationship
    if row["has_adviser"] == "Yes":
        score += 10

    return score


def assign_priority(score):
    if score >= 90:
        return "Very High Priority"
    elif score >= 70:
        return "High Priority"
    elif score >= 40:
        return "Medium Priority"
    else:
        return "Low Priority"


def recommend_next_best_action(row):
    if row["priority"] in ["Very High Priority", "High Priority"]:

        if row["product_type"] == "ISA":
            return "ISA reinvestment call"

        elif row["product_type"] == "JISA":
            return "JISA maturity follow-up"

        elif row["product_type"] == "CTF":
            return "CTF to ISA conversion call"

        elif row["product_type"] == "Over 50":
            return "Over 50 retention call"

    elif row["priority"] == "Medium Priority":
        return "Send targeted email campaign"

    else:
        return "Low priority nurture campaign"


# ---------------------------------------------------------
# Main process
# ---------------------------------------------------------

input_path = r"C:\& Satheesh\Customer Segmentation & Next Best Action\data\Customer_Segmentation_Next_Best_Action.xlsx"

output_path = r"C:\& Satheesh\Customer Segmentation & Next Best Action\output\customer_segmentation_output.xlsx"


# Read Excel file
df = pd.read_excel(input_path)

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Apply scoring model
df["conversion_score"] = df.apply(calculate_conversion_score, axis=1)

# Assign priority
df["priority"] = df["conversion_score"].apply(assign_priority)

# Recommend next best action
df["next_best_action"] = df.apply(recommend_next_best_action, axis=1)

# Sort highest priority customers first
df = df.sort_values(by="conversion_score", ascending=False)

# Export output file
df.to_excel(output_path, index=False)

print("Customer segmentation model completed successfully.")
print(f"Output file created: {output_path}")

print("\nTop 10 customers:")
print(
    df[
        [
            "customer_id",
            "customer_name",
            "product_type",
            "fresco_segment",
            "conversion_score",
            "priority",
            "next_best_action",
        ]
    ].head(10)
)


# In[41]:


df.head(10)


# In[51]:


import matplotlib.pyplot as plt

df["priority"].value_counts().plot(kind="bar")

plt.title("Customer Priority Distribution")
plt.xlabel("Priority")
plt.ylabel("Customer Count")

plt.show()


# In[53]:


df["product_type"].value_counts().plot(kind="pie", autopct='%1.1f%%')

plt.title("Product Distribution")

plt.show()


# In[55]:


top_customers = df.sort_values(
    by="conversion_score",
    ascending=False
).head(10)

print(top_customers[
    [
        "customer_name",
        "product_type",
        "conversion_score",
        "priority",
        "next_best_action"
    ]
])


# In[ ]:




