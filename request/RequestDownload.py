import requests,json
import urllib.request


# class SortSet:
#      id= "datadate"
#      sort= "desc"



# class Table:
#     offset = 0
#     pageSize = 10
#     totalPage = 1
#     totalSize = 0
#     sortSet = [SortSet()]
#     filterSet = []

#     def __init__(self, offset, totalPage, totalSize):
#        self.offset = offset
#        self.totalPage = totalPage
#        self.totalSize = totalSize


# class Result:
#     keyid = ""
#     pagesize: 10
#     offset: 10
#     total: 22912
#     data: list


# class Record:
#     dataid = ""
#     thumb: 1
#     operations: 2
#     path: 3
#     row: 42
#     ct_long: 42.5
#     ct_lat: 3.5
#     dataexists: 1
#     filesize: 16553622


# https://bjdl.gscloud.cn/sources/download/aeab8000652a45b38afbb7ff023ddabb/" + dataid + "?sid=LSXKQJxGyflDM14UUlg1HbssIASqCdkcycwSIyiOHfGV8w&uid=954172


# https://www.gscloud.cn/wsd/gscloud_wsd/dataset/query_data
# tableInfo: {"offset":0,"pageSize":10,"totalPage":1,"totalSize":0,"sortSet":[{"id":"datadate","sort":"desc"}],"filterSet":[]}
# pid: aeab8000652a45b38afbb7ff023ddabb
#      aeab8000652a45b38afbb7ff023ddabb


pid = "aeab8000652a45b38afbb7ff023ddabb"


# request_params = {}
# request_params['tableInfo'] = {"offset":0,"pageSize":10,"totalPage":1,"totalSize":0,"sortSet":[{"id":"datadate","sort":"desc"}],"filterSet":[]}
# request_params['pid'] = pid
# request_params['tableInfo']["offset"] = 2
# r = requests.get(url="https://www.gscloud.cn/wsd/gscloud_wsd/dataset/query_data", params=request_params)
# print(r.content)
# total = 22912



table = {"offset":0,"pageSize":100,"totalPage":330,"totalSize":22912,"sortSet":[{"id":"datadate","sort":"desc"}],"filterSet":[]}
offset = 279
count = 0
while offset < 22912:
    table['offset'] = offset

    request_params = {}
    request_params['tableInfo'] = json.dumps(table)
    request_params['pid'] = pid
    r = requests.get(url="https://www.gscloud.cn/wsd/gscloud_wsd/dataset/query_data", params=request_params)
    print('offset={}'.format(offset))
    records = json.loads(r.content).get("data")
    

    base_dir = "F:/GDEMV3_30M_分辨率数字高程数据"
    for i in records:
        dataid = i["dataid"]
        url = "https://bjdl.gscloud.cn/sources/download/aeab8000652a45b38afbb7ff023ddabb/" + dataid + "?sid=LSXKQJxGyflDM14UUlg1HbssIASqCdkcycwSIyiOHfGV8w&uid=954172"
        # file = requests.get(url)
        file_path = base_dir + '/' + dataid + '.zip'
        urllib.request.urlretrieve(url,file_path)
        # open("F:/GDEMV3_30M_分辨率数字高程数据","wb").write(file.content)
        count+=1
        print('count{}文件{}下载完成'.format(count,dataid))
    
    offset+=100

print("finish")