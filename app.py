print('Tutorial to Git')
print('neweracy')


class my_class():
    def __init__(self,y):
        self.y = y
    
    def my_method(self):
        return f'value : {self.y}'
    
value = my_class(12)
     
print(value.my_method())