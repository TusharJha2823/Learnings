CREATE SCHEMA ANGELONE;

USE ANGELONE;
CREATE TABLE tickets(
    airline_number VARCHAR(10),
    origin VARCHAR(3),
    destination VARCHAR(3),
    oneway_round CHAR(1),
    ticket_count INT
);

INSERT INTO tickets (
    airline_number, origin, destination, oneway_round, ticket_count
)
VALUES 
 ('DEF456', 'BOM', 'DEL', 'O', 150),
 ('GHI789', 'DEL', 'BOM', 'R', 50),
 ('JKL012', 'BOM', 'DEL', 'R', 75),
 ('MNO345', 'DEL', 'NYC', 'O', 200),
 ('PQR678', 'NYC', 'DEL', 'O', 180),
 ('STU901', 'NYC', 'DEL', 'R', 60),
 ('ABC123', 'DEL', 'BOM', 'O', 100),
 ('VWX234', 'DEL', 'NYC', 'R', 90);


SELECT tc.origin  AS origin, tc.destination AS destination, SUM(tc.ticket) as ticket_sum FROM (
 (SELECT t1.origin AS origin, t1.destination AS destination, t1.ticket_count as ticket
 FROM tickets t1
 )
 UNION ALL (
    SELECT t2.destination AS destination, t2.origin AS origin, t2.ticket_count as ticket
 FROM tickets t2
 WHERE oneway_round = 'R'
 )) AS tc
 GROUP BY tc.origin, tc.destination
 ORDER BY SUM(tc.ticket) DESC
 LIMIT 1;