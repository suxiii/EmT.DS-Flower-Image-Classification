import pandas as pd
import numpy as np

# Đọc dữ liệu từ URL
url = "https://raw.githubusercontent.com/Apress/data-analysis-and-visualization-using-python/master/Ch05/Sales.csv"
data = pd.read_csv(url, header=0, sep=",")

# Tạo cột Total
data['Total'] = data['Quantity'] * data['Unit Price']
data['Month'] = pd.to_datetime(data['Date']).dt.month
data['Quarter'] = pd.to_datetime(data['Date']).dt.quarter

# Tìm NV có kết quả kinh doanh cao nhất theo từng tháng
result = data.groupby(['Month', 'Salesperson']).sum()
result = result.reset_index()
result = result.sort_values(by=['Month', 'Total'], ascending=False)
result = result.drop_duplicates(subset='Month', keep='first')
print(result[['Month', 'Salesperson', 'Total']])
print('--------------------------------------')



