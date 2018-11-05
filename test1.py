import xlsxwriter

workbook = xlsxwriter.Workbook('demo.xlsx')
worksheet = workbook.add_worksheet()

worksheet.set_column('A:A',20)

bold = workbook.add_format({'bold':True})
worksheet.write('A1','Hello')
worksheet.write('A2','world',bold)

worksheet.write(2,0,'hello world')

# worksheet.insert_image('B5','bd_logo1.png')

workbook.close()