
import logging

#输出控制台

#1、设置longger名称
logger = logging.getLogger("log_file_demo")
#2、设置log级别
logger.setLevel(logging.DEBUG)
#3、创建handler
#写入控制台
handler = logging.StreamHandler()
#写入文件
filehandler = logging.FileHandler("./test1.log")
#4、设置日志级别
handler.setLevel(logging.INFO)
filehandler.setLevel(logging.DEBUG)
#5、定义输出格式
formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
handler.setFormatter(formatter)
filehandler.setFormatter(formatter)
#6、添加hannler
logger.addHandler(handler)
logger.addHandler(filehandler)

#7、运行输出
logger.info("this info")
logger.debug("this debug")
logger.warning("this warning")


