# Database Diagrams

NB. mermaid doesn't support database diagrams so this isn't quite the right format

## MVP

```mermaid
classDiagram
    direction LR
    class manufacturers {
        id SERIAL [PK]
        full_name TEXT NOT NULL
        short_brand_name TEXT NOT NULL
        trade_website TEXT
        trade_telephone TEXT
        customer_website TEXT
        customer_telephone TEXT
    }
    class products {
        id SERIAL [PK]
        mpn TEXT NOT NULL
        manufacturer_id INT NOT NULL [FK]
        short_description TEXT NOT NULL
        long_description TEXT
        product_type_id INT NOT NULL [FK]
        screen_size FLOAT
        stock_on_hand INT NOT NULL
        cost_price DECIMAL(10,2)
        retail_price DECIMAL(10,2)
    }
    class product_types {
        id SERIAL [PK]
        name TEXT
    }
    
    manufacturers "1" -- "*" products
    products "*" -- "1" product_types
```

## Active/discontinued products (Extension 4)

```mermaid
classDiagram
    direction LR
    class manufacturers {
        id SERIAL [PK]
        full_name TEXT NOT NULL
        short_brand_name TEXT NOT NULL
        trade_website TEXT
        trade_telephone TEXT
        customer_website TEXT
        customer_telephone TEXT
    }
    class products {
        id SERIAL [PK]
        mpn TEXT NOT NULL
        manufacturer_id INT NOT NULL [FK]
        short_description TEXT NOT NULL
        long_description TEXT
        product_type_id INT NOT NULL [FK]
        screen_size FLOAT
        stock_on_hand INT NOT NULL
        cost_price DECIMAL(10,2)
        retail_price DECIMAL(10,2)
        discontinued BOOL
    }
    class product_types {
        id SERIAL [PK]
        name TEXT
    }
    
    manufacturers "1" -- "*" products
    products "*" -- "1" product_types
```
## Multiple Branches (Extension 5)

```mermaid
classDiagram
    direction LR
    class manufacturers {
        id SERIAL [PK]
        full_name TEXT NOT NULL
        short_brand_name TEXT NOT NULL
        trade_website TEXT
        trade_telephone TEXT
        customer_website TEXT
        customer_telephone TEXT
    }
    class products {
        id SERIAL [PK]
        mpn TEXT NOT NULL
        manufacturer_id INT NOT NULL [FK]
        short_description TEXT NOT NULL
        long_description TEXT
        product_type_id INT NOT NULL [FK]
        screen_size FLOAT
        cost_price DECIMAL(10,2)
        retail_price DECIMAL(10,2)
        discontinued BOOL
    }
    class product_types {
        id SERIAL [PK]
        name TEXT
    }
    class branches {
        id SERIAL [PK]
        address TEXT NOT NULL
        telephone TEXT NOT NULL
    }
    class branches_products_stocks {
        id SERIAL [PK]
        product_id INT NOT NULL [FK]
        branch_id INT NOT NULL [FK]
        stock_on_hand INT NOT NULL
        UNIQUE(product_id, branch_id)
    }

    manufacturers "1" -- "*" products
    products "*" -- "1" product_types
    branches_products_stocks "*" -- "1" branches
    branches_products_stocks "*" -- "1" products
```
