import pandas as pd
import json

# 读取Excel文件
df = pd.read_excel("G:\测试\同调者详情json转换用.xlsx", sheet_name='同调者详情',keep_default_na=False)


# 指定列
# columns = ['name', 'type', 'mu','ke','image'] 
columns = df.columns # 取所有列
# # 普通字段
# c1 = []
# # 数组字段
# c2 = []
# # 嵌套字段
# c3 = []

# # 嵌套数组字段
# # c4 = []

# for c in columns:
    
#     if c.count(".")>0 :
#         c3.append(c)
#     elif c.count("[]")>0:
#         c2.append(c)
#     else:
#         c1.append(c)

nested_columns = [name.split('.') for name in columns]

# 将数据转换为JSON
# print(c3)
# json_data = df[c1].to_json(orient='records', force_ascii=False)
# records_data = df[c1].to_records()
# dict_data = df[c1].to_dict()
#print(json_data)


json_list = []

data = []
for row in df.itertuples(index=False):
    row_data = {}
    for col, nested_cols in zip(row._fields, nested_columns):
        nested_data = row.__getattribute__(col)
        for nested_col in reversed(nested_cols):
            nested_data = {nested_col: nested_data}
        row_data.update(nested_data)
    data.append(row_data)

# for i in list(df.index):

#     row_dict = {}

#     for c in c1:
#         row_dict[c] = df[c].at[i]

#     for c in c2:
#         row_dict[c] = df[c].at[i].split(",")

#     json_list.append(row_dict)

# #df = pd.DataFrame(json_list)
json_data = json.dumps(data,ensure_ascii=False)
# #新建文件并写入
f = open(r'G:\测试\同调者详情json转换用.json','w', encoding='utf-8')
f.write(json_data)
f.close()