from time import sleep
import DataReader.DataReader as DataReader 
import unittest

#测试用例
class testcase(unittest.TestCase):
    def __init__(self, test_data_file, *args, **kwargs):
        super(testcase, self).__init__(*args, **kwargs)
        self.data_reader = DataReader.Tableoperation(test_data_file)
    def test001(self,driver,last_cell_coordinate,expect): #验证游客模式无法进入工坊
        try:
            driver.get("https://app.myshell.ai/zh/explore")
            sleep(4)
            # 点击工坊页
            driver.find_element('xpath', '/html/body/div[1]/main/aside/div[2]/nav/div/div[2]/a[3]').click()
            sleep(5)
            text_of_element = driver.find_element('xpath', '/html/body/div[3]/div[3]/div/section/div/p').text
            print(text_of_element) 
            # 断言：比较实际文本与预期文本是否一致。
            self.assertEqual(expect,text_of_element,"元素的文本与期望值不匹配。")
            print('new3')
            # 如果成功，则保存结果到Excel文件中，并标记‘T’（通过）。
            self.data_reader.Save_excel(last_cell_coordinate,'T')
            sleep(5)
        except Exception as e:
            print(e)
            self.data_reader.Save_excel(last_cell_coordinate,'F')
            sleep(5)
    def test002(self,driver,last_cell_coordinate,expect): #验证个人中心无法进入工坊
        try:
            driver.get("https://app.myshell.ai/")
            sleep(4)
            # 点击个人中心
            driver.find_element('xpath', '/html/body/div[1]/main/aside/div[2]/nav/div/div[2]/a[5]').click()
            sleep(5)
            text_of_element = driver.find_element('xpath', '/html/body/div[3]/div[3]/div/section/div/p').text
            print(text_of_element) 
            # 断言：比较实际文本与预期文本是否一致。
            self.assertEqual(expect,text_of_element,"元素的文本与期望值不匹配。")
            print('new3')
            # 如果成功，则保存结果到Excel文件中，并标记‘T’（通过）。
            self.data_reader.Save_excel(last_cell_coordinate,'T')
            sleep(5)
        except Exception as e:
            print(e)
            self.data_reader.Save_excel(last_cell_coordinate,'F')
            sleep(5)