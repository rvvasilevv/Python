days_of_championship=int(input())
points_needed_to_cover=int(input())
count_swimmers=int(input())
hotel_room_day_for_one=float(input())
participation_fee_for_one=float(input())
sum_of_fees_for_all=days_of_championship*(hotel_room_day_for_one*count_swimmers)+count_swimmers*participation_fee_for_one
first_day_points=float(input())
previous_day_points=first_day_points
obshtbroi=0
sponsorships_if_win=sum_of_fees_for_all*0.25
sponsorships_if_lose=sum_of_fees_for_all*0.1
count=0
while obshtbroi < points_needed_to_cover:
    count+=1
    if count not in range(0,days_of_championship):
        break
    points_for_each_day=float(input())
    obshtbroi+=first_day_points+points_for_each_day+(0.05*previous_day_points)
    previous_day_points=previous_day_points
if obshtbroi > points_needed_to_cover:
    sum_of_fees_for_all=sum_of_fees_for_all-sponsorships_if_win
    print(f"Money left to pay: {sum_of_fees_for_all:.2f} BGN.\nThe championship was successful!")

else:
    sum_of_fees_for_all=sum_of_fees_for_all-sponsorships_if_lose
    print(f"Money left to pay: {sum_of_fees_for_all:.2f} BGN.\nThe championship was not successful.")