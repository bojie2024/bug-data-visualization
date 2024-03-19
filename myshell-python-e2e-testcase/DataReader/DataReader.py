import openpyxl
import Utilities.disposition

# 表格操作
class Tableoperation:
    def __init__(self,test_data_file):
        self.wb = openpyxl.load_workbook(test_data_file)
        self.sheet = self.wb.worksheets[0]
    def read_excel(self):
        test_data_list = []
        # 用例编号列表
        testIDs = []  
        # 预期结果 
        expect = []
        for row in self.sheet.iter_rows(min_row=2):  # 假设第一行为标题头
            # 是否执行
            execute = row[4].value
            if execute == '1' or execute == 1:  # 确保execute可以正确地与整数或字符串"1"匹配
                # 获取用例编号，并添加到testIDs列表中 
                test_id_value = row[0].value  
                print(test_id_value)
                test_data_list.append(row)
                testIDs.append(test_id_value)  # 注意这里我们使用了小写字母d和s以区分变量名和值
                expect.append(row[3].value)
        return test_data_list,testIDs,expect
    def Save_excel(self,last_cell_coordinate,result):
        self.sheet[last_cell_coordinate] = result
        try:
            self.wb.save(Utilities.disposition.Fileaddress())   # 确保路径正确且文件没有被其他程序占用。
        except PermissionError:
            print("文件保存失败，请确保文件未被其他程序打开并且具有写入权限。")
        
