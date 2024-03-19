from selenium import webdriver
from time import sleep
import random
import DataReader.DataReader as DataReader 
import TestCases.testcase as testcase
from openpyxl.cell import Cell
import Utilities.disposition

def run_test_cases(test_data_file):
    #print(test_data_file)
    #获取表格操作
    Tableoperation_1 = DataReader.Tableoperation(test_data_file)
    test_data_list,testID,expect = Tableoperation_1.read_excel()
    #print(test_data_list) expect预期结果
    print(test_data_list)
    # 创建类的实例
    obj = testcase.testcase(test_data_file) 
    for index,data in enumerate(test_data_list):
        driver = webdriver.Chrome()
        print(f"当前是第{index}次循环, {data}!,{testID[index]}")
        try:
            # 获取列表最后一排位置
            print(data,'测试')
            whether = data[-1]
            if isinstance(whether, Cell):
                last_cell_coordinate = whether.coordinate  # 获取该单元格的坐标位置信息
            else:
                last_cell_coordinate = None                 # 如果不是，则设置为None    
            # 输出结果用于验证（根据实际情况决定是否需要）last_cell_coordinate 输入是否通过
            #print("最后一个单元格的坐标:", last_cell_coordinate)
            #method_name 获取用例编号 set转换为list并索引第0个位置
            method_name = list({testID[index]})[0]
            #print(method_name)
            # 使用getattr来获取method_name对应的方法对象，并执行它
            method_to_call = getattr(obj, method_name)
            if callable(method_to_call):  # 检查是否可调用
                method_to_call(driver,last_cell_coordinate,expect[index])   # 调用该方法   expect[index]预期结果
        finally:
            driver.quit()

if __name__ == "__main__":
    test_data_file = Utilities.disposition.Fileaddress()
    run_test_cases(test_data_file)
