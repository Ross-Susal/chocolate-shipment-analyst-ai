import pandas as pd

df = pd.read_csv("data/sample-chocolate-shipments-data-all-Apr-2025.csv")

# Inspecting the data
print(df.head())
print(df.shape)
print(df.info())
print(df.columns)

# Checking the empty fields in each column
print(df.isna().sum())

# Deleted the empty rows
df.drop(columns=["Unnamed: 20","Unnamed: 21","Unnamed: 22"],inplace=True)

# Converting the data type to datetime
df["Shipdate"] = pd.to_datetime(df["Shipdate"], format="mixed")
print(df["Shipdate"].head(10))
print(df["Shipdate"].dtype)

#Checking number of duplicated rows
duplicated_count = df.duplicated().sum()
print(duplicated_count)

#Chceking for duplicates in shipmentID
print("Duplicate ShipmentIDs:", df["ShipmentID"].duplicated().sum())

#Valdating the values 
print(df["cancelled"].unique())

# Validating the values in Order Status
print(df["Order_Status"].unique())

#Analysing for any inregularities in cancelled column relative to order status
print(pd.crosstab(df["Order_Status"],df["cancelled"]))

#Checking the numerical columns
print(df.describe())
print(df[["Boxes","Cost_price"]].describe())

#One shipping with negative Cost _price Identified
print(df[df["Cost_price"] < 0][
    ["ShipmentID", "Shipdate", "Amount", "Boxes", "Cost_price", "Profit","Cost_per_box", "Order_Status"]
])

# Data-quality correction:
# The source dataset contains two columns with swapped names.
# "Cost_price" contains Profit values, while "Profit" contains Cost Price values.
# Swap the column names to match the actual data.
df.rename(columns={"Cost_price":"Temp_Profit"},inplace = True)
df.rename(columns={"Profit":"Cost_price","Temp_Profit":"Profit"},inplace=True)

#Verifying the changes
print(df[["Profit","Cost_price"]].head(10))
print(df[["Profit","Cost_price"]].describe())

#Validating if the Profit Margin% values are right
#As the cost price and profit columns were wrong
print(df[["Amount","Cost_price","Profit","Profit_Margin%"]].head(10))

#Observed the It is not Margin% but the cost%
#Calculating values of Margin% with right formulae
df["Profit_Margin%"]= (df["Profit"]/df["Amount"]) * 100
print(df[["Amount","Cost_price","Profit","Profit_Margin%"]].head(10))

#Finalising the values are accurate for Profit and Margin%
profit_difference = (df["Amount"]-df["Cost_price"]-df["Profit"]).abs()
print("Max_profit_diff: ", profit_difference.max())
Calculated_margin = (df["Profit"]/df["Amount"])*100
margin_difference = (Calculated_margin - df["Profit_Margin%"]).abs()
print("Maximum_margin_difference :", margin_difference.max())

#Final Validation
print(df.info())

#Creating the cleaned file
df.to_csv("data/processed/chocolate_shipments_cleaned.csv",index=False)

print(df.columns.tolist())