from telethon.sync import TelegramClient
api_id = 
api_hash = ''
client = TelegramClient('simple_user_bot', api_id, api_hash)
client.connect()



def get_all_group_member(chat_id):
    all_participants = client.get_participants(chat_id, aggressive=True)
    all_group_member_list = []
    for index in range(len(all_participants)):
        all_group_member_dict = {'ID': all_participants[index].id, 'Username': all_participants[index].username,'Language': all_participants[index].lang_code, 'Bot': all_participants[index].bot}
        all_group_member_list.append(all_group_member_dict)
        print(all_group_member_dict)
    return all_group_member_list

get_all_group_member(-1001266485204)