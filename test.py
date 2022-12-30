import requests
from django.db import connection

# cursor = connection.cursor()
# cursor.execute("SELECT * FROM upload_data")
# all_data = cursor.fetchall()
# print(all_data)


def telebots(mess):
    requests.get(
        url=f"https://api.telegram.org/bot5082135962:AAGhUTECboqGDnU8gAtY8kK8VgWUbdjmeVc/sendMessage?chat_id=935920479&parse_mode=HTML&text={mess}")

