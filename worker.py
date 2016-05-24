import hashlib
from binascii import hexlify,unhexlify
import random
"""
header_hex = ("01000000" +
 "81cd02ab7e569e8bcd9317e2fe99f2de44d49ab2b8851ba4a308000000000000" +
 "e320b6c2fffc8d750423db8b1eb942ae710e951ed797f7affc8892b0f1fc122b" +

 "c7f5d74d" +
 "f2b9441a" +
 "42a14695")
header_bin = header_hex.decode('hex')
hash = hashlib.sha256(hashlib.sha256(header_bin).digest()).digest()
hash.encode('hex_codec')
'1dbd981fe6985776b644b173a4d0385ddc1aa2a829688d1e0000000000000000'
hash[::-1].encode('hex_codec')
'00000000000000001e8d6829a8a21adc5d38d0a473b144b6765798e61f98bd1d'
"""

def hash_it (c,v):
    input_string = c+v
    input_string_bin = unhexlify(input_string)
    hash = hashlib.sha256(hashlib.sha256(input_string_bin).digest()).digest()
    return str(hexlify(hash).decode('ascii'))

def gen_target (number_of_zeros):
    target = ''.join('0' for n in range(number_of_zeros))
    target = target + ''.join('f' for n in range(64-number_of_zeros))
    return target


#def find_proof (c,v):


#target_hexstr = "00000f"
#target =''.join('0' for n in range(5))
#target = target + ''.join('f' for n in range(59))
target = gen_target(5)
print("Target:  "+target)




random_number = ''.join(random.choice('0123456789abcdef') for n in range(64))

#print (target_hexstr)
#print (random_number)


while (str(hash_it(random_number,random_number)) > target):
    random_number = ''.join(random.choice('0123456789abcdef') for n in range(64))
    #print (random_number)

print ("Result:  " + hash_it(random_number,random_number))
print ("Answer:  " + random_number)