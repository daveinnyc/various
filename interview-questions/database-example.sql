 /* Development command line shortcuts:
 
  -- remove old DBs, create new one and display query results
  rm *db ; sqlite3 -column -header example.db < database-example.sql
*/



CREATE TABLE users(
	id INTEGER PRIMARY KEY,
	firstname TEXT,
	lastname TEXT,
	registerdate DATE
);

CREATE TABLE orders(
    id INTEGER PRIMARY KEY,
    userid INTEGER,
    item TEXT
);

INSERT INTO users (id, firstname, lastname, registerdate) VALUES (1, 'Sally', 'Lnamea', '2016-07-12');
INSERT INTO users (id, firstname, lastname, registerdate) VALUES (2, 'Bob', 'Lnamerb', '2016-07-06');
INSERT INTO users (id, firstname, lastname, registerdate) VALUES (3, 'Fred', 'Lnamec', '2016-07-07');
INSERT INTO users (id, firstname, lastname, registerdate) VALUES (4, 'Tom', 'Lnamed', '2016-07-08');
INSERT INTO users (id, firstname, lastname, registerdate) VALUES (5, 'Sally', 'Lnamee', '2016-07-09');

SELECT COUNT(firstname) AS count, registerdate FROM users WHERE firstname='Sally' GROUP BY registerdate;

INSERT INTO orders (id, userid, item)  VALUES (1, 2, "BB");
INSERT INTO orders (id, userid, item)  VALUES (2, 3, "CC");
INSERT INTO orders (id, userid, item)  VALUES (3, 5, "EE");
INSERT INTO orders (id, userid, item)  VALUES (4, 1, "AA");
INSERT INTO orders (id, userid, item)  VALUES (5, 3, "CC");

SELECT orders.id,
       users.firstname, 
       users.lastname 
    FROM orders
    LEFT JOIN users 
    ON orders.userid = users.id
    ORDER BY orders.id;

    
