# class Coffee:
#     def __init__(self, name):
#         self.name = name
        
#     def orders(self):
#         pass
    
#     def customers(self):
#         pass
    
#     def num_orders(self):
#         pass
    
#     def average_price(self):
#         pass

# class Customer:
#     def __init__(self, name):
#         self.name = name
        
#     def orders(self):
#         pass
    
#     def coffees(self):
#         pass
    
#     def create_order(self, coffee, price):
#         pass
    
# class Order:
#     def __init__(self, customer, coffee, price):
#         self.customer = customer
#         self.coffee = coffee
#         self.price = price



class Coffee:
    def __init__(self, name):
        self._name = name
    
    def get_name(self):
        return self._name
    def set_name(self, val):
        if isinstance(val, str) and 3 <= len(val) and not hasattr(self, 'name'):
            self._name = val
        else:
            TypeError("Name must be a string above 3 characters ")
    name = property(get_name, set_name)
    

    def orders(self):
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        return list(set([order.customer for order in self.orders()]))

    
    def num_orders(self):
        return len(self.orders())
    
    
    def average_price(self):
        if len(self.orders()) == 0:
            return 0
        total = sum([order.price for order in self.orders()])
        return total / len(self.orders()) 

            



class Customer:

    def __init__(self, name):
        self._name = name
    def get_name(self):
        return self._name
    
    def set_name(self, val):
        if isinstance(val, str) and 1 <= len(val) <= 15:
            self._name = val
        else:
            TypeError("Name must be a string between 1-15 characters ")
    name = property(get_name, set_name)
        

    def orders(self):
        return [order for order in Order.all if order.customer == self]

    
    def coffees(self):
        return list(set([order.coffee for order in  self.orders()]))
    
    def create_order(self, coffee, price):
        new_order = Order(self, coffee, price)
        return new_order





class Order:
    all = []
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)
    
    def get_price(self):
        return self._price
     
    def set_price(self, val):
        if isinstance(val, float) and 1.0  <= val <= 10.0 and not hasattr(self, 'price'):
            self._price = val
        
    price = property(get_price, set_price)

 