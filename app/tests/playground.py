from pypykatz.pypykatz import pypykatz
from base64 import b64decode

# dump lsass memory
lsass:bytes = b64decode(open('./lsass.b64', 'r').read())
print(pypykatz.parse_minidump_bytes(lsass).to_json())

"""
NFO:pypykatz:Parsing file lsass.DMx
ERROR:pypykatz:Minidump parsing error!
Traceback (most recent call last):
  File "/home/br00x/.local/lib/python3.10/site-packages/pypykatz/pypykatz.py", line 139, in parse_minidump_file
    minidump = MinidumpFile.parse(filename)
  File "/home/br00x/.local/lib/python3.10/site-packages/minidump/minidumpfile.py", line 48, in parse
    mf.file_handle = open(filename, 'rb')
FileNotFoundError: [Errno 2] No such file or directory: 'lsass.DMx'
ERROR:pypykatz:Error while parsing file lsass.DMx
Traceback (most recent call last):
  File "/home/br00x/.local/lib/python3.10/site-packages/pypykatz/lsadecryptor/cmdhelper.py", line 260, in run
    mimi = pypykatz.parse_minidump_file(args.memoryfile, packages=args.packages)
  File "/home/br00x/.local/lib/python3.10/site-packages/pypykatz/pypykatz.py", line 144, in parse_minidump_file
    raise e
  File "/home/br00x/.local/lib/python3.10/site-packages/pypykatz/pypykatz.py", line 139, in parse_minidump_file
    minidump = MinidumpFile.parse(filename)
  File "/home/br00x/.local/lib/python3.10/site-packages/minidump/minidumpfile.py", line 48, in parse
    mf.file_handle = open(filename, 'rb')
FileNotFoundError: [Errno 2] No such file or directory: 'lsass.DMx'
Traceback (most recent call last):
  File "/home/br00x/.local/lib/python3.10/site-packages/pypykatz/lsadecryptor/cmdhelper.py", line 260, in run
    mimi = pypykatz.parse_minidump_file(args.memoryfile, packages=args.packages)
  File "/home/br00x/.local/lib/python3.10/site-packages/pypykatz/pypykatz.py", line 144, in parse_minidump_file
    raise e
  File "/home/br00x/.local/lib/python3.10/site-packages/pypykatz/pypykatz.py", line 139, in parse_minidump_file
    minidump = MinidumpFile.parse(filename)
  File "/home/br00x/.local/lib/python3.10/site-packages/minidump/minidumpfile.py", line 48, in parse
    mf.file_handle = open(filename, 'rb')
FileNotFoundError: [Errno 2] No such file or directory: 'lsass.DMx'



"""