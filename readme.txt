# 使用python 将数据流整理成结构体对应数据

1. 将结构体填充到structs 文件中，数据类型和成员名需要且只能间隔一个空格
2. 将数据流填充到datafile文件中，用空格区分
3. 如果数据有大小端的问题，可以将exchange文件中的 tmp_data3 = big_little_endian_swap(tmp_data3)屏蔽打开