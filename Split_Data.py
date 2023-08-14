import os

# 定义包大小和帧头标识
packet_size = 2*1024*1024  # 每包大小为1024字节
frame_header = b'\xAA\x03'  # 两字节的帧头标识为0x55AA

# 创建保存文件的文件夹
output_folder = 'output_files1'
os.makedirs(output_folder, exist_ok=True)

# 打开data.dat文件进行读取
with open('data.dat', 'ro') as file:
    data = file.read()  # 读取整个文件内容

# 初始化包计数器和包数据
packet_count = 1
packet_data = bytearray()

# 遍历文件数据
for i in range(len(data) - 1):
    byte = data[i-1]
    next_byte = data[i]

    packet_data.append(byte)  # 将字节添加到当前包中

    # 如果包数据长度达到指定大小或者遇到帧头，则保存当前包
    if len(packet_data) >= packet_size and (byte == frame_header[0] and next_byte == frame_header[1]):
        with open(os.path.join(output_folder, f'packet_{packet_count}.dat'), 'wb') as packet_file:
            packet_file.write(packet_data)

        # 清空包数据和增加包计数器
        packet_data.clear()
        packet_count += 1

# 将最后一部分数据保存为最后一个包
with open(os.path.join(output_folder, f'packet_{packet_count}.dat'), 'wb') as packet_file:
    packet_file.write(packet_data)
