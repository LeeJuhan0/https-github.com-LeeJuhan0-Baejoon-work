n = int(input())
card_list = []
card_list2 = []
for i in range(n):
    card_list.append(i+1)
card_list.reverse()    

def card2(card_list, card_list2):
    while len(card_list) + len(card_list2) > 1:
        if len(card_list) == 0 :
            card_list, card_list2 = card_list2, card_list
            card_list.reverse()
        if len(card_list) != 1:
            card_list.pop()
            card_list2.append(card_list.pop())
        else :
            card_list.pop()
            card_list, card_list2 = card_list2, card_list
            card_list.reverse()
            card_list2.append(card_list.pop())
    return card_list[0] if card_list else card_list2[0]

print(card2(card_list,card_list2))
