class Product:
    # this is the constructorوmagic Method for the Product class ,we create a magic Method : __name__
    def __init__(self, price, name, count):
        self.__price = price
        self.__CountProduct = count
        self.__ProductName = name

    # ===============================================   properties =================================

    # ===============================================   Name  ======================================
    # ProductName property
    def get_ProductName(self):  # getter
        return self.__ProductName

    def set_ProductName(self, value):  # setter
        self.__ProductName = value

    # property has 4 arguments   get_ite,set_item,delete_item,documentation
    # return the object that can set and get the ProductName
    ProductName = property(get_ProductName, set_ProductName)
    # ===============================================   price  =====================================
    # price property

    def get_prices(self):  # getter
        return self.__price

    def set_prices(self, value):  # setter
        if value < 0:
            raise ValueError("this is not a valid price")
        self.__price = value

    # property has 4 arguments   get_ite,set_item,delete_item,documentation
    # return the object that can set and get the prices
    price = property(get_prices, set_prices)
    # ===============================================   count =========================================
    # Count property

    def get_Count(self):  # getter
        return self.__CountProduct

    def set_Count(self, value):  # setter
        if value < 0:
            raise ValueError("this is not a valid price")
        self.__CountProduct = value

    # property has 4 arguments   get_ite,set_item,delete_item,documentation
    # return the object that can set and get the count
    CountProduct = property(get_Count, set_Count)
    # ===============================================


myProduct = Product(name='kola', count=10, price=25000)
print("name is : ", myProduct.ProductName)  # call get_ProductName(self):
print("count is : ", myProduct.CountProduct)  # call get_Count(self):
print("price is : ", myProduct.price)  # call get_prices(self):
# myProduct.price = 10  # call set_prices(self):
# myProduct.price=-10 #show an error message
