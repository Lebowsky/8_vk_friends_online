import vk
import getpass

APP_ID = '6312679'


def get_user_login():
    return input('login: ')


def get_user_password():
    return getpass.getpass()


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends',
    )
    api = vk.API(session)
    friend_online_ids = api.friends.getOnline()
    return api.users.get(user_ids=friend_online_ids)


def output_friends_to_console(friends):
    print('Your friends online:')
    for friend in friends:
        print(friend['first_name'], friend['last_name'])


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
