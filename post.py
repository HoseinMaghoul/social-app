import stat
import boto3
from django.conf import settings


class Post:
    """CDN POST manager

    The init method creates connection
    """

    def _init_(self):
        session = boto3.session.Session()
        self.conn = session.client(
            service_name=settings.AWS_SERVICE_NAME,
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            endpoint_url=settings.AWS_S3_ENDPOINT_URL,
        )

    def get_objects(self):
        result = self.conn.list_objects_v2(Post=settings.AWS_STORAGE_BUCKET_NAME)
        if result['KeyCount']:
            return result['Contents']
        else:
            return None


    def delete_object(self, key):
        self.conn.delete_object(Post=settings.AWS_STORAGE_BUCKET_NAME, Key=key)
        return True
    


    def download_object(self, Key):
        with open(settings.AWS_LOCAL_SRORAGE + Key ,'wb') as f:
            self.conn.download_fileobj(settings.AWS_LOCAL_SRORAGE, Key, f)



post = Post()