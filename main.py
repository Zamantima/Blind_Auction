from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)

print("Welcome to the Secret Auction.")
bidders_dict = {}

def bidding():
  Bidder_Name = input("What is your name? ")
  Bid = int(input("What is your bid? R"))
  bidders_dict[Bidder_Name] = Bid

bidding()

Other_Bidder = input(
    "Are there any other bidders?. Type Y for Yes or N for No ")
while (Other_Bidder == 'Y') or (Other_Bidder == 'y') :
  clear()
  bidding()
  Other_Bidder = input(
    "Are there any other bidders?. Type Y for Yes or N for No \n")

clear()

#bid_list = []
max_bid = 0
for bid in bidders_dict:
  bid_amount = bidders_dict[bid]
  if bid_amount > max_bid:
    max_bid = bid_amount
    winner = bid
print(f"The winner is {winner} with a bid of R{max_bid}")
 # bid_list.append(bidders_dict[bid])


#highest_bid = max(bid_list)
#print(f"Highest bid is {highest_bid}")

#for bidders in bidders_dict:
 # if highest_bid == bidders_dict[bidders]:
 #   print(f"Highest bidder is {bidders} with a bid of R{highest_bid}")
    
#print(bidders_dict)