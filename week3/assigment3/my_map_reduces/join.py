import sys

import MapReduce

mr = MapReduce.MapReduce()


def mapper(record):
    order_id = record[1]

    mr.emit_intermediate(order_id, record)


def reducer(key, list_of_values):
    line_item_values = [v for v in list_of_values if v[0] == 'line_item']
    order_values = [v for v in list_of_values if v[0] == 'order']

    for r1 in order_values:
        for r2 in line_item_values:
            mr.emit(r1 + r2)


if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
