import sys

import MapReduce

mr = MapReduce.MapReduce()


def mapper(record):
    person, friend = record

    mr.emit_intermediate(person, friend)


def reducer(key, list_of_values):
    mr.emit((key, len(list_of_values)))

if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
