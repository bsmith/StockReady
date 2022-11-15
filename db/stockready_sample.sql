-- This file contains some sample data that can be loaded into the database
-- WARNING: It will clear the database first!
DELETE FROM products;
DELETE FROM product_types;
DELETE FROM manufacturers;

INSERT INTO product_types (name) VALUES
    ('Television'),
    ('Soundbar'),
    ('HDMI cable'),
    ('Wall mount');

INSERT INTO manufacturers (full_name, short_brand_name, trade_website, trade_telephone, customer_website, customer_telephone) VALUES
    ('Shrub Radio Ltd', 'Shrub', NULL, '01632 496 0456', NULL, '0808 1570456'),
    ('Blue Point GmbH', 'Blue', 'http://bluepoint.de/trade/', NULL, 'http://bluepoint.uk.com/', NULL),
    ('Konosuke Electric Industrial Co., Ltd.', 'Kono', 'https://konoglobal.com/', '+81 874 34 345 67', 'https://kono.co.uk/', '0808 1570123'),
    ('Gold Star Electronics Inc.', 'GS', 'https://gselectronics.com/uk/', '+1 334 555 2143', 'https://gs.co.uk/', '+44 20 7946 0214'),
    ('Wolverhampton Video Products Ltd', 'WVP', 'https://wvp.co.uk/trade/', NULL, 'https://wvp.co.uk/support/', NULL),
    ('Click Cables Inc', 'OB', NULL, '0141 496 0667', NULL, NULL),
    ('BCL Empty Test', 'BCL', NULL, NULL, NULL, NULL)
    ;

