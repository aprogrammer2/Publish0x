import requests
import time
import random
cookies = {
    'gamp': 'eyJpdiI6ImcvL2NXSHd1VUFLRVd6ZGxXTkxGMlE9PSIsInZhbHVlIjoiNklyTXlqMHBXUjN2aXZUZEc5SE9NdHNTL05jQ1VGeS90Y29TTW5CSDJSd1dyQk1yVVh2RGV2RHI1cGJXRXJiTHpnVXFsVlg2WnBWdjNvTW8xSDBBRWpXWFZLV0FCTEhxU1p1T2h6ZWVGWVE9IiwibWFjIjoiMzU3OGI3NmI4NTcxZjdhNjU0MTYyNDcxZThlMGU1YzVlODI4NTE5Njg1NmNhZjQ1NGVkZDRiNmZhMWIyMTlmZiJ9',
    '_ga': 'GA1.2.2007771342.1681399946',
    '_gid': 'GA1.2.1602047384.1681399946',
    'popUpRegisterClosed': '1',
    '__cf_bm': 'k.3vUiHAvgoqalubNSr0cQuqfIxQWIKx8yfVxMxuiQw-1681402540-0-AT6L0Bpt553pgYb6ed7XJIEP6tYY9sLO+rXJpxLpH3soStW3KKkUUcb6MQxwQ+Xsrk4uYGHEWB79P6LfuET1JUMKOphuoRdhV/OTWJqu0cX1ihX5s+yeBoEIh3gCu3g6cw==',
    'XSRF-TOKEN': 'eyJpdiI6IkZYSmF5czc2Um9ES0RxYlJyZVZjNlE9PSIsInZhbHVlIjoicmdjeUsvYm9UdW0xOTFzRWN2N0R5RzJ0d1V6VjFQbGZkcW9vcmdURE1iK3FJOEl2QUs3c1JsUUhZT1RnejloR3BncVQ4TENONnBSd1JkczViMnp5blVtY1A0enBBVUY3QjQ3R2xKOXFZRndRc2tUbWdvMVQzaDZBY1R5NGo5WHkiLCJtYWMiOiJiMWJlZGJjMjUyMzVkYjQzYzJhZWJlOWFkZGYwZmE2OTM3MTFmOGU4Nzk1YzRjNDc4ODQwM2FjYWFjODc0Y2ZhIn0%3D',
    'publish0x_session': 'eyJpdiI6IkJKNjJKVFEyNkhTbDBTZHpOZUUveGc9PSIsInZhbHVlIjoiTkFGTlNaeGc3ZUxJYUlCVkdKOFRFL0lIa01UT0Z4R2JiOGUwT1QvbUFwdkhoNjIrd3QvTXdEbndQaTVNMTNxQWhGdHN3NE9EOTRmNmRzdTNnaXNIdlozMGlGVHhaM3ZFOUFRbUFVbkRLMHFNSDFwU2l3TjZLak5nSFVMZUdmRTciLCJtYWMiOiJlMjJlODg3NzQ3ZmQ1NmUzNWEzOWM3NTM0ZjIyZjM3N2M5Y2U3NzlkYmI0YjkxYTA3YzMyMjA1ZjNjMDRlMjY2In0%3D',
}

headers = {
    'authority': 'www.publish0x.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'accept-language': 'en-US,en;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'gamp=eyJpdiI6ImcvL2NXSHd1VUFLRVd6ZGxXTkxGMlE9PSIsInZhbHVlIjoiNklyTXlqMHBXUjN2aXZUZEc5SE9NdHNTL05jQ1VGeS90Y29TTW5CSDJSd1dyQk1yVVh2RGV2RHI1cGJXRXJiTHpnVXFsVlg2WnBWdjNvTW8xSDBBRWpXWFZLV0FCTEhxU1p1T2h6ZWVGWVE9IiwibWFjIjoiMzU3OGI3NmI4NTcxZjdhNjU0MTYyNDcxZThlMGU1YzVlODI4NTE5Njg1NmNhZjQ1NGVkZDRiNmZhMWIyMTlmZiJ9; _ga=GA1.2.2007771342.1681399946; _gid=GA1.2.1602047384.1681399946; popUpRegisterClosed=1; __cf_bm=k.3vUiHAvgoqalubNSr0cQuqfIxQWIKx8yfVxMxuiQw-1681402540-0-AT6L0Bpt553pgYb6ed7XJIEP6tYY9sLO+rXJpxLpH3soStW3KKkUUcb6MQxwQ+Xsrk4uYGHEWB79P6LfuET1JUMKOphuoRdhV/OTWJqu0cX1ihX5s+yeBoEIh3gCu3g6cw==; XSRF-TOKEN=eyJpdiI6IkZYSmF5czc2Um9ES0RxYlJyZVZjNlE9PSIsInZhbHVlIjoicmdjeUsvYm9UdW0xOTFzRWN2N0R5RzJ0d1V6VjFQbGZkcW9vcmdURE1iK3FJOEl2QUs3c1JsUUhZT1RnejloR3BncVQ4TENONnBSd1JkczViMnp5blVtY1A0enBBVUY3QjQ3R2xKOXFZRndRc2tUbWdvMVQzaDZBY1R5NGo5WHkiLCJtYWMiOiJiMWJlZGJjMjUyMzVkYjQzYzJhZWJlOWFkZGYwZmE2OTM3MTFmOGU4Nzk1YzRjNDc4ODQwM2FjYWFjODc0Y2ZhIn0%3D; publish0x_session=eyJpdiI6IkJKNjJKVFEyNkhTbDBTZHpOZUUveGc9PSIsInZhbHVlIjoiTkFGTlNaeGc3ZUxJYUlCVkdKOFRFL0lIa01UT0Z4R2JiOGUwT1QvbUFwdkhoNjIrd3QvTXdEbndQaTVNMTNxQWhGdHN3NE9EOTRmNmRzdTNnaXNIdlozMGlGVHhaM3ZFOUFRbUFVbkRLMHFNSDFwU2l3TjZLak5nSFVMZUdmRTciLCJtYWMiOiJlMjJlODg3NzQ3ZmQ1NmUzNWEzOWM3NTM0ZjIyZjM3N2M5Y2U3NzlkYmI0YjkxYTA3YzMyMjA1ZjNjMDRlMjY2In0%3D',
    'origin': 'https://www.publish0x.com',
    'pragma': 'no-cache',
    'referer': 'https://www.publish0x.com/zero-to-hero/zero-to-hero-april-xxzqwwj?a=JxboVJYNag',
    'sec-ch-ua': '"Chromium";v="112", "Brave";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'sec-gpc': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
}

data = {
    'post_id': '398565',
    '_token': '9C2e3dXFfUQonrppfLBjra9hQ3Op8DQeLl4vpwdy',
    'split': '20',
}
while time.sleep(600):
    data["post_id"] = str(random.randint(0,100000))
    response = requests.post('https://www.publish0x.com/sendtips', cookies=cookies, headers=headers, data=data)