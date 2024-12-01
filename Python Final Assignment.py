#importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt
#reading the file
df = pd.read_csv('https://storage.googleapis.com/courses_data/Assignment%20CSV/finance_liquor_sales.csv')

#Creating a new data frame for the first section of the assgnment ,also specifing the time frame
df1 = df[(df['date'] > '2016-01-01') & (df['date'] < '2020-01-01')]
#
df1 = df1[['zip_code', 'item_number', 'bottles_sold']]
#
# #Grouped by zip code and item number so the same item numbers for the same zip codes are combined with sum
df1_grouped = df1.groupby(['zip_code','item_number'], as_index=False).agg('sum')
#
# #Removing duplicates so we only have the highest bottles sold by zip code
most_pplr_itm = df1_grouped.drop_duplicates(subset="zip_code")

plt.figure(figsize=(10,5))
plt.scatter(most_pplr_itm['zip_code'],most_pplr_itm['bottles_sold'], marker='X')

plt.title('Bottles Sold per zipcode')
plt.xlabel('Zip Code')
plt.ylabel('Bottles Sold')

plt.show()

#Second task

#Creating a new data frame for the second section of the assgnment ,also specifing the time frame
df2 = df[(df['date'] > '2016-01-01') & (df['date'] < '2020-01-01')]

df2 = df2[['store_number', 'store_name', 'sale_dollars']]

#Grouped by store using sum() and then reseting index beacause it is lost when we group by
store_sales = df2.groupby(['store_number','store_name'])['sale_dollars'].sum().reset_index()
#calculating overall sales of all the stores
overall_sales = store_sales['sale_dollars'].sum()
#calculating store sales by creating a new column sales percentage
store_sales['sales_percentage'] = (store_sales['sale_dollars'] / overall_sales) * 100
#we sort the values so we can find the 15 stores with the biggest sales percentage and we makethe column of sales percentage have 2 decimals
sorted_store_sales = store_sales.sort_values(by='sales_percentage', ascending=False).round(decimals=2)

# Select the top 15 stores and reseting index so we have nice index order
top_15_stores = sorted_store_sales.head(15).reset_index()

#print(top_15_stores[['store_name','sales_percentage']])

plt.figure(figsize=(12, 6))
bars = plt.barh(top_15_stores['store_name'], top_15_stores['sales_percentage'])

#Creating a function so we can add comments on the bars
def autolabel(rects):
    for rect in rects:
        plt.text(rect.get_width() - 0.8, rect.get_y() + 0.2,
                 str(round((rect.get_width()), 2)),
                 fontsize=10,
                 color='white')

autolabel(bars)
plt.xlabel('%Sales')
plt.ylabel('Store Name')
plt.title('%Sales by Store')

plt.show()














