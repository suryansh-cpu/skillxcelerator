print("Enter the names of both players in different line")
player1 = str(input())
player2=str(input())
print(f"NAMES ENTERED ARE :{player1},{player2}")
player3 = player1
player1=player2
player2 = player3
print(f"NAMES AFTER SWAPPING ARE :{player1},{player2}")