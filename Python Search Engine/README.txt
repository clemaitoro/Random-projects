


1. What did I implement?

I tested it by running the following command:

    import pearl




    table = ([['inducements', 'eyre.txt'], ['inducements', 'eyre.txt'], ['inducements', 'eyre.txt'], ['inducements', 'eyre.txt'], ['indulged', 'hacktest.txt'], ['indulged', 'hacktest.txt'], ['indulged', 'eyre.txt'], ['indulged', 'hacktest.txt']])



    table = pearl.merge(table) # sort the data
    table = pearl.removecount_dups(table) # remove duplicates and count the number of occurrences
    table = pearl.check_dups2(table) # check for duplicates and put them together
    table = pearl.change_sintax(table) # change the sintax for google.py
    table = pearl.density(table) # count the number of words in the file

    print(table)

for the case the output was:

    [['inducements', [['eyre.txt', 4]]], ['indulged', [['hacktest.txt', 3], ['eyre.txt', 1]]]]

we used serveral variations of these commands like diffrent words or other functions
like we replace:
table = ([['inducements', 'eyre.txt'], ['inducements', 'eyre.txt'], ['inducements', 'eyre.txt'], ['inducements', 'eyre.txt'], ['indulged', 'hacktest.txt'], ['indulged', 'hacktest.txt'], ['indulged', 'eyre.txt'], ['indulged', 'hacktest.txt']])
with:
table = util.all_word_pairs() this created a really big output of all the words, files and density that are connected
but this often took to long to print all the words so we mainly used the first one.
after we completed the basic assignment we started also testing with the google.py and made serveral tests:
We created a file with random words and tested if it was counted correctly by counting in the file manually.
We also tested the density by counting the words of a file with a diffrent command:

count = len(util.words('eyre.txt'))         and serveral other files.   output: 184515

We then started testing with serveral normal words like you, me, the, and, or, and, but, etc. and tested if the density was correct.
with manually counting the occurrences of a word and then dividing it by the total number of words in the file with the previous command.


3. What does the zip file contain

Pearl.py
Readme.txt


