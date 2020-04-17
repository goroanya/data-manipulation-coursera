import sys

import MapReduce

mr = MapReduce.MapReduce()


def mapper(record):

    friends_sorted = sorted(record)
    mr.emit_intermediate(tuple(friends_sorted), True)


def reducer(key, list_of_values):
    person, friend = key

    if len(list_of_values) != 2:
        mr.emit((person, friend))
        mr.emit((friend, person))


if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
