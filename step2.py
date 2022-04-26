"""

"""

import pandas as pd
from Essential.BaiduMapAPI import AddressEncoder as bdAddress
from Essential.AmapAPI import AddressEncoder as gdAddress
from Essential.GeoConvert import bd09_to_wgs84


def get_address_coord(method='amap', key=''):
    """
    把地址的经纬度信息抓下来。

    :param method: amap:调用高德api生成国测局坐标。baidu: 调用百度api生成wgs84坐标。
    :param key: api服务密钥，自己去对应网站申请
    :return:
    """
    data = pd.read_csv('Result/pre-processing.csv', index_col=0)

    if method == 'baidu':
        a = bdAddress(ak=key)
        data['result'] = data['地址'].apply(lambda x: a.get_address_code(x))
        data['precise'] = data['result'].apply(lambda x: x[2])
        data['result'] = data['result'].apply(lambda x: bd09_to_wgs84(x[0], x[1]))
    else:
        a = gdAddress(key=key)
        data['result'] = data['地址'].apply(lambda x: a.get_address_code(x))

    data['lng'] = data['result'].apply(lambda x: x[0])
    data['lat'] = data['result'].apply(lambda x: x[1])
    del data['result']
    data.to_csv('Result/coord.csv')
    return data


if __name__ == '__main__':
    get_address_coord()
