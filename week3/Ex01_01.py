# 12345초는 몇 시간 몇 분 몇 초?

time = 12345
hour = time//3600
minute = (time - hour*3600)//60
second = time - hour*3600 - minute*60

print('%d시간 %d분 %d초 입니다.' hour, minute, second)
