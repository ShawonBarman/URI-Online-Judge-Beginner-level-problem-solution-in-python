import struct
a,b,c,d = map(str,input().split(' ',3))
b = struct.unpack('f', struct.pack('f', float(b)))[0]
print('%d%.6f%c%s'%(int(a), float(b), c, d))
print('%d\t%.6f\t%c\t%s'%(int(a), float(b), c, d))
print('%10d%10.6f%10s%10s'%(int(a), float(b), c, d))
