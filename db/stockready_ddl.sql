DROP TABLE IF EXISTS products CASCADE;
DROP TABLE IF EXISTS manufacturers CASCADE;
DROP TABLE IF EXISTS product_types CASCADE;

CREATE TABLE product_types (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE manufacturers (
    id SERIAL PRIMARY KEY,
    -- identify manufacturer
    full_name TEXT NOT NULL,
    short_brand_name TEXT NOT NULL,
    -- contact details
    trade_website TEXT,
    trade_telephone TEXT,
    customer_website TEXT,
    customer_telephone TEXT
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    -- details aligned with manufacturer
    mpn TEXT NOT NULL,
    manufacturer_id INT NOT NULL REFERENCES manufacturers (id),
    -- description and type of product
    short_description TEXT NOT NULL,
    long_description TEXT,
    product_type_id INT NOT NULL REFERENCES product_types (id),
    -- product features
    screen_size FLOAT,
    -- stock and costs
    stock_on_hand INT NOT NULL,
    cost_price DECIMAL(10,2) NOT NULL,
    retail_price DECIMAL(10,2) NOT NULL
);
