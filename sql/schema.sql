CREATE TABLE dim_host(
host_id INTEGER PRIMARY KEY,
host_name TEXT
);

CREATE TABLE dim_location(
location_id INTEGER PRIMARY KEY,
neighbourhood_group TEXT,
neighbourhood TEXT
);

CREATE TABLE dim_room(
room_id INTEGER PRIMARY KEY,
room_type TEXT
);

CREATE TABLE fact_listing(
listing_id INTEGER PRIMARY KEY,
host_id INTEGER,
location_id INTEGER,
room_id INTEGER,
price REAL,
minimum_nights INTEGER,
number_of_reviews INTEGER,
availability_365 INTEGER
);