from aiobotocore.session import get_session
from contextlib import asynccontextmanager
import os
from dotenv import load_dotenv
load_dotenv()


class S3Client:
    def __init__(
        self,
        access_key: str,
        secret_key: str,
        endpoint_url: str,
        bucket_name: str
    ) -> None:
        self.config = {
            "aws_access_key_id": access_key,
            "aws_secret_access_key": secret_key,
            "endpoint_url": endpoint_url,
        }
        self.bucket_name = bucket_name
        self.session = get_session()

    @asynccontextmanager
    async def get_client(self):
        async with self.session.create_client("s3", **self.config) as client:
            yield client

    async def upload_file(self, file_path: str):
        object_name = file_path.split("/")[-1]
        async with self.get_client() as client:
            with open(file_path, "rb") as file:
                await client.put_object(Bucket=self.bucket_name, Key=object_name, Body=file)


async def main():
    s3_client = S3Client(
        access_key=os.environ.get("ACCESS_KEY"),
        secret_key=os.environ.get("SECRET_KEY"),
        endpoint_url=os.environ.get("ENDPOINT_URL"),
        bucket_name=os.environ.get("BUCKET_NAME"),        
    )
    
    await s3_client.upload_file(file_path="test.txt")