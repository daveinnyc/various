-- added in ex2
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

-- added in ex3
INSERT INTO person (id, first_name, last_name, age) VALUES (0, 'Zed', 'Shaw', 37);
INSERT INTO pet (id, name, breed, age, dead) VALUES (0, 'Fluffy', 'Unicorn', 1000, 0);
INSERT INTO pet VALUES (1, 'Gigantor', 'Great Big Robot', 1, 1);


-- added in ex4
INSERT INTO person_pet (person_id, pet_id) VALUES (0,0);
INSERT INTO person_pet VALUES (0,1);
INSERT INTO person (id, first_name, last_name, age) VALUES (1, 'Mr.', 'Wizard', 40);
INSERT INTO pet (id, name, breed, age, dead) VALUES (2, 'Fang', 'Chihuahua', 4, 1);
INSERT INTO person_pet (person_id, pet_id) VALUES (1,2);


-- added in ex5
SELECT * FROM person;
SELECT name, age FROM pet;
SELECT name, age FROM pet WHERE dead == 0;
SELECT * FROM person WHERE first_name != 'Zed';


-- ### EXTRA CREDIT QUESTIONS ###
-- pets older than 10 years
SELECT * FROM pet WHERE age > 10;

-- younger than Mr WIzard
SELECT id, last_name, age FROM person WHERE age < 40;

-- AND clause
SELECT id, first_name, age FROM person WHERE age > 10 AND age < 50;

-- multiple clauses
SELECT first_name FROM person WHERE (age < 30 OR first_name == 'Mr.') AND last_name == 'Wizard';;
SELECT last_name FROM person WHERE (age > 30 AND age < 40) OR first_name == 'Mr.';

--EOF
