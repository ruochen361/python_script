import pandas as pd
import psycopg2

# 读取Excel文件
df = pd.read_excel('F:\海南\项目信息表.xlsx', sheet_name='项目信息表')


# 指定列,
columns = ['zxmmc',	'zxmdm','stbhxydymc','xmlx','xmwz','ssqymj','xmqx','ssdw',	'xmmb'	,'tzze','tzzejz','zyczzj','zyczzjjz','dfczzj','dfczzjjz','zj2023','zj2024','zj2025'] 

# 将数据转换为JSON
data_dict = df[columns].to_dict(orient='records')

# 连接pg数据库
conn = psycopg2.connect(
    host="localhost",
    database="datebase",
    user="user",
    password="password"
)
cursor = conn.cursor()

count = 0
try:
    # 遍历每条记录并插入到表格中
    for record in data_dict:
        
        cursor.execute("""
                       INSERT INTO public.hainan_project_info( zxmmc, zxmdm, xmlx, stbhxydymc, xmwz, ssqymj, xmqx, ssdw, xmmb, tzze, tzzejz, zyczzj, zyczzjjz, dfczzj, dfczzjjz, zj2023, zj2024, zj2025) 
                       VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                       """, 
                      (record["zxmmc"], record["zxmdm"], record["xmlx"], record["stbhxydymc"],record["xmwz"], record["ssqymj"],record["xmqx"], record["ssdw"],record["xmmb"], record["tzze"],
                       record["tzzejz"],record["zyczzj"],record["zyczzjjz"], record["dfczzj"],record["dfczzjjz"],record["zj2023"], record["zj2024"],record["zj2025"]))
    
    # 提交事务
    conn.commit()
    count = count+1
except Exception as e:
    print("Error occurred while inserting records into the database.")
    print(e)
finally:
    # 关闭数据库连接
    # cursor.close()
    conn.close()

# 输出插入成功的文档数量
print("成功插入文档数量：{}".format(count))