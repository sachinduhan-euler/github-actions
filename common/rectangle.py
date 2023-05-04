class Rectangle:
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width
    
    def area(self) -> float:
        return round(self.length * self.width,2)
    
    def perimeter(self) -> float:
        return round(2 * (self.length + self.width),2)

