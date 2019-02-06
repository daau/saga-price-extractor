class Writer():
  def __init__(self, directory):
    self.f = open(directory, 'w')

  def write(self, text):
    self.f.write(text + "\n")

  def save(self):
    self.f.close()