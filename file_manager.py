import json

class FileManager:
  def __init__(self,file_path):
    self.file_path = file_path

  def read_file(self):
    with open(self.file_path,'r') as file:
      content = file.read()
    return json.loads(content)

  def write_file(self, data):
    with open(self.file_path, 'w') as file:
      json.dump(data, file, indent=4)