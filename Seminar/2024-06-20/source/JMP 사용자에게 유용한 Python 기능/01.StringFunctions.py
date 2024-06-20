# -*- coding: utf-8 -*-
import re

source_text = "Hello, JMP-Python!"
print(f"source_text: {source_text}")

source_length = len(source_text)
print(f"source_length: {source_length}")

substr_text = source_text[8:]
print(f"substr_text: {substr_text}")

new_source_text = source_text + " Python!"
# new_source_text = f"{source_text} Python!"
print(f"new_source_text: {new_source_text}")

split_text_list1 = new_source_text.split(", ")
split_text_list11 = re.split(",| ", new_source_text)
split_text_list2 = new_source_text.split(",")
print(f"split_text_list1: {split_text_list1}")
print(f"split_text_list11: {split_text_list11}")
print(f"split_text_list2: {split_text_list2}")

joined_text = ", ".join(split_text_list1)
# joined_text = ",".join(split_text_list2)
print(f"joined_text: {joined_text}")

replace_text1 = new_source_text.replace("Python", "PYTHON")
replace_text2 = new_source_text.replace("Python", "PYTHON", 1)
print(f"replace_text1: {replace_text1}")
print(f"replace_text2: {replace_text2}")


upper_text = source_text.upper()
print(f"upper_text: {upper_text}")

lower_text = source_text.lower()
print(f"lower_text: {lower_text}")

cap_text = source_text.capitalize()
print(f"cap_text: {cap_text}")

title_text = source_text.title()
print(f"title_text: {title_text}")

swap_text = title_text.swapcase()
print(f"swap_text: {swap_text}")

strip_text = f"  {source_text}  ".strip()
print(f"strip_text: {strip_text}")


is_starts_with = source_text.startswith("Hello")
print(f"is_starts_with: {is_starts_with}")

is_ends_with = source_text.endswith("Python!")
print(f"is_ends_with: {is_ends_with}")
