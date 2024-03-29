WITH A AS 
(SELECT CATEGORY, MAX(PRICE) 'MAX_PRICE'
FROM FOOD_PRODUCT
WHERE CATEGORY IN ('과자', '국', '김치', '식용유')
GROUP BY 1)

SELECT CATEGORY, PRICE 'MAX_PRICE', PRODUCT_NAME
FROM FOOD_PRODUCT
WHERE (CATEGORY, PRICE) IN (SELECT * FROM A)
ORDER BY 2 DESC