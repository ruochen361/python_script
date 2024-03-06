import pandas as pd

# 读取Excel文件
df = pd.read_excel('G:\测试\同调者详情json转换用.xlsx', sheet_name='同调者详情')


# 指定列
# columns = ['name', 'type', 'mu','ke','image'] 
columns = df.columns # 取所有列
# 将数据转换为JSON
json_data = df[columns].to_json(orient='records', force_ascii=False)
print(json_data)

#新建文件并写入
f = open(r'G:\测试\同调者详情json转换用.json','w', encoding='utf-8')
f.write(json_data)
f.close()