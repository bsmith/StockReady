# Get Your ‘StockReady’ for Black Friday!

In the Technology Retail trade, Black Friday is a massive opportunity to sell televisions and accessories.
Shopkeepers need to get their shop ready for Black Friday, and be able to find products for customers on the day itself.
On a mobile device, they need to record and count their inventory. They need to find products to sell to customers.
On a PC, they need to see a report of their current stock.

App name: StockReady

Build an app which allows a shopkeeper to track their shop's inventory.
This is not an app which the customer will see, it is an admin/management app for the shop workers.

## MVP

* The inventory should track individual ‘products’, including a manufacturer product number (MPN), description, type (TV, cable, mount, etc), screen size (if applicable), stock quantity, cost price, and retail price.

* The inventory should track ‘manufacturers’, including a name, contact details for trade, contact details for customers (eg. telephone and website).

* The inventory should track ‘product types’ which just have names (eg. television, hdmi cable, wall mount).

* You should be able to create and edit manufacturers, products, product types separately. \[6 items]

* Show an inventory page, listing all the details for all the products in stock in a single view.

* Show a details page for each manufacturer and product. \[2 items]

    * (Product types don’t need a details page as they only have a ‘name’.)

* As well as showing stock quantity as a number, the app should visually highlight "low stock" and "out of stock" items to the user.

Inspired by: Argos, Currys, RicherSounds, John Lewis

## Possible Extensions

1. Filter the inventory list to show only one product type.

2. On the product detail page for televisions, show the next smaller and the next
larger television by the same manufacturer.

3. Show a list of all manufacturers, with links to the manufacturer detail page, and a
separate page listing all the products of that manufacturer.

4. Mark products as active/discontinued. Discontinued products with stock should be
highlighted in the product list. Allow the user to select if discontinued-with-no-stock products are hidden in the product list.

    * Separate page just listing all the discontinued products that still have stock.

5. The Shop has opened a second location! Track ‘Branches’, allowing them to be
listed and edited. ‘Stock quantity’ will need to be moved to be held against each
product in each location (many-to-many).

6. On the product edit page, don’t just have a ‘stock quantity’ box: have separate
boxes for sold, stolen and deliveries.

    * Track these in the database, and calculate the values sold (based on retail
price), stolen and bought (based on cost price). Show the profit/(loss).
