SELECT CAR.CAR_ID, CAR.CAR_TYPE, FLOOR(CAR.DAILY_FEE * 30 * (100-D.DISCOUNT_RATE) * 0.01) FEE
FROM CAR_RENTAL_COMPANY_CAR CAR JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY H USING (CAR_ID)
JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN D USING (CAR_TYPE)
WHERE CAR.CAR_TYPE IN ('세단', 'SUV') AND D.DURATION_TYPE = '30일 이상'
GROUP BY CAR.CAR_ID
HAVING MAX(H.END_DATE) <= '2022-11-01' AND FEE BETWEEN 500000 AND 2000000
ORDER BY 3 DESC, 2, 1 DESC