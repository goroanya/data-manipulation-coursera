import sys

import MapReduce

mr = MapReduce.MapReduce()


def mapper(record):
    nucleotides = record[1][:-10]
    mr.emit_intermediate(nucleotides, True)


def reducer(key, list_of_values):
    mr.emit(key)


if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
