import copy

class Prototype:
    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        self._objects[name] = obj

    def unregister_object(self, name):
        del self._objects[name]

    def clone(self, name, **attr):
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj

class A:
    def __init__(self):
        self.x = 1
        self.y = 2
        self.z = 3
    def __str__(self):
        return 'x={} y={} z={}'.format(self.x, self.y, self.z)

a = A()
prototype = Prototype()
prototype.register_object('objecta', a)
b = prototype.clone('objecta', x=4, y=5, z=6)
print(a)
print(b)
