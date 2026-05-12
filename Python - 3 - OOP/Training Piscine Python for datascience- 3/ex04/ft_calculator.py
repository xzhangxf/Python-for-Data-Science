class calculator:
    """Calculator for vector operations: dot product, addition, subtraction."""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        '''Calculate the dot product of two vectors.'''
        result = sum(x * y for x, y in zip(V1, V2))
        print(f"Dot product is: {result}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        '''Add two vectors element-wise.'''
        result = [float(x + y) for x, y in zip(V1, V2)]
        print(f"Add Vector is : {result}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        '''Subtract vector V2 from vector V1 element-wise.'''
        result = [float(x - y) for x, y in zip(V1, V2)]
        print(f"Sous Vector is: {result}")
