import gzip
import json
MAXLINES = 20_000
res = {}
line_number = 0
with gzip.open('ctl_records_sample.jsonlines — копия.gz', mode='rt') as my_data:
    for line in my_data:
        # print(line_number)
        cert = json.loads(line)
        fingerprint = cert['data']['leaf_cert']['fingerprint']
        # print(fingerprint)
        res.setdefault(fingerprint, 0)
        res[fingerprint] += 1
        line_number += 1
        if line_number > MAXLINES:
            break


for fingerprint in (key for key, value in res.items() if value > 1):
     print(fingerprint)

dupl = {}
line_number = 0
with gzip.open('ctl_records_sample.jsonlines — копия.gz', mode='rt') as my_data:
    for line in my_data:
        # print(line_number)
        cert = json.loads(line)
        leaf_cert = cert['data']['leaf_cert']
        fingerprint = cert['data']['leaf_cert']['fingerprint']
        # print(fingerprint)
        if res[fingerprint] > 1:
            dupl.setdefault(fingerprint, [])
            dupl[fingerprint].append(leaf_cert)
        line_number += 1
        if line_number > MAXLINES:
            break

for fingerprint, certs in dupl.items():
    print(fingerprint, len(certs), certs)

with open('Dublicated fingerprints.json', 'w') as json_file:
         json.dump(dupl, json_file)





