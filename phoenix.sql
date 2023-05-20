DROP VIEW IF EXISTS "powers";

CREATE VIEW "powers" ( "pk" VARCHAR PRIMARY KEY, "personal"."hero" VARCHAR, "personal"."power" VARCHAR, "professional"."name" VARCHAR, "professional"."xp" VARCHAR, "custom"."color" VARCHAR)
AS SELECT * FROM "powers";



SELECT p1."professional"."name" AS "Name1", p2."professional"."name" AS "Name2", p1."personal"."power" AS "Power"
FROM "powers" p1
JOIN "powers" p2 ON p1."personal"."power" = p2."personal"."power" 
AND p1."power" = p2."power" 
WHERE p1."hero"='yes' 
and p2."hero" = 'yes';
