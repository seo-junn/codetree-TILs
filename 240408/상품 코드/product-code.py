class Product:
    def __init__(self,name='',code=''):
        self.product_name = name
        self.product_code = code
    
    def __str__(self):
        return "product " + self.product_code + " is " + self.product_name

p1 = Product("codetree","50")
p2 = Product()
name,code = input().split()
p2.product_name = name
p2.product_code = code

print(p1)
print(p2)