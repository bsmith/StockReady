```mermaid
classDiagram
    class manufacturer_repository {
        select(id)
        select_all()
        delete(id)
        delete_all()
        save(Manufacturer)
        update(Manufacturer)
        select_products_of_manufacturer(Manufacturer)
    }
    class product_repository {
        select(id)
        select_all()
        delete(id)
        delete_all()
        save(Product)
        update(Product)
        select_discontinued_stocked_products()
        select_related_products(Product)
    }
    class product_type {
        select(id)
        select_all()
        delete(id)
        delete_all()
        save(ProductType)
        update(ProductType)
        select_products_of_type(ProductType)
    }
