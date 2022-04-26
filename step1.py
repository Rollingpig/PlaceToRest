"""

"""

import pandas as pd


def save_from_clipboard():
    raw = pd.read_clipboard()
    raw.to_csv('Result/raw.csv')
    return raw


def pre_processing():
    data = pd.read_csv('Result/raw.csv', index_col=0)
    data = data.rename(columns={
        '睡觉点具体在哪里？请手动定位': '地址',
        '休息点是什么类型？': '类型',
        '旅店价格？': '旅店价格',
        '开放时间？': '开放时间',
        '是否有以下设施/功能': '设施/功能',
        '是否拥挤？': '拥挤程度',
        '环境条件如何？': '环境评分',
        '还有有什么需要备注的吗': '备注',
    })
    data.to_csv('Result/pre-processing.csv')
    return data


if __name__ == '__main__':
    save_from_clipboard()
    pre_processing()