INSERT INTO products (mpn, manufacturer_id, short_description, long_description, product_type_id, screen_size, stock_on_hand, cost_price, retail_price) VALUES
    (
        'GS32BBB', (SELECT id FROM manufacturers WHERE short_brand_name = 'GS'),
        'GS 32" LED TV (2021)',
        'GS 32" B-series Full HD Smart LED TV with remote control',
        (SELECT id FROM product_types WHERE name = 'Television'),
        32, -- screen size
        10, -- SOH
        125.00, -- cost price
        175.00 -- retail price
    ),
    (
        'GS43BBB', (SELECT id FROM manufacturers WHERE short_brand_name = 'GS'),
        'GS 43" LED TV (2021)',
        'GS 43" B-series Full HD Smart LED TV with remote control',
        (SELECT id FROM product_types WHERE name = 'Television'),
        43, -- screen size
        1, -- SOH
        200.00, -- cost price
        275.00 -- retail price
    ),
    (
        'GS48BBB', (SELECT id FROM manufacturers WHERE short_brand_name = 'GS'),
        'GS 48" LED TV (2021)',
        'GS 48" B-series Full HD Smart LED TV with remote control',
        (SELECT id FROM product_types WHERE name = 'Television'),
        48, -- screen size
        5, -- SOH
        250.00, -- cost price
        340.00 -- retail price
    ),
    (
        'GS55BBB', (SELECT id FROM manufacturers WHERE short_brand_name = 'GS'),
        'GS 55" LED TV (2021)',
        'GS 55" B-series Full HD Smart LED TV with remote control',
        (SELECT id FROM product_types WHERE name = 'Television'),
        55, -- screen size
        0, -- SOH
        300.00, -- cost price
        380.00 -- retail price
    ),
    (
        'GS65BBB', (SELECT id FROM manufacturers WHERE short_brand_name = 'GS'),
        'GS 65" LED TV (2021)',
        'GS 65" B-series Full HD Smart LED TV with remote control',
        (SELECT id FROM product_types WHERE name = 'Television'),
        65, -- screen size
        3, -- SOH
        350.00, -- cost price
        450.00 -- retail price
    ),
    (
        'GS48ABC', (SELECT id FROM manufacturers WHERE short_brand_name = 'GS'),
        'GS 48" A-series TV',
        'GS 48" Super Smart 4K TV (A-series, 2022)',
        (SELECT id FROM product_types WHERE name = 'Television'),
        48, -- screen size
        0, -- SOH
        300.00, -- cost price
        380.00 -- retail price
    ),
    (
        'GS55ABC', (SELECT id FROM manufacturers WHERE short_brand_name = 'GS'),
        'GS 55" A-series TV',
        'GS 55" Super Smart 4K TV (A-series, 2022)',
        (SELECT id FROM product_types WHERE name = 'Television'),
        55, -- screen size
        1, -- SOH
        380.00, -- cost price
        450.00 -- retail price
    ),
    (
        'GS65ABC', (SELECT id FROM manufacturers WHERE short_brand_name = 'GS'),
        'GS 65" A-series TV',
        'GS 65" Super Smart 4K TV (A-series, 2022)',
        (SELECT id FROM product_types WHERE name = 'Television'),
        65, -- screen size
        2, -- SOH
        420.00, -- cost price
        520.00 -- retail price
    ),
    (
        'GS75ABC', (SELECT id FROM manufacturers WHERE short_brand_name = 'GS'),
        'GS 75" A-series TV',
        'GS 75" Super Smart 4K TV (A-series, 2022)',
        (SELECT id FROM product_types WHERE name = 'Television'),
        75, -- screen size
        3, -- SOH
        480.00, -- cost price
        600.00 -- retail price
    ),
    (
        '55KQ22', (SELECT id FROM manufacturers WHERE short_brand_name = 'Kono'),
        'Kono 55" Quantum',
        'Kono 4k Quantum SMART 55"
        
        The Kono Quantum series incorporates the latest in teleportation technology to really put the actors in your living room!
        
        (Caution: May not actually teleport)
        (Warning: May cause teleportation)',
        (SELECT id FROM product_types WHERE name = 'Television'),
        55, -- screen size
        2, -- SOH
        400.00, -- cost price
        500.00 -- retail price
    ),
    (
        '65KQ22', (SELECT id FROM manufacturers WHERE short_brand_name = 'Kono'),
        'Kono 65" Quantum',
        'Kono 4k Quantum SMART 65"
        
        The Kono Quantum series incorporates the latest in teleportation technology to really put the actors in your living room!
        
        (Caution: May not actually teleport)
        (Warning: May cause teleportation)',
        (SELECT id FROM product_types WHERE name = 'Television'),
        65, -- screen size
        2, -- SOH
        470.00, -- cost price
        570.00 -- retail price
    ),
    (
        '75KQ22', (SELECT id FROM manufacturers WHERE short_brand_name = 'Kono'),
        'Kono 75" Quantum',
        'Kono 4k Quantum SMART 75"
        
        The Kono Quantum series incorporates the latest in teleportation technology to really put the actors in your living room!
        
        (Caution: May not actually teleport)
        (Warning: May cause teleportation)',
        (SELECT id FROM product_types WHERE name = 'Television'),
        75, -- screen size
        2, -- SOH
        610.00, -- cost price
        700.00 -- retail price
    ),
    (
        '85KQ22', (SELECT id FROM manufacturers WHERE short_brand_name = 'Kono'),
        'Kono 85" Quantum',
        'Kono 4k Quantum SMART 85"
        
        The Kono Quantum series incorporates the latest in teleportation technology to really put the actors in your living room!
        
        (<i>Caution</i>: May not actually teleport)
        (<b>Warning</b>: May cause teleportation)',
        (SELECT id FROM product_types WHERE name = 'Television'),
        85, -- screen size
        4, -- SOH
        800.00, -- cost price
        1000.00 -- retail price
    ),
    (
        'CCI01HDMI', (SELECT id FROM manufacturers WHERE short_brand_name = 'OB'),
        '1m HDMI Cable',
        NULL,
        (SELECT id FROM product_types WHERE name = 'HDMI cable'),
        NULL, -- screen size
        40, -- SOH
        0.50, -- cost price
        8.00 -- retail price
    ),
    (
        'CCI02HDMI', (SELECT id FROM manufacturers WHERE short_brand_name = 'OB'),
        '2m HDMI Cable',
        NULL,
        (SELECT id FROM product_types WHERE name = 'HDMI cable'),
        NULL, -- screen size
        38, -- SOH
        1.00, -- cost price
        12.00 -- retail price
    ),
    (
        'CCI05HDMI', (SELECT id FROM manufacturers WHERE short_brand_name = 'OB'),
        '5m HDMI Cable',
        NULL,
        (SELECT id FROM product_types WHERE name = 'HDMI cable'),
        NULL, -- screen size
        6, -- SOH
        2.50, -- cost price
        16.00 -- retail price
    ),
    (
        'CCI10HDMI', (SELECT id FROM manufacturers WHERE short_brand_name = 'OB'),
        '10m HDMI Cable',
        NULL,
        (SELECT id FROM product_types WHERE name = 'HDMI cable'),
        NULL, -- screen size
        20, -- SOH
        5.00, -- cost price
        25.00 -- retail price
    ),
    (
        'WVP_WM_48', (SELECT id FROM manufacturers WHERE short_brand_name = 'WVP'),
        'WVP Wall mount',
        'WVP Wall mount up to 48"',
        (SELECT id FROM product_types WHERE name = 'Wall mount'),
        48, -- screen size
        4, -- SOH
        15.00, -- cost price
        25.00 -- retail price
    ),
    (
        'WVP_WM_85', (SELECT id FROM manufacturers WHERE short_brand_name = 'WVP'),
        'WVP Wall mount',
        'WVP Wall mount up to 85"',
        (SELECT id FROM product_types WHERE name = 'Wall mount'),
        85, -- screen size
        4, -- SOH
        50.00, -- cost price
        80.00 -- retail price
    ),
    (
        'Soundbar', (SELECT id FROM manufacturers WHERE short_brand_name = 'Shrub'),
        'Shrub Soundbar',
        NULL,
        (SELECT id FROM product_types WHERE name = 'Soundbar'),
        NULL, -- screen size
        0, -- SOH
        40.00, -- cost price
        55.00 -- retail price
    ),
    (
        'SB_BT', (SELECT id FROM manufacturers WHERE short_brand_name = 'Shrub'),
        'Shrub Bluetooth SB',
        'Shrub Soundbar with bluetooth',
        (SELECT id FROM product_types WHERE name = 'Soundbar'),
        NULL, -- screen size
        1, -- SOH
        55.00, -- cost price
        85.00 -- retail price
    ),
    (
        '10310', (SELECT id FROM manufacturers WHERE short_brand_name = 'Shrub'),
        '10" DVD Player',
        '',
        (SELECT id FROM product_types WHERE name = 'Television'),
        10, -- screen size
        16, -- SOH
        50.00, -- cost price
        65.00 -- retail price
    ),
    (
        '670032', (SELECT id FROM manufacturers WHERE short_brand_name = 'Blue'),
        'BP 28" LCD TV',
        'BluePoint 28" LCD TV',
        (SELECT id FROM product_types WHERE name = 'Television'),
        28, -- screen size
        0, -- SOH
        100.00, -- cost price
        170.00 -- retail price
    ),
    (
        '680048', (SELECT id FROM manufacturers WHERE short_brand_name = 'Blue'),
        'BP 32" LCD TV',
        'BluePoint 32" LCD TV',
        (SELECT id FROM product_types WHERE name = 'Television'),
        32, -- screen size
        15, -- SOH
        120.00, -- cost price
        175.00 -- retail price
    ),
    (
        '685548', (SELECT id FROM manufacturers WHERE short_brand_name = 'Blue'),
        'BP 32" LCD TV',
        'BluePoint 32" LCD TV with smart',
        (SELECT id FROM product_types WHERE name = 'Television'),
        32, -- screen size
        7, -- SOH
        160.00, -- cost price
        255.00 -- retail price
    ),
    (
        '690055', (SELECT id FROM manufacturers WHERE short_brand_name = 'Blue'),
        'BP 48" LCD TV',
        'BluePoint 48" LCD TV',
        (SELECT id FROM product_types WHERE name = 'Television'),
        48, -- screen size
        8, -- SOH
        160.00, -- cost price
        260.00 -- retail price
    );

UPDATE products SET discontinued = TRUE WHERE
    mpn IN ('WVP_WM_48', 'WVP_WM_85', 'Soundbar', '670032', '680048');