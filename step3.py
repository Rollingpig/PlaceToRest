"""

"""

import pandas as pd


def final_processing():
    data = pd.read_csv('Result/coord.csv', index_col=0)
    data = data.drop(columns=['提交时间', '填写ID', '答题时间', '昵称'])
    data.to_csv('Result/休息点.csv', index=False)
    return None


if __name__ == '__main__':
    final_processing()
