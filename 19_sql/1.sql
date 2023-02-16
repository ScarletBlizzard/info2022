CREATE TABLE Books (
    id INTEGER PRIMARY KEY,
    author TEXT,
    title TEXT,
    publish_year INTEGER 
);

CREATE TABLE Readers (
    id INTEGER PRIMARY KEY,
    name TEXT
);

CREATE TABLE Records (
    id INTEGER PRIMARY KEY,
  	reader_id INTEGER,
  	book_id INTEGER,
    taking_date TEXT,
    returning_date TEXT,
    FOREIGN KEY (reader_id) REFERENCES Reader (id),
    FOREIGN KEY (book_id) REFERENCES Books (id)
);

INSERT INTO Books (author, title, publish_year)
VALUES
    ("Братья Стругацкие", "Пикник на обочине", 1972),
    ("Дуглас Хофштадтер", "Гёдель, Эшер, Бах", 1979),
    ("Бернар Вербер",     "Танатонавты", 1994);

INSERT INTO Readers (name)
VALUES
    ("Максим Сушков"),
    ("John Doe");

INSERT INTO Records (reader_id, book_id, taking_date, returning_date)
VALUES
    (1, 1, "2016-05-05 12:00:00", "2016-06-06 12:00:00"),
    (1, 3, "2023-01-28 14:00:00", "2023-02-10 11:30:00"),
    (2, 2, "2022-12-12", NULL);

