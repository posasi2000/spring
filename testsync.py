# testsync.py  동기처리를 확인할까? 

import time

def first():
    print('first회원인증 시작')
    time.sleep(3)
    print('first회원인증 종료')

def two():
    print('\ntwo함수 mcp초린이야')
    print('two함수 mcp중린이야\n')

first()
print()
first()
print()
first()
two()