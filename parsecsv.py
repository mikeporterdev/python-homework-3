import csv


def get_voting_data():
    return parse_file('EU-referendum-result-data.csv')


def parse_file(filename):
    # When files are opened, a lock is placed on them to avoid something else editing it whilst you're reading it.
    # The with command will open up the file, place the lock on the file, and remove the lock when the with command has
    # finished (when the code within the indent block is finished).

    # Open('blah.csv') is the command that opens the file and allows reading of the data.
    with open(filename) as file:
        # csv.DictReader(...) is a function from the 'csv' library that parses a file and returns it as a dict.
        # You don't need to worry about the [x for x in ...] syntax for now. I will explain this next lesson.
        return [x for x in csv.DictReader(file)]
