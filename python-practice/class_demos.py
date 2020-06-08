# Notes on classes


class Sample():
    def __init__(self, name, number):
        self.name = name
        self.number = number
        
    def print_values(self):
        print(f"name: {self.name}")
        print(f"number: {self.number}")


class SampleWithProperties():
    def __init__(self, name, number):
        self.__name = name
        self.__number = number
        
    @property
    def name(self):
        # double underscore is to tell future devs to avoid variable
        return self.__name
    
    @property
    def double_name(self):
        # Can return calculated or other values besides fields
        return 2 * self.__name


    @property
    def number(self):
        return self.__number
   
    @name.setter
    def name(self, value):
        # Often has some ort of validation or transformation code
        self.__name = value
        

    @number.setter
    def number(self, value):
        # Often has some ort of validation or transformation code
        self.__number = value % 2
        

class MoreProperties():
    def __init__(self, nname):
        self.name = nname
        
    @property
    def name(self):
        # double underscore is to tell future devs to avoid variable
        return self.__name
      
    @name.setter
    def name(self, value):
        # Often has some ort of validation or transformation code
        self.__name = value
        
        
if __name__ == "__main__":
    '''
    # Demo Sample()
    instance = Sample("fred", 3)   
    instance.print_values()
    print(f"Access name field directly: {instance.name}")
    instance.number += 100
    print(f"Access number field directly: {instance.number}")
    '''

    '''    
    # Demo SampleWithProperties()
    instance_with_props = SampleWithProperties("fred", 3)   
    # Directly accessing values
    #    Next line fails
    #    print(f"Access name field, direct: {instance_with_props.__name}")
    # Python rewrites value names with intial __ to protect namespace
    #    not really a private value, but less likely to be accessed
    print(f"Access name field, direct: {instance_with_props._SampleWithProperties__name}")
    # Using getter to access values, looks like direct access but isn't
    #    name field
    print(f"Access name field, getter: {instance_with_props.name}")
    print(f"Access name field, getter: {instance_with_props.double_name}")
    instance_with_props.name = "Barney"
    print(f"Access name field, after setter: {instance_with_props.name}")
    #    number field
    print(f"Access number field, before setter: {instance_with_props.number}")    
    instance_with_props.number = 4
    print(f"Access number field, after setter: {instance_with_props.number}")
    instance_with_props.number = 3
    print(f"Access number field, after setter: {instance_with_props.number}")
    '''
    
    # Demo MoreProperties()
    #    Figure out why self.value doesn't work and self.__value does in prior examples
