
import util


def make_table(pairs): # main function for the google.py
    table = [] # start with an empty table

    table = merge(pairs) # sort the data
    table = remove_dups(table) # remove duplicates and count the number of occurrences
    table = check_dups(table)  # check for duplicates and put them together
    table = change_sintax2(table)  # change the sintax for google.py

    return table # return the table


def make_counted_table(pairs):   # main function for the google.py
    table = []          # start with an empty table

    table = merge(pairs)  # sort the data
    table = removecount_dups(table) 
    table = check_dups2(table) # check for duplicates and put them together
    table = change_sintax(table) # change the sintax for google.py

    return table       # return the table


def make_density_table(pairs):   # main function for the google.py
    table = [] # start with an empty table

    table = merge(pairs) # sort the data
    table = removecount_dups(table) # remove duplicates and count the number of occurrences
    table = check_dups2(table) # check for duplicates and put them together
    table = change_sintax(table) # change the sintax for google.py
    table = density(table) # count the number of words in the files

    return table # return the table


def density(data):  # count the number of words
    files = [data[0][1][0][0]]  # start with the first file
    i = 0  # start with the first element of the list
    while i < len(data):  # while the list has elements
        j = 1  # start with the second element of the list within the list
        while j < len(data[i]):  # while the list within the list has elements
            files.append(data[i][j][0][0])  # add the file to the list
            j += 1  # increase the index of the second while loop
        i += 1  # increase the index of the first while loop
    files = merge(files)  # sort the list of filnames
    files = remove_dups(files)  # remove duplicates of same filename

    i = 0  # start with the first element of the list
    length = []  # start with an empty list
    while i < len(files):  # while the list has elements
        # add the number of words in the file to the list
        length.append(len(util.words(files[i])))
        i += 1  # increase the index of the while loop

    i = 0  # start with the first element of the list
    while i < len(data):  # while the list has elements
        k = 0  # start with the first element of the list within the list
        while k < len(data[i][1]):  # while the list within the list has elements
            j = 0  # start with the first element of the list length
            while j < len(length):  # while the list length has elements
                if files[j] == data[i][1][k][0]:  # if the file is the same
                    # divide the number of occurrences by the number of words
                    data[i][1][k][1] = data[i][1][k][1]/length[j]

                j += 1  # increase the index of the third while loop
            k += 1  # increase the index of the second while loop
        # sort the list in decreasing order of density
        data[i][1] = merge_decreasing(data[i][1])
        i += 1  # increase the index of the first while loop
    return data


def merge(data):  # merge sort
    if len(data) == (0 or 1):  # if the list is empty or has only one element
        res = data[:]  # return the list
        return res

    else:  # if the list has more than one element
        mid = (len(data)) // 2  # find the middle of the list
        fst = merge(data[:mid])  # sort the first half of the list
        snd = merge(data[mid:])  # sort the second half of the list
        res = []  # start with an empty list
        fi = 0  # index for the first half
        si = 0  # index for the second half
        while (fi < len(fst)) and (si < len(snd)):  # while both lists have elements
            if fst[fi] < snd[si]:  # if the first element of the first list is smaller than the first element of the second list
                # add the first element of the first list to the result list
                res.append(fst[fi])
                fi += 1  # increase the index for the first list
            else:  # if the first element of the second list is smaller than the first element of the first list
                # add the first element of the second list to the result list
                res.append(snd[si])
                si += 1  # increase the index for the second list

        if fi < len(fst):  # if the first list has elements left
            # add the rest of the first list to the result list
            res.extend(fst[fi:])
        elif si < len(snd):  # if the second list has elements left
            # add the rest of the second list to the result list
            res.extend(snd[si:])

        return res  # return the result list


def merge_decreasing(data):  # merge sort
    if len(data) == (0 or 1):  # if the list is empty or has only one element
        res = data[:]  # return the list
        return res

    else:  # if the list has more than one element
        mid = (len(data)) // 2  # find the middle of the list
        fst = merge_decreasing(data[:mid])  # sort the first half of the list
        snd = merge_decreasing(data[mid:])  # sort the second half of the list
        res = []  # start with an empty list
        fi = 0  # index for the first half
        si = 0  # index for the second half
        while (fi < len(fst)) and (si < len(snd)):  # while both lists have elements
            if fst[fi][1] > snd[si][1]:  # if the first element of the list whitin the list the second element is smaller than the first element of the second list within that list the second element
                # add the first element of the first list to the result list
                res.append(fst[fi])
                fi += 1  # increase the index for the first list
            else:  # if the first element of the second list within that list the second element is smaller than the first element of the first list within that list the second element
                # add the first element of the second list to the result list
                res.append(snd[si])
                si += 1  # increase the index for the second list
        if fi < len(fst):  # if the first list has elements left
            # add the rest of the first list to the result list
            res.extend(fst[fi:])
        elif si < len(snd):  # if the second list has elements left
            # add the rest of the second list to the result list
            res.extend(snd[si:])

        return res  # return the result list


