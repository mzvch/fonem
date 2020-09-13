DROP table IF EXISTS slowko  ;
create table slowko (
    slowko_id INTEGER PRIMARY KEY,
    ortograficzna TEXT NOT NULL,
    fonetyczna TEXT NOT NULL
);

INSERT INTO slowko values (1, 'siano', 'śano');