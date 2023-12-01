# 导入所需的Python模块
import requests  # 用于发送HTTP请求的模块
import configparser  # 用于解析INI文件的模块
import os  # 用于操作系统相关操作的模块，如文件处理和路径操作


# 定义一个类IniFileCache，用于管理INI文件缓存
class IniFileCache:
    # 初始化函数，传入INI文件的URL和缓存文件的路径
    def __init__(self, url, cache_file):
        self.url = url  # 缓存的INI文件URL
        self.cache_file = cache_file  # 缓存的INI文件本地路径
        self.cached_data = None  # 缓存的INI文件内容
        # 从缓存中加载INI文件内容
        self.load_from_cache()

        # 从缓存文件中加载INI文件内容
        self.fetch_from_web()

    def load_from_cache(self):
        # 判断缓存文件是否存在
        if os.path.exists(self.cache_file):
            # 打开缓存文件并读取内容
            with open(self.cache_file, 'r') as file:
                self.cached_data = configparser.ConfigParser().read_string(file.read())  # 将文件内容加载到cached_data变量中

    # 从网络上获取INI文件内容
    def fetch_from_web(self):
        # 发送GET请求获取INI文件内容
        response = requests.get(self.url)
        # 如果请求成功并且状态码为200
        if response.status_code == 200:
            # 将获取到的INI文件内容保存到cached_data变量中
            self.cached_data = response.text
            # 将INI文件内容保存到缓存文件中
            self.save_to_cache()

            # 将INI文件内容保存到缓存文件中

    def save_to_cache(self):
        # 打开缓存文件并写入INI文件内容
        with open(self.cache_file, 'w',encoding='gbk') as file:
            file.write(self.cached_data)

            # 清理缓存文件

    def clear_cache(self):
        # 判断缓存文件是否存在
        if os.path.exists(self.cache_file):
            # 删除缓存文件
            os.remove(self.cache_file)

        # 在主函数中创建一个IniFileCache对象，传入INI文件的URL和缓存文件的路径


def main(url,file_name):
    url = url  # 替换为实际的INI文件链接
    cache_file = file_name  # 替换为实际的缓存文件名
    cache = IniFileCache(url, cache_file)
    cache.save_to_cache()

    # 在这里执行其他操作，可以随时调用cache.fetch_from_web()方法更新缓存
    # ... 其他操作 ...

    # 当程序退出时，清理缓存
    cache.clear_cache()
    del cache


# 判断当前脚本是否为主脚本，如果是则执行主函数
if __name__ == '__main__':
    main('https://binzhijie.github.io/rollcall_web_config/web_config.ini','web_config.ini')