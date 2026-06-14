p1 = "CLick this"
p2 = "Buy now"
p3 = "Make money"
p4 = "Subscribe"

message = input("Comment here:-")

if((p1 in message or (p2 in message) or (p3 in message) or (p4 in message))):
    print("This is a SPAM comment !!")
else:
    print('This is not a spam..')