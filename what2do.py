# -*- coding: utf-8 -*-
# this program selects one activity, one book and one video game

from datetime import date
import calendar
from select_random_thing import select_random_from_list, open_file

filename = "drawabox_exercises.csv"
activity_path = "wtd/activities.csv"
book_path = "wtd/books.csv"
game_path = "wtd/games.csv"

activity_list = open_file(activity_path)
book_list = open_file(book_path)
game_list = open_file(game_path)

current_date = date.today()

print("On this beautiful "
      + calendar.day_name[current_date.weekday()]
      + " you should go",
      select_random_from_list(activity_list))
print("Today's book is", select_random_from_list(book_list))
print("Today's game is", select_random_from_list(game_list))
