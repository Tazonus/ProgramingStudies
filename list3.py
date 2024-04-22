import re
ascii_table = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
brackets_open = "{[(<"
brackets_close = ">)]}"

#removing all brackets from ascii table
ascii_table = re.sub(brackets_open,'',ascii_table)
ascii_table = re.sub(brackets_close,'',ascii_table)

input = input("Write equation you want to check: \n")
brackets_only = re.sub(r"[\([{})\]]", "", input)

print(brackets_only)

#for x in input:
    