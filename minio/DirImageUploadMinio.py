import os
from PIL import Image

from minio import Minio
from minio.error import MinioException



def upload_to_minio(file_name,file_path):
    # 创建一个客户端
    minioClient = Minio('host',
        access_key='user',
        secret_key='password',
        secure=True
    )
    bucket_name = 'bucket_name'
    # 判断桶是否存在
    check_bucket = minioClient.bucket_exists(bucket_name)

    if not check_bucket:
        minioClient.make_bucket(bucket_name)
    try:

        response = minioClient.fput_object(bucket_name, file_name,file_path,
                                           content_type='image/png')
        # 打印上传成功的信息
        print('File uploaded successfully:')
        print('ETag:', response.etag)
        print('Version ID:', response.version_id)

        url = minioClient.get_presigned_url('GET',bucket_name,file_name)
        # print('url:', file_name, url[0:url.index('?')] )
        sql = f"db.diseases_pests_type.update({{'name':'{file_name[0:file_name.index('.')]}'}},{{$set:{{'image':'{url[0:url.index('?')]}'}}}})"
        print(sql)
    except MinioException as err:
        # 打印上传失败的错误信息
        print('File upload failed:', err)





# 指定文件夹路径
folder_path = 'G:\新建文件夹\图片'

# 遍历文件夹中的文件
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path) and filename.endswith(('.jpg', '.jpeg', '.png')):
        # try:
        #     # 打开图像文件
        #     image = Image.open(file_path)
            
        #     # 可以对图像进行各种操作，例如显示、保存、处理等
        #     # 这里仅打印图像大小作为示例操作
        #     print(f"Image: {filename}, Size: {image.size}")
            
        #     # 关闭图像文件
        #     image.close()
        # except IOError:
        #     print(f"Failed to open image: {filename}")
        upload_to_minio(filename,file_path)




