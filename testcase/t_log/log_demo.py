import logging
#固定格式 %（）s asctime时间，name名称，levelname日志级别，message打印的信息
import os

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(name)s %(levelname)s %(message)s')
#获取当前目录  /Users/wangwang/Documents/Test_Pytest/Pytest_W1/testcase/t_log/log_demo.py
path_abspath = os.path.abspath(__file__)
logger = logging.getLogger(path_abspath)
#日志级别 debug info  warning
logger.info("this is info")
logger.debug("debug")
logger.warning("warning")