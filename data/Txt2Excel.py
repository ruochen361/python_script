import pandas as pd


dict_list = []

# with open('G:\master\名单1.txt', 'r', encoding='utf-8') as f:
#     for ann in f.readlines():
#         ann = ann.strip('\n')       #去除文本中的换行符
#         record = ann.split(" ")
#         list.append({"姓名":record[1],'科目一': record[3],'科目二': record[4],'科目三': record[5],'科目四': record[6],'总分': record[7]})
#         print(ann)



rcv_data = pd.read_csv('G:\master\名单4.txt', sep=' ')
# rcv_data.head()

# ic(rcv_data)
rcv_data.to_excel('成绩4.xlsx', index = False)