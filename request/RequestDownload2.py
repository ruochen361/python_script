import requests,json
import urllib.request



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

# {"offset":0,"pageSize":10,"totalPage":0,"totalSize":0,"sortSet":[{"id":"datadate","sort":"desc"}],"filterSet":[{"id":"ct_long","value":"73.5"},{"id":"ct_lat","value":"2.5"},{"id":"dataexists","value":"1"}]}

table = {"offset":0,"pageSize":10,"totalPage":0,"totalSize":0,"sortSet":[{"id":"datadate","sort":"desc"}],"filterSet":[]}

ct_long = 94
ct_lat = 53
count = 0
while ct_long < 100:
    ct_long += 0.5
    
    while ct_lat < 54:
        ct_lat += 0.5
        table['filterSet'] = [{"id":"ct_long","value":str(ct_long)},{"id":"ct_lat","value":str(ct_lat)},{"id":"dataexists","value":"1"}]

        request_params = {}
        request_params['tableInfo'] = json.dumps(table)
        request_params['pid'] = pid
        r = requests.get(url="https://www.gscloud.cn/wsd/gscloud_wsd/dataset/query_data", params=request_params)
        print('ct_long={},ct_lat={}'.format(ct_long,ct_lat))
        records = json.loads(r.content).get("data")
        

        base_dir = "F:/GDEMV3_30M_分辨率数字高程数据-中国"
        for i in records:
            dataid = i["dataid"]
            url = "https://bjdl.gscloud.cn/sources/download/aeab8000652a45b38afbb7ff023ddabb/" + dataid + "?sid=LSXKQJxGyflDM14UUlg1HbssIASqCdkcycwSIyiOHfGV8w&uid=954172"
            # file = requests.get(url)
            file_path = base_dir + '/' + dataid + '.zip'
            urllib.request.urlretrieve(url,file_path)
            count+=1
            print('count{}文件{}下载完成'.format(count,dataid))
    print('{}'.format(ct_long))
    ct_long+=0.5
    ct_lat = 2
        

print("finish")