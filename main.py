import gzip
import json
import csv
import os
import pandas as pd

# 0) save as a separate file only domains
# 1) Rule 1 : if domain consist $  ptinr 1
# 2) Rule 2: if domain consist more than 5 "."
# 3) Rule 3: if domain is an IP (<12 numbers)
# 4) Rule 4 if domain consist “login” and “registered
# 5) Rule 5: if domain greater that 54 lenght
# 6) split the data to 70/30 and name 70% - train_data,
#    30%-test_data and add new variable result as an output (0/1) ontly to train data
# 7) if domain has more than 3 yes to rules (>=3 "1" ) put "1" to result if no, else put "0"
# 8) convert all data to csv file

def my_analytics(domain):
    weird_symbols_flag = "$" in domain
    dots_5numbers_flag = domain.count(".") >= 5
    defis_2number_flag = domain.count("-") >= 3
    ip_flag = any(len(s) <= 12 and s.isnumeric() for s in domain.split("."))
    num_flag = any(len(s) <= 20 and s.isnumeric() for s in domain.split("-"))
    num_nosplit_flag = any(len(s) <= 12 and s.isnumeric() for s in domain)
    # поиск по словам
    weird_word_flag = any(s in ['login', 'registered', '$', '!', '%'] for s in domain.split("."))
    length = len(domain) >= 40
    # dot_com_flag = domain.endswith('.com')


    analitycs_write.writerow([domain, int(weird_symbols_flag), int(dots_5numbers_flag),
                              int(ip_flag), int(weird_word_flag), int(length), int(num_flag),
                              int(num_nosplit_flag), int(defis_2number_flag)])
    global count_rows_max
    count_rows_max +=1

    #  data_flag: 1/0
    # domain, 1,0,0,0,  1   for train_csv
    # domain, 1,0,0,0,      for test_csv

    # with open("domains_analytics.csv", 'a') as csv_file:


    # ip_flag = False
    # for s in domain.split("."):
    #     if len(s) <= 12 and s.isnumeric():
    #         ip_flag = True
    #         break

csv_file = open("domains_analytics.csv", 'w+')
analitycs_write = csv.writer(csv_file)
analitycs_reader = csv.reader(csv_file)

csv_file30 = open("finance_test20.csv", 'w')
test30_write = csv.writer(csv_file30)

csv_file70 = open("finance_train80.csv", 'w')
test70_write = csv.writer(csv_file70)

# try:
#     os.unlink('domains_analytics.csv')
# except FileNotFoundError:
#     pass
count_rows_max = 0
MAXLINES = 100000
domains_data = []
line_number = 0
with gzip.open('ctl_records_sample.jsonlines — копия.gz', mode='rt') as my_data:
    for line in my_data:
        cert = json.loads(line)
        domains = cert['data']['leaf_cert']['all_domains']
        for domain in domains:
            my_analytics(domain)
            # s = domain.split('.')
            # print(domain)
            # domains_data.setdefault(0, domain)
            # domains_data[domain] += 1
            # line_number += 1
            # print(domains_data)

            # if 'apple' in s:
            #     print(domain)
        line_number += 1
        if line_number > MAXLINES:
            break



csv_file.seek(0)

last30_percents = round(count_rows_max*0.2)
first70_percents = count_rows_max - last30_percents


for i in range(first70_percents):
    row = next(analitycs_reader)
    row.append(int(row.count('1')>=1))
    test70_write.writerow(row)

for i in range(last30_percents):
    row = next(analitycs_reader)
    test30_write.writerow(row)


data = pd.read_csv('finance_train80.csv')
pass



