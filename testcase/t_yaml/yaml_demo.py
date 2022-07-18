""
#创建yaml格式文件
#读取这个文件
#输出这个文件
""
#2、读取单个文件
import yaml
# #打开
# #encoding="utf-8" 中文乱码
#
# with open("./data.yml", "r", encoding="utf-8") as f:
#     #读取
#     r=yaml.safe_load(f)
#     #输出
#     print(r)
#

#2、2读个多个文档
#1、编辑修改data.yml
#2、all
# #3、循环输出
# with open("./data.yml", "r", encoding="utf-8") as f:
#     r = yaml.safe_load_all(f)
#     for i in r:
#         print(i)
from  utils.YamlUtil import YamlReader
#单个
# res = YamlReader("./data.yml").data()
# print(res)
#多个
res = YamlReader("./data.yml").data_all()
print(res)