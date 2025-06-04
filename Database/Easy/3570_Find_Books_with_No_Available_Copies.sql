-- Write your MySQL query statement below
SELECT LB.book_id, LB.title, LB.author, LB.genre, LB.publication_year, BC.current_borrowers
FROM
library_books LB
INNER JOIN
(
    SELECT book_id, COUNT(*) AS current_borrowers FROM
    borrowing_records
    WHERE
    return_date IS NULL
    GROUP BY book_id
) BC
ON LB.book_id = BC.book_id AND LB.total_copies = BC.current_borrowers
ORDER BY LB.total_copies DESC, LB.title ASC;
