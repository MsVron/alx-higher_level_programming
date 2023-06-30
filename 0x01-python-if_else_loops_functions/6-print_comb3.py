#!/usr/bin/python3

output = []

for i in range(0, 10):
    for j in range(i+1, 10):
        output.append("{:02d}".format(i) + "{:02d}".format(j))

output_str = ", ".join(output)
print(output_str)
