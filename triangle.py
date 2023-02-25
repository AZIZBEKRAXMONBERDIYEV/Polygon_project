from math import sqrt


class Triangle:
    def __init__(self, a:float, b:float, c:float):
        self.a = a
        self.b = b
        self.c = c

    def is_valid(self) -> bool:
        '''
        This method checks if the triangle is valid.
        
        Args: 
            No
        Returns:
            bool: True if the triangle is valid, False otherwise
        '''
        return self.a > 0 and self.b>0 and self.c>0
    
    def get_type(self) -> str:
        '''
        This method finds the type of the triangle.

        Note: typies are 'Teng yonli', 'Teng tomonli', 'Turli tomonli'
        '''
        if self.a ==self.b or self.a == self.c or self.b == self.c:
            return "Teng yonli"
        if self.a == self.b and self.a == self.c:
            return "Teng tomonli"
        if self.a != self.b or self.a != self.c or self.b != self.c:
            return "Turli tomonli"
        
    def perimeter(self) -> float:
        '''
        This method finds the perimeter of the triangle.
        Args:
            No
        Returns:
            float: return perimeter of the triangle if the triangle is valid, 0 otherwise
        '''
        if self.is_valid():
            return self.a + self.b + self.c
        else:
            return 0

    def area(self) -> float:
        '''
        This method finds the area of the triangle.
        Args:
            NO
        Returns:
            float: return area of the triangle if the triangle is valid, 0 otherwise
        '''
        x = (self.a+self.b+self.c)/2
        if self.is_valid():
            return sqrt(x*(x-self.a)*(x-self.b)*(x-self.c))