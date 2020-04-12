SELECT
    value
FROM
    (
        SELECT
            m1.row_num as row,
            m2.col_num as col,
            sum(m1.value * m2.value) as value
        FROM
            A m1
            JOIN B m2 on m2.row_num = m1.col_num
        GROUP BY
            m1.row_num,
            m2.col_num
    )
WHERE
    row = 2
    AND col = 3;