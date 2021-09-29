# 2-A
import pandas as pd
employee_address = pd.read_sas('/Users/sunjaelee/Desktop/학교/학부연구생/성재조교님 과제/1st_시험문제/employee_addresses.sas7bdat', format='sas7bdat', encoding='utf-8')

new_addresses = employee_address.sort_values(by=['Employee_ID'])
new_addresses.to_csv('/Users/sunjaelee/Desktop/학교/학부연구생/성재조교님 과제/1st_시험문제/work/new_addresses')

# 2-B
new_addresses.head()
countries = list(set(new_addresses['Country']))
countries
is_US = (new_addresses.Country == b'US') | (new_addresses.Country == b'us')
is_AU = (new_addresses.Country == b'AU') | (new_addresses.Country == b'au')
new_addresses[is_US]
new_addresses[is_AU]

# 2-C
print('New Employee Addresses')

# 3-A
pd.options.display.float_format = '{:.2f}'.format
orders = pd.read_sas('/Users/sunjaelee/Desktop/학교/학부연구생/성재조교님 과제/1st_시험문제/orders.sas7bdat', format='sas7bdat')
orders.set_index('Order_ID')

# 3-B
is_order_type_1 = orders.Order_Type == 1
new_order = orders.loc[:, ['Order_ID', 'Customer_ID']]
new_order[is_order_type_1].set_index('Order_ID')

# 3-C
new_order = orders.loc[:, ['Customer_ID', 'Order_Date', 'Order_ID']]
new_order.sort_values(by=['Customer_ID', 'Order_Date'], ascending=[True, False])

# 4-A
order_fact = pd.read_sas('/Users/sunjaelee/Desktop/학교/학부연구생/성재조교님 과제/1st_시험문제/order_fact.sas7bdat', format='sas7bdat')
order_fact.loc[:, ['Customer_ID', 'Order_Type', 'Order_Date', 'Delivery_Date', 'Total_Retail_Price']]

# 4-B
import datetime
order_fact['Order_Date'] = order_fact['Order_Date'].dt.strftime('%A, %B %d, %Y')
order_fact['Total_Retail_Price'] = order_fact['Total_Retail_Price'].astype(int)
order_fact.loc[:, ['Order_Date', 'Total_Retail_Price']]

#4-C
order_fact.rename(columns={'Order_Date': '주문일', 'Delivery_Date': '배송일'}, inplace=True)
order_fact.loc[:, ['주문일', '배송일']]

#4-D
order_fact['Order_Type'] = order_fact['Order_Type'].map({1: 'DM', 2: 'TM', 3: 'Internet'})
order_fact['Order_Type']