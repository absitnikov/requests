import os
import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def _get_upload_link(self, file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload(self, file_path: str):
        href = self._get_upload_link(file_path=file_path.split('\\')[-1]).get("href", "")
        response = requests.put(href, data=open(str(file_path.split('\\')[-1]), 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Successful uploaded")


if __name__ == '__main__':
    path_to_file = os.path.join(os.getcwd(), '1.txt')
    token =
    uploader = YaUploader(token)
    result = uploader.upload('1.txt')
