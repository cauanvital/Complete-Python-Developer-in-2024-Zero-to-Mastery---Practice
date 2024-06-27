# Please write a program to compress and decompress the string
# "hello world!hello world!hello world!hello world!".

from zlib import compress, decompress

string = b'hello world!hello world!hello world!hello world!'
compress_str = compress(string)

print(compress_str)
print(decompress(compress_str))
