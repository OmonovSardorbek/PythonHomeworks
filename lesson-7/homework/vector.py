class Vector:
    def __init__(self, *components):
        self.components = tuple(components)
    
    def __repr__(self):
        return f"Vector{self.components}"
    
    def __add__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions for addition.")
        return Vector(*(a + b for a, b in zip(self.components, other.components)))
    
    def __sub__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions for subtraction.")
        return Vector(*(a - b for a, b in zip(self.components, other.components)))
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(*(other * a for a in self.components))
        elif isinstance(other, Vector):
            if len(self.components) != len(other.components):
                raise ValueError("Vectors must have the same dimensions for dot product.")
            return sum(a * b for a, b in zip(self.components, other.components))
        else:
            raise TypeError("Operand must be a scalar or a Vector.")
    
    def __rmul__(self, scalar):
        return self * scalar

    def magnitude(self):
        return (sum(a**2 for a in self.components))**0.5

    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector.")
        return Vector(*(a / mag for a in self.components))

    def __len__(self):
        return len(self.components)