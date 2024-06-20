# -*- coding: utf-8 -*-

source_list = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]

for source_item in source_list:
    print(source_item)

for idx in range(len(source_list)):
    print(idx, source_list[idx])

for idx, source_item in enumerate(source_list):
    print(idx, source_list[idx])


zfill_list = [
    str(source_item).zfill(4)
    for source_item in source_list
]
print(f"zfill_list: {zfill_list}")
