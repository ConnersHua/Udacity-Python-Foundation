"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
任务3:
(080)是班加罗尔的固定电话区号。
固定电话号码包含括号，
所以班加罗尔地区的电话号码的格式为(080)xxxxxxx。

第一部分: 找出被班加罗尔地区的固定电话所拨打的所有电话的区号和移动前缀（代号）。
 - 固定电话以括号内的区号开始。区号的长度不定，但总是以 0 打头。
 - 移动电话没有括号，但数字中间添加了
   一个空格，以增加可读性。一个移动电话的移动前缀指的是他的前四个
   数字，并且以7,8或9开头。
 - 电话促销员的号码没有括号或空格 , 但以140开头。

输出信息:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
代号不能重复，每行打印一条，按字典顺序排序后输出。

第二部分: 由班加罗尔固话打往班加罗尔的电话所占比例是多少？
换句话说，所有由（080）开头的号码拨出的通话中，
打往由（080）开头的号码所占的比例是多少？

输出信息:
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
注意：百分比应包含2位小数。
"""

# 第一部分

area_code = []

for call in calls:
    num_from=call[0]
    num_to=call[1]
    if num_from[0:5]=="(080)":
        if num_to[0:2]=="(0" and num_to[1:str(num_to).find(")")] not in area_code:
            area_code.append( num_to[1:str(num_to).find(")")] )
        elif num_to[0] in ["7","8","9"] and str(num_to).find(" ") != -1 and num_to[0:4] not in area_code:
            area_code.append(num_to[0:4])

result = '\n'.join(filter_code for filter_code in sorted(area_code))

print("The numbers called by people in Bangalore have codes: \n" + result )

# 第二部分

def percent_final():
    callers = 0
    receivers = 0
    for c in calls:
        if c[0][:5] == '(080)':
            callers += 1
        if c[0][:5] == '(080)' and c[1][:5] == '(080)':
            receivers += 1
    percent = round((receivers/callers*100), 2) #round down to 2 decimal digits
    return str(percent)

print(percent_final() + " percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")