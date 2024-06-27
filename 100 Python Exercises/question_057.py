# Write a program to read an ASCII string and to convert it to a unicode string
# encoded by utf-8.

string = input()
print(string)
utf8_string = string.encode('utf-8')
print(utf8_string)
