CREATE TABLE currency
(
    name VARCHAR,
    code VARCHAR PRIMARY KEY,
    rate FLOAT
);

CREATE TABLE last_currency_update
(
    updated_at INT PRIMARY KEY
)