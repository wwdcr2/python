# -*- coding: utf-8 -*-
# 함수 사용
# max, min
print(max(1,3,5,7,9))
print(min(1,3,5,7,9))
print(sum([1,3,5,7,9])) #sum은 [] 배열형태로

print(pow(2,2)) #거듭제곱
print(divmod(9,4))

#반올림
print(round(2.567,2)) # = 2.57
print(round(2.564,2)) # = 2.56 

print(bin(10))
print(bin(0o12))

#실습 
print(max(32,45,48,57,84)) # 이중 큰값
print(min(32,45,48,57,84)) # 이중 작은값
print(sum(32,45,48,57,84)/5) # 평균
print(divmod(45,32)) # divmod 실습
print(pow(max(3,4,8,5),min(3,4,8,5))) # 3,4,8,5중 큰수를 작은수만큼 제곱
print("%d" % 0x3d5f) # 0x3d5f -> 10진수
print("%x" % 1024) # 1024 -> 16진수  
print(format(0x35,'b')) #0x35 -> 2진수
print("%d" % 0o35) # 0o35 -> 16진수
print("%x" % (3452+5785)) #해당값 -> 16진수
print(format((0xAC+200),'b')) #해당값 -> 2진수


#다시 수업
print('%-10s%-10s%-10s' % ('name','age','address'))

print(bin(192)+"."+bin(168)+"."+bin(108)+"."+bin(11)) # 192.168.108.11 이진수 출력
print(bin(192),bin(168),bin(108),bin(11),sep='.')
    #윗 문제 강사님 힌트 = print('{:b}'.format(10진수)) => 2진수 8바이트 출력 (8바이트 넘을시 알맞게 출력)
print(('{:08b}'.format(192)),('{:08b}'.format(168)),('{:08b}'.format(108)),('{:08b}'.format(11)),sep='.')

print('{5}{4}{3}{2}{1}{0}'.format('The','famine','was','severe','in','Samaria')) #거꾸로 출력