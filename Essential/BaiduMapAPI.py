"""

Author: Danry Li 2018

使用百度地图API，输入地址的文本字符串，返回地址经纬度tuples
返回的数据类型示例：(lng, lat)

"""
import requests


class AddressEncoder:

    def __init__(self, ak, ret_coord_type='bd09ll'):
        """
        初始化

        :param ak: 百度地图Web服务的key，需要自己去百度官网上申请
        :param ret_coord_type: gcj02ll（国测局坐标）、bd09mc（百度墨卡托坐标）、bd09ll（百度经纬度坐标）
        """
        self._ak = ak
        self._output_type = 'json'
        self._ret_coord_type = ret_coord_type

    def _get_params(self, address):
        """
        创建获取地理编码的参数信息

        :param address:
        待解析的地址。最多支持84个字节。
        可以输入两种样式的值，分别是：
        1、标准的结构化地址信息，如北京市海淀区上地十街十号 【推荐，地址结构越完整，解析精度越高】
        2、支持“*路与*路交叉口”描述方式，如北一环路和阜阳路的交叉路口
        第二种方式并不总是有返回结果，只有当地址库中存在该地址描述时才有返回。
        :return: 一个字典
        """
        params = {
            'address': address,

            # 地址所在的城市名。用于指定上述地址所在的城市，
            # 当多个城市都有上述地址时，该参数起到过滤作用，但不限制坐标召回城市。
            'city': '上海市',

            # 可选参数，添加后返回国测局经纬度坐标或百度米制坐标
            # gcj02ll（国测局坐标）、bd09mc（百度墨卡托坐标）、bd09ll（百度经纬度坐标）
            'ret_coordtype': self._ret_coord_type,

            'ak': self._ak,
            'output': self._output_type
        }
        return params

    def _get_url_v2(self, address):
        """
        创建获取地理编码的URL
        :param address: 待解析的地址。
        :return: 一个URL
        """
        url = 'http://api.map.baidu.com/geocoder/v2/?address=%s' \
              '&output=%s&ak=%s' % (address, self._output_type, self._ak)
        return url

    def _get_url_v3(self, address):
        """
        创建获取地理编码的URL
        :param address: 待解析的地址。
        :return: 一个URL
        """
        url = 'https://api.map.baidu.com/geocoding/v3/?address=%s' \
              '&output=%s&ak=%s' % (address, self._output_type, self._ak)
        return url

    def get_address_code(self, address: str):
        """
        :param address: 地址，字符串
        :return: tuple(lng, lat, precise)。lng, lat是经纬度坐标. precise是位置的附加信息，是否精确查找。1为精确查找，即准确打点；0为不精确，即模糊打点。
        """
        # 准备get请求的参数
        p = self._get_params(address)
        url = self._get_url_v3(address)

        # 用request对象获取信息
        request = requests.get(url, p)
        if request.status_code == 200:
            js = request.json()
            if js['status'] == 0:
                return js['result']['location']['lng'], \
                       js['result']['location']['lat'], \
                       js['result']['precise']
            else:
                print('api error')
                print(js)
                return None
        else:
            return None


if __name__ == "__main__":
    f = AddressEncoder(ak='')
    r = f.get_address_code('重庆市回龙坝镇回龙北街21号')
    print(r)
