#############################
#   Edit these variables    #
#############################
group = 'version'
place = 'DVD'
thing = 'distro'
indexfile = '/home/daniel/distros'
#####################################################
#   Don't edit, unless you know what you are doing  #
#####################################################
import sys
index = open(indexfile,'r+')
def listall():
    index.seek(0)
    for line_list in index:
        displayline(line_list)
def displayline(line):
    linelist=line.split('^')
    print(linelist[0] + " with " + group + ' ' + linelist[1] + " is on " + place + ' ' + linelist[2])
def listthing():
    thing_tmp = input("Which " + thing + " are you looking for?   ")
    index.seek(0)
    for line_thing in index:
        if thing_tmp in line_thing:
            displayline(line_thing)
def listplace():
    place_tmp = input("Which " + place + " are you looking for?   ")
    index.seek(0)
    for line_place in index:
        if place_tmp in line_place:
            displayline(line_place)
def listgroup():
    group_tmp = input("Which " + group + " are you looking for?   ")
    index.seek(0)
    for line_group in index:
        if group_tmp in line_group:
            displayline(line_group)
def add():
    thing_tmp_add = input("Which " + thing + " are you adding?   ")
    place_tmp_add = input("Which " + place + " is it on?  ")
    group_tmp_add = input("Which " + group + " is it (by)?  ")
    index.write(thing_tmp_add + "^" + place_tmp_add + "^" + group_tmp_add)
def delete():
    thing_tmp_rm = input("Which " + thing + " are you deleting?   ")
    place_tmp_rm = input("Which " + place + " is it on?   ")
    group_tmp_rm = input("Which " + group + " is it (by)?   ")
    lines_to_delete = []
    index.seek(0)
    for line_rm in index:
        if thing_tmp_rm in line_rm and place_tmp_rm in line_rm and group_tmp_rm in line_rm:
            displayline(line_rm)
            lines_to_delete.append(line_rm)
        response_rm = input("Are you SURE you want to delete these lines?   ").upper()
        response_rm = response_rm[:1]
        if response_rm == "Y":
            lines_rm = index.readlines()
            index.seek(0)
            for i in lines_rm:
                if i not in lines_to_delete:
                    index.write(i)
def reset():
    response_wipe = input("Are you SURE you want to wipe the database?   ").upper()
    response_wipe = response_wipe[:1]
    if response_wipe == "Y":
        index.seek(0)
        index.write('')
def mainprogram():
    while True:
        print("What type of operation do you want to do?")
        print("1: read-only operations")
        print("2: edit the database")
        print("q: quit")
        choice_main = input()
        if choice_main == '1':
            ro()
        elif choice_main == '2':
            rw()
        elif choice_main == 'q':
            index.close()
            sys.exit()
        else:
            print("Input 1 or 2!")
def ro():
    while True:
        print("Which operation do you want to do?")
        print("1: list all " + thing +"s")
        print("2: find information about a/an " + thing)
        print("3: list everything with/by a specific " + group)
        print("4: list everything on a " + place)
        print("q: quit")
        choice_ro = input()
        if choice_ro == '1':
            listall()
        elif choice_ro == '2':
            listthing()
        elif choice_ro == '3':
            listgroup()
        elif choice_ro == '4':
            listplace()
        elif choice_ro == 'q':
            break
        else:
            print("Input 1-4!")
def rw():
    while True:
        print("Which operation do you want to do?")
        print("1: add a " + thing)
        print("2: remove a " + thing)
        print("3: wipe the database")
        print("q: quit")
        choice_rw = input()
        if choice_rw == '1':
            add()
        elif choice_rw == '2':
            delete()
        elif choice_rw == '3':
            reset()
        elif choice_rw == 'q':
            break
        else:
            print("Input 1-3!")
mainprogram()
