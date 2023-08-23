import json
import main


class Registration:


    @staticmethod
    def registration():
        print('Registration:')
        username = input("Username:")

        with open('users.json','r') as file:
            data = json.load(file)

        if username in [user['username']for user in data]:
            print('username already exists\nyou can login')
        Registration.login()

        else:
            password = input('password:')
            confirm = ('confirm password:')

            if password == confirm:
                data.append({'username':username,'passsword':password})
                with open('users/users.json','w') as file:
                    json.dump(data,file,indent=4)




    @staticmethod
    def login():
        print('Login')
        username = input('username:')

        with open('users.json','r') as file:
           data = json.load(file)

        user_username = [user["username"] for user in data]
        if username in user_usernames:

            password = input('password: ')
            for user in data:
                if (user['username'] == username) and (user['password'] == password):
                    print("processing ...")
                    main.Menu(username,password).run()

        else:
            print(f'User with username"{username}",not excists')



if __name__ == '__main__':
    Registration.login()
