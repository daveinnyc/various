-- updated for ex9
-- SQLITE3: TRUE == 1, FALSE == 0
CREATE TABLE person(
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    age INTEGER
);

CREATE TABLE pet(
    id INTEGER PRIMARY KEY,
    name TEXT,
    breed TEXT,
    age INTEGER,
    dead INTEGER
);

CREATE TABLE person_pet(
    person_id INTEGER,
    pet_id INTEGER
);

INSERT INTO person (id, first_name, last_name, age) VALUES (0, 'Zed', 'Shaw', 37);
INSERT INTO person (id, first_name, last_name, age) VALUES (1, 'Mr.', 'Wizard', 40);
INSERT INTO person (id, first_name, last_name, age) VALUES (2, 'Me', 'Myself', 25);
INSERT INTO person (id, first_name, last_name, age) VALUES (3, 'Him', 'Them', 33);
INSERT INTO person (id, first_name, last_name, age) VALUES (4, 'Her', 'Them', 33);
INSERT INTO pet (id, name, breed, age, dead) VALUES (0, 'Fluffy', 'Unicorn', 1000, 0);
INSERT INTO pet (id, name, breed, age, dead) VALUES (1, 'Gigantor', 'Great Big Robot', 1, 1);
INSERT INTO pet (id, name, breed, age, dead) VALUES (2, 'Fang', 'Chihuahua', 4, 0);
INSERT INTO pet (id, name, breed, age, dead) VALUES (3, 'Tres', 'Shepard', 4, 1);
INSERT INTO pet (id, name, breed, age, dead) VALUES (4, 'Quatro', 'Wolf', 7, 0);
INSERT INTO pet (id, name, breed, age, dead) VALUES (5, 'Cinco', 'Shih-Tzu', 2, 0);
INSERT INTO pet (id, name, breed, age, dead) VALUES (6, 'Seis', 'Shih-Tzu', 4, 0);
INSERT INTO pet (id, name, breed, age, dead) VALUES (7, 'Siete', 'Mutt', 2, 1);
INSERT INTO pet (id, name, breed, age, dead) VALUES (8, 'Ocho', 'Mutt', 4, 0);
INSERT INTO person_pet (person_id, pet_id) VALUES (0,1);
INSERT INTO person_pet (person_id, pet_id) VALUES (1,2);
INSERT INTO person_pet (person_id, pet_id) VALUES (0,0);
INSERT INTO person_pet (person_id, pet_id) VALUES (2,3);
INSERT INTO person_pet (person_id, pet_id) VALUES (2,4);
INSERT INTO person_pet (person_id, pet_id) VALUES (2,5);
INSERT INTO person_pet (person_id, pet_id) VALUES (2,6);
INSERT INTO person_pet (person_id, pet_id) VALUES (3,7);
INSERT INTO person_pet (person_id, pet_id) VALUES (4,8);


-- ### EXTRA CREDIT QUESTIONS ###
.print ''
.print 'Extra Credit'
SELECT * FROM pet WHERE id < 4;

REPLACE INTO pet (id, name, breed, age, dead)
    VALUES (0, 'Celestia', 'Parrot', 7, 0);

.print ''
.print 'Verify REPLACE'
SELECT * FROM pet WHERE id < 4;

--EOF
