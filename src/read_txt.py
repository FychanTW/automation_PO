from trello import TrelloClient
import os
client = TrelloClient(
    api_key = '--------',
    token='-------'
)
path = os.getcwd()

f = open(".\\extract2.txt",'r',encoding='UTF-8')
datalist = f.readlines()
for data in datalist[0:10]:
    if data[0:4]=='発注番号':
        print('the PO number is:',data[-12:])
        PO_Number = data[-12:]
all_board = client.list_boards()
print(all_board)
BOARD_ID = all_board[0].id
print(BOARD_ID)
last_board = all_board[-1]
print(last_board.name)
board = client.get_board(BOARD_ID)
lists = board.all_lists()
all_list = last_board.list_lists()
print(all_list)
PO_LIST_ID = all_list[0].id
target_list=board.get_list(PO_LIST_ID)
#created_card= target_list.add_card(str(PO_Number),"auto_made",position="top")
cards = board.get_cards()
for card in cards:
    print(card.name,"is",card.id)
#cards[0].set_description("mimeType = \"application/pdf\"")
#f2 = open("extract2.pdf",'rb')
#cards[0].attach(name ="test1.pdf",mimeType ="application/pdf", file = f2)
#f2.close()
f.close()
