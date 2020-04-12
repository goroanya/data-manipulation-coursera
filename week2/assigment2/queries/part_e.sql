SELECT
    count(*)
FROM
    (
        SELECT
            *
        FROM
            frequency
        GROUP BY
            docid
        HAVING
            count(term) > 300
    );