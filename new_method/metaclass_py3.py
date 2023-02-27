class ExampleMetaClass(type):
    pass

class SubClass(metaclass=ExampleMetaClass):
    pass

subclass_object = SubClass()

print(f"subclass_object's class is: {subclass_object.__class__}")
print(f"SubClass's class is: {SubClass.__class__}")
print(f"ExampleMetaClass's class is {subclass_object.__class__.__class__.__class__}")
