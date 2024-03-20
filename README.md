# cypress 无法使用 使用cypress打开主站直接会被拦截 无法通过人机认证
# Python + Selenium相对于其他自动化测试工具的优势和劣势：
## 优势
- **易学易用**：
  Python语法简洁直观，适合各个水平层次的开发者快速上手。
- **丰富的库支持**：
  Python有大量成熟的第三方库如Pandas、NumPy等，非常适合处理数据驱动所需的复杂数据操作。
- **跨平台性**：
  可在Windows、Linux和macOS等多种操作系统中无缝运行。
- **浏览器兼容性好**：
  Selenium提供了广泛的浏览器支持，并能模拟真实用户界面交互。
- **社区活跃**：
  遇到问题时可以从庞大而活跃的社区获得帮助和资源。
## 劣势
- **执行效率**： 
   相比编译型语言（如Java），解释型语言Python可能在执行效率上略显不足。
- **资源消耗较高**： 
   Selenium通过启动真实浏览器进行测试，与基于DOM或Headless 浏览器相比，在资源占用方面可能更高。
- **调试难度较高**： 
   当遇到涉及页面交互特别是异步加载内容时，调试Selenium脚本可能会比较困难。

# 框架介绍
- **测试用例（Test Cases）**：
  具体描述了每个测试场景的步骤和预期结果。
- **页面对象（Page Objects）**：
  将与页面元素交互封装起来，使得代码更易维护。
- **数据驱动组件（DataReader）**：
  负责提供参数化数据给到测试用例。
- **工具/服务层（Utilities/Services Layer）**：
  提供日志、配置管理等支持功能。
- **报告层（Reporting Layer）**：
  生成可视化的测试报告以便回顾结果。
- **执行层（Carryout）**：
  执行整个测试用例运行。
  
# 使用方法 
## 安装python
### 访问Python官方网站：https://www.python.org/。
## 安装Selenium库：确保已经安装了Selenium库以及对应的WebDriver。
### pip install selenium
## 使用excel表格操作测试用例是否执行
![image](https://github.com/myshell-ai/qa/assets/140363121/e85076bf-9c02-46d7-a934-b84459b31944)
- **编号-重要**：
测试用例实际运行是：根据编号来调用对应的测试用例步骤。 编号不要重复。名称需要与 Test Cases 方法名称保持一致！(不然找不到测试步骤)
- **用例名称**：
该条用例的验证名称
- **模块**：
该条用例所在的模块
- **预期结果-重要**：
写入预期结果 断言时会调用该处预期结果与页面的实际结果做对比。
- **是否执行(1/2)**：
1为需要执行 2或者其他值为无需执行
- **验证是否通过(T/F)**：
无需认为修改里面任何值 用例验证通过输入T 用例验证通过输入F

## testcase 测试用例(步骤/判断用例是否通过)
![image](https://github.com/myshell-ai/qa/assets/140363121/bce1cb41-b26a-4ef6-b41f-570b6b3a95eb)
### 添加新的测试用例方法
 ```python
# expect 表格的预期结果  last_cell_coordinate 当前测试用例是否通过的表格位置 用来保存用例通过状态
def XXX (self,driver,last_cell_coordinate,expect):  #xxx 方法名称需要与excel表格编号名称保持一致 不然运行时找不到对应的测试用例步骤
        try:
            #具体测试步骤
        except Exception as e:
            print(e)
             #断言或者上方用例元素找不到导致用例未通过 标记用例状态
 ``` 
## Carryout 执行整个测试自动化运行 重要（执行过程中不要打开excel表格）
### 直接运行该文件 开始运行

