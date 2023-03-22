"""어느 꽃집의 장미 가격은 1송이 5000원, 튤립 1송이 6500원, 해바라기 1송이 4200원이고,
10송이 이상을 사거나 혹은 50000원 이상을 사면 10% 할인을 해준다."""

# test1: 장미 5송이, 튤립 2송이를 구매했을 때 총액은?
# test2: 튤립 10송이를 구매했을 때 총액은?
# test3: 장미 3송이, 튤립 3송이, 해바라기 3송이를 구매했을 때 총액은?

rose = int(input("장미 구매 개수: "))
tulip = int(input("튤립 구매 개수: "))
sunflower = int(input("해바라기 구매 개수: "))
total_number = rose + tulip + sunflower
total_price = rose*5000 + tulip*6500 + sunflower*4200

if (total_number >= 10) or (total_price >= 50000) :
    total_price = total_price*0.9

print("총액은 {0}원 입니다.".format(int(total_price)))
