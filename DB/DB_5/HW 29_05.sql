SELECT 
    k.Name_KL AS "Имя заказчика",
    ROUND(AVG(z.Cena_Dostavki), 2) AS "Средняя цена доставки",
    CASE 
        WHEN AVG(z.Cena_Dostavki) > (SELECT AVG(Cena_Dostavki) FROM Zakaz) 
            THEN 'lot'
        ELSE 'few'
    END AS "Статус доставки"
FROM Klient k
JOIN Zakaz z ON k.ID_KL = z.ID_KL
GROUP BY k.ID_KL, k.Name_KL;


SELECT 
    z.ID_Z AS "ID_Z",
    z.ID_Pr AS "ID_Pr",
    z.ID_KL AS "ID_KL",
    z.SUMMA AS "SUMMA",
    z.Kol AS "Kol",
    z.Kol || ' ' || z.DATA || ' ' || z.CITY_Z AS "DATA",
    z.CITY_Z AS "CITY_Z",
    z.Cena_Dostavki AS "Cenu_I",
    k.ID_KL AS "ID_KL:",
    k.ID_Pr AS "ID_Pr::",
    k.Name_KL AS "Name_KL",
    k.City_KL AS "City_KL",
    k.Obl_KL AS "Obl_KL",
    k.Discoun AS "Discou",
    p.ID_Pr AS "ID_Pr::",
    p.Name_Pr AS "Name_Pr",
    p.City_Pr AS "City_Pr"
FROM Zakaz z
JOIN Klient k ON z.ID_KL = k.ID_KL
JOIN Prodaves p ON z.ID_Pr = p.ID_Pr
ORDER BY z.ID_Z;

SELECT 
    p.Name_Pr AS "Имя продавца",
    k.Name_KL AS "Имя клиента",
    k.Discoun AS "Скидка клиента (%)"
FROM Prodaves p
JOIN Klient k ON p.ID_Pr = k.ID_Pr
LEFT JOIN Zakaz z ON k.ID_KL = z.ID_KL
GROUP BY p.ID_Pr, k.ID_KL
ORDER BY p.Name_Pr, k.Name_KL;

SELECT 
    k.ID_KL,
    k.ID_Pr,
    k.Name_KL,
    k.City_KL,
    k.Obl_KL,
    k.Discoun,
    z.ID_Z,
    z.ID_Pr,
    z.ID_KL,
    z.SUMMA,
    z.Kol,
    z.DATA,
    z.CITY_Z,
    z.Cena_Dostavki
FROM Klient k
JOIN Zakaz z ON k.ID_KL = z.ID_KL
ORDER BY k.ID_KL, z.ID_Z;

SELECT Name_Pr, ID_Pr
FROM Prodaves p
WHERE EXISTS (
    SELECT k.ID_KL
    FROM Klient k
    WHERE k.City_KL = p.City_Pr AND k.ID_Pr <> p.ID_Pr
        )
ORDER BY ID_Pr;


SELECT City_pr, Name_Pr
FROM (
    SELECT City_Pr, Name_Pr
    FROM Prodaves
    WHERE City_Pr = 'London'
    
    UNION ALL
    
    SELECT City_KL, Name_KL
    FROM Klient
    WHERE City_KL = 'London'
)
ORDER BY Name_Pr
