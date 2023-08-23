import utils
import sys
from diarybook import DiaryBook
from registration import login,Registration




class Menu:

    def login(self,choices):



        print("""
        
        1:login
        2:Registration
        3:exit
        
        
        
        """)




        self.choices = {
             1: registration.Registration.login
             2: registration.Registration.registration
             3: sys.exit


        }

        choice = int(input('choice:'))


        if choice in choices:
           action = choices[choice]
           action()

        else :
           print('not in choices')
           self.login()



    def __init__(self):
        self.diarybook = DiaryBook()

        self.choices = {
          "1": self.show_all_diaries,
          "2": self.add_diary,
          "3": self.search_diaries,
          "4": self.quit
        }

    def show_all_diaries(self):
        if len(self.diarybook.diaries) == 0 :
            print("there is no note in database")
        else:
            for diary in self.diarybook.diaries:
             print(f"{diary.id}-{diary.memo}")



    def add_diary(self):
        memo = input('Enter a memo: ')
        tags = input('Enter a tags: ')
        self.diarybook.new_diary(memo,tags)
        print("your note has been addes successfully")


    def search_diaries(self):
        keyword = input("enter a keyword:")
        filtered_diaries = self.diarybook.search_diary(keyword)
        if len(filtered_diaries) == 0:
            print("there is not diary matching this key")
        else:
            for diary in filtered_diaries:
              print(f"{diary.id} - {diary.memo}")

    def populate_database(self):
        diaries = utils.read_from_json_into_app("data.json")
        for diary in diaries:
            self.diarybook.diaries.append(diary)

    def quit(self):
        print("thanks for using diarybook")
        sys.exit(0)

    def Display_menu(self):
        print("""
            Diarybook Menu:
          
          
            1. Show diaries
            2. Add diary
            3.Filter using keyword
            4.Quit program
            """)



    def run(self):
        self.populate_database()
        while True:
            self.Display_menu()
            choice = input("Enter an option:")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))





if __name__ == "__main__":
    Menu().run()