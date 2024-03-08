from minio import Minio
from kafka import KafkaConsumer
import json
from PIL import Image


# 监听minio事件kafka消息并压缩图片上传minio
# minio监听事件监听图片上传

#压缩图片
def compress_image(image_path, target_size, target_path):
    image = Image.open(image_path)
    image.thumbnail(target_size)
    image.save(target_path)  # 保存压缩后的图片
 


# Convenient dict for basic config
config = {
  "dest_bucket":    "event-test", # This will be auto created
  "minio_endpoint": "host",
  "minio_username": "user",
  "minio_password": "password",
  "kafka_servers":  "host",
  "kafka_topic":    "minio-event", # This needs to be created manually
}


# Initialize MinIO client
minio_client = Minio(config["minio_endpoint"],
               secure=True,
               access_key=config["minio_username"],
               secret_key=config["minio_password"]
               )

# Create destination bucket if it does not exist
if not minio_client.bucket_exists(config["dest_bucket"]):
  minio_client.make_bucket(config["dest_bucket"])
  print("Destination Bucket '%s' has been created" % (config["dest_bucket"]))

# Initialize Kafka consumer
consumer = KafkaConsumer(
  bootstrap_servers=config["kafka_servers"],
  value_deserializer = lambda v: json.loads(v.decode('ascii'))
)

consumer.subscribe(topics=config["kafka_topic"])

target_size = (800, 600)  # 目标尺寸
target_size_str = str(target_size[0]) +'_'+ str(target_size[1])

try:
  print("Ctrl+C to stop Consumer\n")
  for message in consumer:
    message_from_topic = message.value

    request_type = message_from_topic["EventName"]
    bucket_name, object_path = message_from_topic["Key"].split("/", 1)


    # 创建事件，生成压缩图片并上传
    if request_type == "s3:ObjectCreated:Put" and not object_path.split('.')[0].endswith(target_size_str) :
      minio_client.fget_object(bucket_name, object_path, object_path)
      
      names = object_path.split('.')
      target_path = names[0] + '_' + target_size_str +'.'+ names[1]
      compress_image(object_path, target_size, target_path)

      minio_client.fput_object(config["dest_bucket"], target_path, target_path)

      print("- Uploaded processed object '%s' to Destination Bucket '%s'" % (object_path, config["dest_bucket"]))

    # 删除事件，同步删除压缩图片
    if request_type == "s3:ObjectRemoved:Delete" and not object_path.split('.')[0].endswith(target_size_str) :    
      names = object_path.split('.')
      target_path = names[0] + '_' + target_size_str +'.'+ names[1]

      minio_client.remove_object(bucket_name,target_path)

      print("- Uploaded processed object '%s' to Destination Bucket '%s'" % (object_path, config["dest_bucket"]))

except KeyboardInterrupt:

  print("\nConsumer stopped.")