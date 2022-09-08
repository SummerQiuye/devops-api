import csv
import pandas as pd

totalRow = []

# df = pd.read_csv('./读请求命中率.csv')
# for index, row in df.iterrows():
#     # x, y = row[0], row[1]
#     # print()
#     print(row[2])

with open('./读请求命中率.csv', 'r', encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)

    # 遍历所有行并取出指定列
    for i in range(26):
        print("e")
        column = [row[i] for row in reader]

        print(column)
        while "null" in column:
            column.remove("null")
        name = column[0]
        column.pop(0)
        # str转float类型
        for toFloat in range(0, len(column)):
            column[toFloat] = float(column[toFloat])
        # 统计总值求平均值
        countTotal = 0
        for j in range(0, len(column)):
            countTotal += float(column[j])
        print("avg:", round(countTotal/len(column), 2))
        print("max:", max(column))
        print("min", min(column))
        # print(column)
        totalRow.append([name, str(round(countTotal/len(column), 2)), str(max(column)), str(min(column))])
        # print(row)
        # 将分析后数据写入新csv数据表

with open('./mem.csv', 'w', newline='') as csvWriteFile:
    write = csv.writer(csvWriteFile)
    write.writerows(totalRow)
