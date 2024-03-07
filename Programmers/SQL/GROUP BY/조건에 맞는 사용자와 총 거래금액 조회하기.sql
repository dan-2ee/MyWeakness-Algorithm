SELECT USER_ID, NICKNAME, SUM(PRICE) TOTAL_SALES
FROM USED_GOODS_BOARD AS B, USED_GOODS_USER AS U
WHERE B.WRITER_ID = U.USER_ID AND STATUS = 'DONE' 
GROUP BY WRITER_ID
HAVING SUM(PRICE) >= 700000
ORDER BY TOTAL_SALES