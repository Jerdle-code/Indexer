def program():
	import configparser, os
	config = configparser.ConfigParser()
	config.read(os.path.expanduser('~/.config/indexer/indexer.conf'))
	thing = config["Config"]["Item"]
	group = config["Config"]["Category"]
	place = config["Config"]["Object"]
	indexfile = os.path.expanduser(config["Config"]["File"])
	global index
	index = open(indexfile,'r+')
	mainprogram(thing, group, place, indexfile)
def listall(thing, group, place):
    index.seek(0)
    for line_list in index:
        displayline(line_list, thing, group, place)
def displayline(line, thing, group, place):
    linelist=line.split('^')
    print(linelist[0] + " with/by " + group + ' ' + linelist[1] + " is on " + place + ' ' + linelist[2])
def listthing(thing, group, place):
    thing_tmp = input("Which " + thing + " are you looking for?   ")
    index.seek(0)
    for line_thing in index:
        if thing_tmp in line_thing:
            displayline(line_thing, thing, group, place)
def listplace(thing, group, place):
    place_tmp = input("Which " + place + " are you looking for?   ")
    index.seek(0)
    for line_place in index:
        if place_tmp in line_place:
            displayline(line_place, thing, group, place)
def listgroup(thing, group, place):
    group_tmp = input("Which " + group + " are you looking for?   ")
    index.seek(0)
    for line_group in index:
        if group_tmp in line_group:
            displayline(line_group, thing, group, place)
def add(thing, group, place):
    thing_tmp_add = input("Which " + thing + " are you adding?   ")
    place_tmp_add = input("Which " + place + " is it on?  ")
    group_tmp_add = input("Which " + group + " is it (by)?  ")
    index.write(thing_tmp_add + "^" + place_tmp_add + "^" + group_tmp_add + "\n")
def delete(thing, group, place):
    thing_tmp_rm = input("Which " + thing + " are you deleting?   ")
    place_tmp_rm = input("Which " + place + " is it on?   ")
    group_tmp_rm = input("Which " + group + " is it (by)?   ")
    lines_to_delete = []
    index.seek(0)
    for line_rm in index:
        if thing_tmp_rm in line_rm and place_tmp_rm in line_rm and group_tmp_rm in line_rm:
            displayline(line_rm, thing, group, place)
            lines_to_delete.append(line_rm)
        response_rm = input("Are you SURE you want to delete these lines?   ").upper()
        response_rm = response_rm[:1]
        if response_rm == "Y":
            lines_rm = index.readlines()
            index.seek(0)
            for i in lines_rm:
                if i not in lines_to_delete:
                    index.write(i)
def reset(thing, group, place, indexfile):
    import os
    response_wipe = input("Are you SURE you want to wipe the database?   ").upper()
    response_wipe = response_wipe[:1]
    if response_wipe == "Y":
        index.close()
        os.remove(indexfile)
        os.mknod(indexfile)
        exit()
def mainprogram(thing, group, place, indexfile):
    while True:
        print("What type of operation do you want to do?")
        print("1: read-only operations")
        print("2: edit the database")
        print("q: quit")
        choice_main = input()
        if choice_main == '1':
            ro(thing, group, place)
        elif choice_main == '2':
            rw(thing, group, place, indexfile)
        elif choice_main == 'q':
            index.close()
            exit()
        else:
            print("Input 1 or 2!")
def ro(thing, group, place):
    while True:
        print("Which operation do you want to do?")
        print("1: list all " + thing +"s")
        print("2: find information about a/an " + thing)
        print("3: list everything with/by a specific " + group)
        print("4: list everything on a/an " + place)
        print("b: back")
        choice_ro = input()
        if choice_ro == '1':
            listall(thing, group, place)
        elif choice_ro == '2':
            listthing(thing, group, place)
        elif choice_ro == '3':
            listgroup(thing, group, place)
        elif choice_ro == '4':
            listplace(thing, group, place)
        elif choice_ro == 'b':
            break
        else:
            print("Input 1-4!")
def rw(thing, group, place, indexfile):
    while True:
        print("Which operation do you want to do?")
        print("1: add a/an " + thing)
        print("2: remove a/an " + thing)
        print("3: wipe the database")
        print("b: back")
        choice_rw = input()
        if choice_rw == '1':
            add(thing, group, place)
        elif choice_rw == '2':
            delete(thing, group, place)
        elif choice_rw == '3':
            reset(thing, group, place, indexfile)
        elif choice_rw == 'b':
            break
        else:
            print("Input 1-3!")
program()
