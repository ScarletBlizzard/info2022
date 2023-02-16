SELECT b.id, title
FROM Books b
    JOIN Records r ON b.id = r.book_id
WHERE r.returning_date IS NULL; 

SELECT r.name, b.title
FROM Books b
    JOIN Records rec ON b.id = rec.book_id
    JOIN Readers r ON r.id = rec.reader_id;

SELECT author, COUNT(*) AS Количество
FROM Books
GROUP BY author;

