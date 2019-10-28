import sys
import os
import csv

# get csv filename
csv_file = sys.argv[1]

# make result filename
filename, file_extension = os.path.splitext(csv_file)
result_file = filename+'CSV_結果.txt'

with open(csv_file, encoding="ms932") as csv_file:
    with open(result_file,  encoding="ms932", mode='w') as result_file: 
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        section = ''
        for row in csv_reader:
            if "：" in row:
                p = row.index("：")
                if row[0]: section = row[0]
                if '件名' in section:
                    print(f'{row[0]} : {row[p+1]}')
                    result_file.write(f'件名 : {row[p+1]}')
                if '補足' in section:
                    print(f'{row[0]} : {row[p+1]}')
                    result_file.write(f'row[0] : {row[p+1]}')

            if '名称仕様' in row[1]:
                section = '名称仕様'
                continue
            
            if '名称仕様' in section:
                print(f'{row[0]}: {row[1]} , {row[6]}')
                result_file.write(f'{row[0]}: {row[1]} , {row[6]}')                    
          
            line_count += 1
        print(f'Processed {line_count} lines.')

