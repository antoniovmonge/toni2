DROP TABLE IF EXISTS POSTS;
CREATE TABLE POSTS (
    id INTEGER primary key autoincrement,
    name TEXT NOT NULL,
    content TEXT NOT NULL
);