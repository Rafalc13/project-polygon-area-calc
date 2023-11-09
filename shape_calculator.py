class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height
    #print('without self ', width, height)
    #print("with self", self.width, self.height)

  def set_width(self, width):
    self.width = width
    #print("set width", width)

  def set_height(self, height):
    self.height = height
    #print("set height", height)

  def get_area(self):
    #print('set_area', self.width * self.height)
    return self.width * self.height
    
  def get_perimeter(self):
    #print('set_perimeter', 2 * self.width + 2 * self.height)
    return 2 * self.width + 2 * self.height
    
  def get_diagonal(self):
    #print('get_diagonal', (self.width ** 2 + self.height ** 2) ** 0.5)
    return (self.width ** 2 + self.height ** 2) ** 0.5

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return 'Too big for picture.'
    else:
      shape = ''
      for line in range(self.height):
        shape += '*' * self.width + '\n'
        #print('get_picture', shape)
      return shape

  def get_amount_inside(self, shape):
    if isinstance(shape, Square) or isinstance(shape, Rectangle):
      return (self.width // shape.width) * (self.height // shape.height)
    else:
      return 0

  def __str__(self):
    return f'Rectangle(width={self.width}, height={self.height})'

class Square(Rectangle):
  def __init__(self, side):
    super().__init__(side, side)
    #print('tryouts ', super().__init__(side, side))

  def set_side(self, side):
    self.width = side
    self.height = side
    #print('set_side', side)

  def set_width(self, width):
    self.width = width
    #print('set_width_II', self.width)

  def set_height(self, height):
    self.height = height
    #print('set_height_II', self.height)

  def __str__(self):
    return f'Square(side={self.width})'