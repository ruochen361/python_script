import zipfile
import os



src_dir = 'F:/GDEMV3_30M_分辨率数字高程数据-中国'

target_dir = 'F:/GDEMV3_30M_分辨率数字高程数据_dem'


# 将zip文件解压到目标文件夹
def unzip_file(zip_filepath, dest_path):
    """
    解压zip文件
    :param zip_filepath: 压缩文件路径
    :param dest_path: 解压目标路径
    """
    with zipfile.ZipFile(zip_filepath, 'r') as myzip:
        myzip.extractall(path=dest_path)


#删除文件夹中文件名以endfix结尾的文件
def delete_file(folder_path, endfix):
    """
    删除文件夹中指定文件名以endfix结尾的文件
    :param folder_path: 文件夹路径
    :param endfix: 文件名,除去文件扩展名
    """
    for item in os.listdir(folder_path): # 遍历文件夹
        if item.endswith(endfix,0,len(item)-4) : # 如果文件名与要删除的文件名匹配
            file_path = os.path.join(folder_path, item) # 获取文件的完整路径
            if os.path.isfile(file_path): # 如果是文件
                os.remove(file_path) # 删除文件
                print(f"{item} has been deleted.")


def zipdir(folder_path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # 将文件添加到zip文件中，第二个参数是压缩文件中的路径，也可以理解为添加到zip文件后，保存的文件名
            ziph.write(os.path.join(root, file), 
                       os.path.relpath(os.path.join(root, file), 
                                       os.path.join(folder_path, os.pardir)))



# 将源文件夹中zip文件解压到目标文件夹，删除指定后缀文件后，压缩目标文件
for item in os.listdir(src_dir): # 遍历源文件夹
    if item.endswith('.zip'): # 找到zip文件
        item_full_path = os.path.join(src_dir, item)
        unzip_file(item_full_path, target_dir) # 解压zip文件到目标文件夹
        delete_file(target_dir,'num')

zipf = zipfile.ZipFile('F:/新建文件夹/GDEMV3_30M_分辨率数字高程数据-中国', 'w', zipfile.ZIP_DEFLATED)
zipdir(target_dir, zipf)
zipf.close()