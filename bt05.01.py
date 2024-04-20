import  pandas as pd

# Đọc dữ liệu từ file sales_data.csv
#Khu vực nào bán tốt trong quý 2 ?
result = data.groupby(['Region', 'Quarter']).sum()
result = result.reset_index()
result = result[result['Quarter'] == 2]
result = result.sort_values(by='Total', ascending=False)
print(result[['Region', 'Total']])
print('--------------------------------------')

#Kết quả kinh doanh trung bình Sale theo khu vực
result = data.groupby('Region').mean()
result = result.reset_index()
print(result[['Region', 'Total']])
print('--------------------------------------')

data = pd.read_csv('sales_data.csv')
data['Total'] = data['Quantity'] * data['Unit Price']
data['Month'] = pd.to_datetime(data['Date']).dt.month
data['Quarter'] = pd.to_datetime(data['Date']).dt.quarter

#Tìm NV có kết quả kinh doanh cao nhất theo từng tháng
result = data.groupby(['Month', 'Salesperson']).sum()
result = result.reset_index()
result = result.sort_values(by=['Month', 'Total'], ascending=False)
result = result.drop_duplicates(subset='Month', keep='first')
print(result[['Month', 'Salesperson', 'Total']])
print('--------------------------------------')

#Khu vực nào bán tốt trong quý 2 ?
result = data.groupby(['Region', 'Quarter']).sum()
result = result.reset_index()
result = result[result['Quarter'] == 2]
result = result.sort_values(by='Total', ascending=False)
print(result[['Region', 'Total']])
print('--------------------------------------')

#Kết quả kinh doanh trung bình Sale theo khu vực
result = data.groupby('Region').mean()
result = result.reset_index()
print(result[['Region', 'Total']])
print('--------------------------------------')