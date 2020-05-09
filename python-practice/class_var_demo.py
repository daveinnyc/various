class DemoVariableTypes:
    # Class variable, belongs to entire DemoVariableTypes class
    class_var_count = 0
    
    def __init__(self, name):
        # Set initial values for instance variables   
        self.name = name
        self.instance_count = self.class_var_count
        
        # Update the class variable, not the instance variable
        DemoVariableTypes.class_var_count += 1
    
# Run standalone
if __name__ == "__main__":
    # Create some instances
    instance1 = DemoVariableTypes("one")
    instance2 = DemoVariableTypes("two")
    instance3 = DemoVariableTypes("three")


    # Show the instance variable incremented with each new instance   
    print(f"Instance: {instance1.name} iv count: {instance1.instance_count}")
    print(f"Instance: {instance2.name} iv count: {instance2.instance_count}")
    print(f"Instance: {instance3.name} iv count: {instance3.instance_count}")
    
    
    # Show the class variable is the same for each instance
    print("")
    print(f"Instance: {instance1.name} cv count: {instance1.class_var_count}")
    print(f"Instance: {instance2.name} cv count: {instance2.class_var_count}")
    print(f"Instance: {instance3.name} cv count: {instance3.class_var_count}")
    