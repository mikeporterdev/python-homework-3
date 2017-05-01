from parsecsv import get_voting_data


# I've created a method for you in parsecsv.py that will automatically parse a spreadsheet as a list of dicts.
# Call the get_voting_data() function to retrieve a list of dicts representing the csv dataset.
# Fill out the various methods that parse and manipulate this data.

# I have written print data for you so that you can see what the parsed data looks like, and so you can see how to call
# it.

def print_data():
    data_dict = get_voting_data()
    print(data_dict)
    for row in data_dict:
        print(row['Area'])


print(print_data())


def sum_of_all_votes():
    pass


def sem_of_all_remain_votes():
    pass


def sum_of_all_leave_votes():
    pass


def top_five_highest_turnout_areas():
    pass


def lowest_five_turnout_areas():
    pass


def sum_of_all_people_who_cant_fill_a_ballot_properly():
    # sum up the rejected, no_official_mark, voting_for_both_answers, writing_or_mark and unmarked ballots.
    pass


def average_of_failed_ballots_by_area():
    pass

# Find a few different csv datasets available online and see what kind of stuff you can parse out of them.
# To add a new file, put the csv in the same place the referendum csv is and add a new method to parsecsv that passes
# in the file name to parse_data. Once you've added a new get_x_data method, you will need to add it to the import
# statement at the top. ie. from parsecsv import get_voting_data, get_x_data. Pycharm might offer to handle this
# automatically for you.

# I've left some comments around the parsing methods to show you a bit about how they work.

# This is very much a play around exercise to teach how to read and manipulate datasets.
# Some recommended data sets could be weather data, football data, other voting statistics etc.
