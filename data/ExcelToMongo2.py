import pandas as pd
import pymongo
from decimal import Decimal


# 连接MongoDB数据库

# 配置 MongoDB 连接参数
username = 'username'  # 替换为你的实际用户名
password = 'password'  # 替换为你的实际密码
host = 'localhost'          # 替换为你的 MongoDB 主机名或 IP 地址
port = 27017                # 替换为你的 MongoDB 端口号
database = 'datebase'  # 替换为你要连接的数据库名称

# 创建 MongoClient 对象并连接 MongoDB
client = pymongo.MongoClient(f"mongodb://{username}:{password}@{host}:{port}/{database}")



# 读取Excel文件
df = pd.read_excel('F:\模拟数据\三角槭.xlsx', sheet_name='本地调查数据')

# 指定列
columns = ['立地等级', '树龄', '胸径(cm）','树种'] 

# 将数据转换为JSON
# json_data = df[columns].to_json(orient='records', force_ascii=False)
# print(json_data)

data_dict = df[columns].to_dict(orient='records')

list = []
for d in data_dict:
    new_dict = {'siteLevel':d['立地等级'],'age':d['树龄'],
                'dbh':float(Decimal(d['胸径(cm）']).quantize(Decimal("0.01"), rounding = "ROUND_HALF_UP")),
                'tree':d['树种']}
    list.append(new_dict)

# 指定要连接的数据库和集合
db = client['datebase']
collection = db['table']

# 插入数据到集合中
collection.insert_many(list)

# 输出插入成功的文档数量
print("成功插入文档数量：", len(list))