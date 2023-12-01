import requests


def is_network_connected():
    try:
        # 发送一个HTTP请求来检测网络连接
        requests.get('https://binzhijie.github.io/rollcall_web_config/web_config.ini')
        return True
    except requests.exceptions.RequestException:
        return False

if __name__ == '__main__':
    requests.get('https://binzhijie.github.io/rollcall_web_config/web_config.ini')
    print(is_network_connected())