import sys

import MapReduce

mr = MapReduce.MapReduce()

A_ROW, A_COL, B_ROW, B_COL = 5, 5, 5, 5


def mapper(record):
    matrix, row, col, val = record

    if matrix == 'a':
        for i in range(B_COL):
            mr.emit_intermediate((row, i), (matrix, row, col, val))
    elif matrix == 'b':
        for i in range(A_ROW):
            mr.emit_intermediate((i, col), (matrix, row, col, val))


def reducer(key, list_of_values):
    from_a = {r[2]: r[3] for r in list_of_values if r[0] == 'a'}
    from_b = {r[1]: r[3] for r in list_of_values if r[0] == 'b'}

    val = 0

    for i in range(A_ROW):
        val += from_a.get(i, 0) * from_b.get(i, 0)

    mr.emit(key + (val,))


if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
