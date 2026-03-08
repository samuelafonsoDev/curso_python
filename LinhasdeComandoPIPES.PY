import os
filename = 'introducao.txt'
cmd = 'md5sum' + filename
fp = os.popen(cmd)
resp = fp.read()
stat = fp.close()
print(resp)
print(stat)