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

/*
  let's break down the SQL query you wrote to identify the busiest route for the airline company:

1. Sample Data Setup:

The initial part creates a table named tickets with columns representing flight information and ticket details:

airline_number: Airline flight identifier (e.g., DEF456)
origin: Departure airport code (e.g., BOM)
destination: Arrival airport code (e.g., DEL)
oneway_round: Indicates one-way ('O') or round-trip ('R') travel
ticket_count: Number of tickets sold for a specific flight
Then, sample data is inserted representing several flights with origin, destination, type (one-way or round-trip), and ticket count.

2. The Main Query:

The core functionality resides in the main SELECT statement:

Subquery (tc):
This part uses a Common Table Expression (CTE) named tc. It combines two subqueries representing both directions of travel for a route.
First Subquery:
Selects origin, destination, and ticket_count directly from the tickets table (t1). This captures one-way trips (both directions) and round-trip origin legs.
Second Subquery:
Selects destination as origin (to account for return trips), origin as destination (to reverse the direction), and ticket_count from tickets table (t2). This captures the return legs of round-trip tickets.
Filters for oneway_round = 'R' to ensure it only considers return legs of round-trip journeys.
Both subqueries are combined using UNION ALL which keeps all duplicate rows (important for round-trip ticket counts).
Main SELECT:
Selects origin and destination from the tc CTE (renamed for clarity).
Uses SUM(tc.ticket) to calculate the total ticket count for each route (considering both directions with UNION ALL).
GROUP BY tc.origin, tc.destination groups the results by route (origin and destination combination).
ORDER BY SUM(tc.ticket) DESC sorts the results in descending order based on the total ticket count (busiest routes first).
LIMIT 1 retrieves only the top row (the busiest route).
How it Works:

The CTE (tc) combines data from both directions of travel for each route.
The main SELECT calculates the total ticket count for each route by summing ticket counts from both directions (one-way and return legs of round-trip tickets).
Grouping by origin and destination ensures separate entries for routes like DEL-NYC and NYC-DEL.
Sorting by total ticket count (descending) prioritizes the busiest routes.
Finally, LIMIT 1 retrieves only the route with the highest total ticket count, representing the busiest route.
This approach ensures that both one-way and round-trip ticket counts are considered for each route, providing an accurate picture of the busiest route based on total ticket sales. 
*/