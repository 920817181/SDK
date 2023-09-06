import re
from collections import OrderedDict

endian_swap_enable =  1
output_hex = 1

with open('structs.txt', 'r', encoding='utf-8') as f1:
    tmp_data = f1.readlines()
    # 去掉第一行和最后一行，根据结构体文件格式自行调整
    format_data1 = tmp_data[1:len(tmp_data)-1]
    # 去掉换行符
    format_data = [x.strip() for x in format_data1]

with open('datafile.txt', 'r', encoding='utf-8') as f2:
    # 假设数据以txt存储，读取数据内容
    data = f2.read()


def extract_numbers(input_string):
    # 使用正则表达式匹配数字的模式
    pattern = r'\d+'
    # 使用findall方法查找所有匹配的数字
    numbers = re.findall(pattern, input_string)
    # 将字符串形式的数字转换成整数，并返回结果
    tmp = [int(num) for num in numbers]
    return tmp[0]


def big_little_endian_swap(original_string):
    # 拆分原始字符串，并去除空白项
    parts = original_string.split()
    parts = [part for part in parts if part.strip()]

    # 反转列表中的元素
    reversed_parts = parts[::-1]

    # 将元素重新连接成字符串，使用空格分隔
    modified_string = " ".join(reversed_parts)
    return modified_string


# 数据结果解析
res = OrderedDict()
index = 0  # 索引记录，用于定位数据从哪开始解析
for f in format_data:
    tmp_data2 = f.split(" ")
    # 取出变量名
    name = tmp_data2[1].replace(";", "")
    # 取出字段定义
    content = tmp_data2[0]
    # 获取成员的数据类型
    data_size = int(extract_numbers(content))//8
    # 将对应位置的数据提取出来
    tmp_data3 = data[index: index + (data_size * 3)]
    # 大小端转换，根据需求进行开启或屏蔽
    if endian_swap_enable == True:
        tmp_data3 = big_little_endian_swap(tmp_data3)

    if output_hex == 1:
        # 输出16进制数据 
        res.update({name: tmp_data3.replace(" ", "")})
    else:    
        # 输出10进制数据
        res.update({name: int(tmp_data3.replace(" ", ""), 16)})



    # 每次处理后增加字符串偏移量
    index += (data_size*3)

with open('res.txt', 'w+', encoding='utf-8') as f3:
    for k, v in res.items():
        f3.write('{0:<40}:{1:<10}\n'.format(k, v))
