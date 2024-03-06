import pandas as pd
import pymongo

# 读取Excel文件
df = pd.read_excel('G:\新建文件夹\自然保护区\自然保护区业务.xlsx', sheet_name='病虫害名录')


# 指定列
columns = ['name', 'type', 'mu','ke','image'] 

# 将数据转换为JSON
# json_data = df[columns].to_json(orient='records', force_ascii=False)
# print(json_data)

data_dict = df[columns].to_dict(orient='records')

for d in data_dict:
    d['image'] = f"url/{d['name']}.png"

# 连接MongoDB数据库

# 配置 MongoDB 连接参数
username = 'username'  # 替换为你的实际用户名
password = 'password'  # 替换为你的实际密码
host = 'localhost'          # 替换为你的 MongoDB 主机名或 IP 地址
port = 27017                # 替换为你的 MongoDB 端口号
database = 'datebase'  # 替换为你要连接的数据库名称

# 创建 MongoClient 对象并连接 MongoDB
client = pymongo.MongoClient(f"mongodb://{username}:{password}@{host}:{port}/{database}")

# 指定要连接的数据库和集合
db = client['datebase']
collection = db['table']


# 插入数据到集合中
collection.insert_many(data_dict)

# 输出插入成功的文档数量
print("成功插入文档数量：", len(data_dict))