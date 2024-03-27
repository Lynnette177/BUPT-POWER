import requests
import json
# 定义要访问的网址
url = 'https://app.bupt.edu.cn/buptdf/wap/default/chong'

# 定义要发送的 Cookie
cookies = {
    'eai-sess':'d1fmrog0copqkir6ke5l3hg1j5',
   # 'UUkey':'实测只传eai就够了'
}
response = requests.get(url, cookies=cookies,verify=False,allow_redirects=False)
if response.status_code == 200:
    # 打印响应内容
    print("Cookie有效 保持登录")
    payload = {
        'partmentId': '沙河校区xxxxxx',
        'floorId': 'x层',
        'dromNumber': 一串数字，这部分数据都自己去浏览器查一下看一眼网络请求就行了,
        'areaid': x
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 添加其他的请求头部信息
    }
    response = requests.post('https://app.bupt.edu.cn/buptdf/wap/default/search', data=payload, headers=headers,cookies=cookies,)
    print(response.text)
    data = json.loads(response.text)
    info = {
        "楼层": data["d"]["data"]["floorName"],
        "日期时间": data["d"]["data"]["time"],
        "剩余电量": data["d"]["data"]["surplus"] + " 度",
        "总用电量": data["d"]["data"]["vTotal"] + " 度",
        "单价": data["d"]["data"]["price"] + " 元/度",
        "校区": data["d"]["data"]["parName"]
    }

    # 连接信息为一个字符串
    message = (
        f"楼层：{info['楼层']}\n"
        f"日期时间：{info['日期时间']}\n"
        f"剩余电量：{info['剩余电量']}\n"
        f"总用电量：{info['总用电量']}\n"
        f"单价：{info['单价']}\n"
        f"位置：{info['校区']}"
    )
    print(message)
