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
任务0:
短信记录的第一条记录是什么？通话记录最后一条记录是什么？
输出信息:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

texts_content = "First record of texts, {} texts {} at time {}".format(texts[0][0],texts[0][1],texts[0][2])
print(texts_content)

calls_content = "Last record of calls, {} calls {} at time {}, lasting {} seconds".format(calls[-1][0],calls[-1][1],calls[-1][2],calls[-1][3])
print(calls_content)