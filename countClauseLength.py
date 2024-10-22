import matplotlib.pyplot as plt
import collections

# 读取文件中的字符串
def read_strings_from_file(file_path):
    strings = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            strings.append(line.strip())
    return strings

# 统计不同长度字符串的数量
def count_string_lengths(strings):
    lengths = [len(s) for s in strings]
    counter = collections.Counter(lengths)
    return counter

# 计算占比
def calculate_percentages(counts, total):
    return {k: v/total for k, v in counts.items()}

file_path = 'wiki2019.txt'
strings = read_strings_from_file(file_path)
length_counts = count_string_lengths(strings)
total_strings = len(strings)
percentages = calculate_percentages(length_counts, total_strings)

# 准备绘图数据
sorted_lengths = sorted(percentages.keys())
percentages_values = [percentages[l] for l in sorted_lengths]

# 绘制柱状图
plt.bar(sorted_lengths, percentages_values)
plt.xlabel('字符串长度')
plt.ylabel('占比')
plt.title('不同长度字符串占比')
plt.show()