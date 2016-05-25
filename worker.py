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


def hash_it(chain, value):
    input_string = chain + value
    input_string_bin = unhexlify(input_string)
    result = hashlib.sha256(hashlib.sha256(input_string_bin).digest()).digest()
    return str(hexlify(result).decode('ascii'))


def gen_target(number_of_zeros):
    target = ''.join('0' for n in range(number_of_zeros))
    target = target + ''.join('f' for n in range(64-number_of_zeros))
    return target


def find_proof_of_work(chain,number_of_zeros):
    target = gen_target(number_of_zeros)
    random_number = ''.join(random.choice('0123456789abcdef') for n in range(64))
    while hash_it(chain, random_number)>target:
        random_number = ''.join(random.choice('0123456789abcdef') for n in range(64))
    return random_number


chain = ''.join(random.choice('0123456789abcdef') for n in range(64))

answer = find_proof_of_work(chain,5)

print('random: ' + chain)
print('answer: ' + answer)
print('hash:   ' + hash_it(chain, answer))

