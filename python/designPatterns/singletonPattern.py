'''
Purpose: Singleton Pattern
    - Ensure a class has only one instance, and provide a global point of access to it.
    - There are many different ways to implement the singleton pattern in Python. We will use the Borg pattern.
    - The Borg pattern is a way to share state between objects while ensuring that only one object is created.
'''

class Borg:
    _shared_state = {}
    def __init__(self):
        '''
        Share the instance's attribute namespace with other instances of the Borg class, and any changes made to the attributes of one instance will be visible to all other instances.

        In Python, each object has an attribute namespace, which is a dictionary that maps attribute names to their corresponding values. This namespace is accessible through the object's __dict__ attribute.

        For example, if you have an object obj with an attribute x, you can access the attribute's value using the expression obj.x. Behind the scenes, this is equivalent to accessing the value in the object's __dict__ dictionary using the key 'x': obj.__dict__['x'].
        '''
        self.__dict__ = self._shared_state

class Singleton(Borg):
    def __init__(self, **kwargs):
        Borg.__init__(self)
        self._shared_state.update(kwargs)

    def __str__(self):
        return str(self._shared_state)

if __name__ == '__main__':
    x = Singleton(HTTP='Hyper Text Transfer Protocol')
    print(x)
    y = Singleton(SNMP='Simple Network Management Protocol')
    print(y) # though y is a new instance, it shares the same state as x which means that the value of HTTP is also available in obj y

    # update the shared state
    z = Singleton(HTTP='New Value')
    print(z)