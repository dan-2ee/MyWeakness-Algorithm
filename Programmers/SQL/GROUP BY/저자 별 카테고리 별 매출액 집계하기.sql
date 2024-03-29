SELECT BOOK.AUTHOR_ID, AUTHOR_NAME, CATEGORY, SUM(SALES*PRICE) AS TOTAL_SALES
FROM BOOK, AUTHOR, BOOK_SALES
WHERE BOOK.AUTHOR_ID = AUTHOR.AUTHOR_ID AND BOOK.BOOK_ID = BOOK_SALES.BOOK_ID
        AND SALES_DATE LIKE '2022-01%'
GROUP BY BOOK.AUTHOR_ID, CATEGORY
ORDER BY BOOK.AUTHOR_ID, CATEGORY DESC