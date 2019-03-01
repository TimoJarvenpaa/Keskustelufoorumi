# CREATE TABLE -lauseet

<pre>
CREATE TABLE account (
        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        name VARCHAR(144) NOT NULL,
        username VARCHAR(144) NOT NULL,
        password VARCHAR(144) NOT NULL,
        role VARCHAR(16) NOT NULL,
        PRIMARY KEY (id)
);

CREATE TABLE thread (
        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        title VARCHAR(100) NOT NULL,
        account_id INTEGER NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY(account_id) REFERENCES account (id)
);

CREATE TABLE message (
        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        content VARCHAR(500) NOT NULL,
        account_id INTEGER NOT NULL,
        thread_id INTEGER NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY(account_id) REFERENCES account (id),
        FOREIGN KEY(thread_id) REFERENCES thread (id) ON DELETE CASCADE
);

CREATE TABLE category (
        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        name VARCHAR(20) NOT NULL,
        PRIMARY KEY (id)
);

CREATE TABLE thread_category (
        thread_id INTEGER,
        category_id INTEGER,
        FOREIGN KEY(thread_id) REFERENCES thread (id),
        FOREIGN KEY(category_id) REFERENCES category (id)
);
<pre>