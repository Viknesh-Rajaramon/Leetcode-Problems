-- Write your MySQL query statement below
SELECT l.book_id, l.title, l.author, l.genre, l.publication_year, b.current_borrowers FROM
library_books l
INNER JOIN
(
    SELECT book_id, COUNT(*) AS current_borrowers FROM
    borrowing_records
    WHERE return_date IS NULL
    GROUP BY book_id
) b
ON l.book_id = b.book_id AND l.total_copies = b.current_borrowers
ORDER BY b.current_borrowers DESC, l.title ASC;