def removecount_dups(data):  # remove duplicates and count the number of occurrences
    res = []  # start with an empty list
    if len(data) != 0:  # if the list is not empty
        fresh = data[0]  # copy the first element(list) of the list to fresh
        fresh.append(1)  # add the number of occurrences
        i = 1  # start with the second element of the list
        while i < len(data):  # while the list has elements

            # if the first element of the fresh list is not equal to the first element of the list within the list
            if (fresh[0] != data[i][0]):
                res.append(fresh)  # add the fresh list to the result list
                fresh = data[i]  # copy the list data to fresh
                fresh.append(1)  # add the number of occurrences
            # if the second element of the fresh list is not equal to the second element of the list within the list
            elif fresh[1] != data[i][1]:
                res.append(fresh)  # add the fresh list to the result list
                fresh = data[i]  # copy the list data to fresh
                fresh.append(1)  # add the number of occurrences
            else:  # if the first and second element of the fresh list is equal to the first and second element of the list within the list
                fresh[2] = fresh[2]+1  # increase the number of occurrences

            i += 1  # increase the index

        res.append(fresh)  # add the last fresh list to the result list
    return res  # return the result list


def remove_dups(data):  # remove duplicates
    res = []  # start with an empty list
    if len(data) != 0:  # if the list is not empty
        fresh = data[0]  # copy the first element(list) of the list to fresh
        i = 1  # start with the second element of the list
        while i < len(data):  # while the list has elements
            if fresh != data[i]:  # if the fresh list is not equal to the list within the list
                res.append(fresh)  # add the fresh list to the result list
                fresh = data[i]  # copy the list data to fresh
            i += 1  # increase the index
        res.append(fresh)  # add the last fresh list to the result list
    return res  # return the result list


def check_dups2(data):  # check for duplicates and put them together
    res = []  # start with an empty list
    if len(data) != 0:  # if the list is not empty
        fresh = data[0]  # copy the first element(list) of the list to fresh

        i = 1  # start with the second element of the list
        while i < len(data):  # while the list has elements
            # if the first element of the fresh list is equal to the first element of the list within the list
            if fresh[0] == data[i][0]:
                # add the second element of the list within the list to the fresh list
                fresh.append(data[i][1])
                # add the third element of the list within the list to the fresh list
                fresh.append(data[i][2])
            # if the first element of the fresh list is not equal to the first element of the list within the list
            elif fresh != data[i][0]:
                res.append(fresh)  # add the fresh list to the result list
                fresh = data[i]  # copy the list data to fresh
            i += 1  # increase the index
        res.append(fresh)  # add the last fresh list to the result list
    return res  # return the result list


def check_dups(data):  # check for duplicates and put them together
    res = []  # start with an empty list
    if len(data) != 0:  # if the list is not empty
        fresh = data[0]  # copy the first element(list) of the list to fresh
        i = 1  # start with the second element of the list
        while i < len(data):  # while the list has elements
            # if the first element of the fresh list is equal to the first element of the list within the list
            if fresh[0] == data[i][0]:
                # add the second element of the list within the list to the fresh list
                fresh.append(data[i][1])
            # if the first element of the fresh list is not equal to the first element of the list within the list
            elif fresh != data[i][0]:
                res.append(fresh)  # add the fresh list to the result list
                fresh = data[i]  # copy the list data to fresh
            i += 1  # increase the index
        res.append(fresh)  # add the last fresh list to the result list
    return res  # return the result list


def change_sintax(data):  # change the sintax for google.py
    res = []  # start with an empty list
    i = 0  # start with the first element of the list
    while i < len(data):  # while the list has elements
        changed = []  # restart with an empty list
        si = 1  # start with the second element of the list
        while si < len(data[i]):  # while the list within the list has elements
            changed.append(data[i][si])  # add the element to the changed list
            # make a list with the first element of the list within the list and the changed list
            final = [data[i][0], changed]
            si = si + 1  # increase the index
        i += 1  # increase the index
        res.append(final)  # add the final list to the result list

    data = res[:]  # copy the result list to data
    changed = []  # restart with an empty list
    res = []  # restart with an empty list
    i = 0  # start with the first element of the list
    while i < len(data):  # while the list has elements
        si = 0  # start with the first element of the list within the list
        changed = []  # restart with an empty list
        while si < len(data[i][1]):  # while the list within the list has elements
            # add the element to the changed list
            changed.append([data[i][1][si], data[i][1][si+1]])
            si = si + 2  # increase the index by 2
        # sort the list in decreasing order of matched words
        changed = merge_decreasing(changed)
        # make a list with the first element of the list within the list and the changed list
        copy = [data[i][0], changed]
        res.append(copy)  # add the copy list to the result list
        i += 1  # increase the index
    return res  # return the result list


def change_sintax2(data):  # change the sintax of the data
    res = []  # start with an empty list
    i = 0  # start with the first element of the list
    test = []  # start with an empty list
    while i < len(data):  # while the list has elements
        changed = []  # start with an empty list
        si = 1  # start with the second element of the list
        test = data[i]  # copy the list data to test
        while si < len(test):  # while the list has elements
            changed.append(data[i][si])  # add the list data to changed
            # copy the list data with the other elements to final
            final = [data[i][0], changed]
            si = si + 1  # increase the index
        i += 1  # increase the index
        res.append(final)  # add the final list to the result list
    return res  # return the result list
