from trello import TrelloClient
token_key_file = open('.\\src\\token_key.txt','r')
my_key = token_key_file.read().split('\n')
client = TrelloClient(
    api_key = my_key[0],
    token= my_key[1] 
)

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
#created_card= target_list.add_card("kanaoka_test"," im made card")