import MapReduce
import sys


mr = MapReduce.MapReduce()


def mapper(record):
    doc_id = record[0]
    words = record[1].split()

    for word in words:
        mr.emit_intermediate(word, doc_id)


def reducer(key, list_of_values):
    total = set()

    for value in list_of_values:
        total.add(value)
        
    mr.emit((key, list(total)))


if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
