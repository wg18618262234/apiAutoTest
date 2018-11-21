import xlrd
import xlwt
import tkinter.filedialog
import os

flag = True
fname = ''


class excel:
    def read_excel(self, row):
        global flag, fname
        try:
            # 文件对话框
            if flag:
                default_dir = '文件路径'
                fname = tkinter.filedialog.askopenfilename(title='选择文件', initialdir=(os.path.expanduser((default_dir))))
                flag = False
        except:
            print('error:选取文件异常')

        # 读取excel
        workbook = xlrd.open_workbook(fname)
        # 获取所有sheet
        # print(workbook.sheet_names())
        # sheet2_name = workbook.sheet_names()[1]

        # 根据sheet索引或者名称获取sheet内容
        sheet = workbook.sheet_by_index(0)
        # sheet = workbook.sheet_names('sheet1')

        # sheet的名称，行数，列数
        # print(sheet.name, sheet.nrows, sheet.ncols)

        # 获取整行和整列的值（数组）
        try:
            rows = sheet.row_values(row)  # 获取row内容
        except:
            print('error:%d行内容为空' % (row + 1))
            return False
        # cols = sheet.col_values(0)  # 获取第一列内容
        # print(rows)
        # print(cols)

        # 获取单元格内容
        # print(sheet.cell(1, 5).value)

        # 获取单元格内容的数据类型
        # print(sheet.cell(1, 5).ctype)
        return rows


if __name__ == '__main__':
    a = excel()
    for i in range(5):
        if a.read_excel(i) == False:
            break
        print(a.read_excel(i))
