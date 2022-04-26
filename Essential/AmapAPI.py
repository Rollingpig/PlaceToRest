"""

使用高德地图API，输入地址的文本字符串，返回地址经纬度tuples
返回的数据类型示例：(lng, lat)

"""
import requests


class AddressEncoder:

    def __init__(self, key):
        """
        初始化

        :param key: 高德地图Web服务的key，需要自己去高德官网上申请
        """
        self._ak = key

    def _get_params(self, address):
        """
        创建获取地理编码的参数信息

        :param address:规则遵循：国家、省份、城市、区县、城镇、乡村、街道、门牌号码、屋邨、大厦，如：北京市朝阳区阜通东大街6号。
        :return: 一个字典
        """
        params = {
            'address': address,
            'key': self._ak,
            'city': '上海',
        }
        return params

    @staticmethod
    def _get_url():
        """
        创建获取地理编码的URL
        :return: 一个URL
        """
        url = 'https://restapi.amap.com/v3/geocode/geo?parameters'
        return url

    def get_address_code(self, address: str):
        """
        :param address: 地址，字符串
        :return: tuple(lng, lat, precise)。lng, lat是经纬度坐标. precise是位置的附加信息，是否精确查找。1为精确查找，即准确打点；0为不精确，即模糊打点。
        """
        # 准备get请求的参数
        p = self._get_params(address)
        url = self._get_url()

        # 用request对象获取信息
        request = requests.get(url, p)
        if request.status_code == 200:
            js = request.json()
            if js['status'] == '1':
                location_str = js['geocodes'][0]['location']
                return float(location_str.split(',')[0]), float(location_str.split(',')[1])
            else:
                print('api error')
                print(js)
                return None
        else:
            return None


if __name__ == "__main__":
    f = AddressEncoder(key='')
    r = f.get_address_code('重庆市回龙坝镇回龙北街21号')
    print(r)
