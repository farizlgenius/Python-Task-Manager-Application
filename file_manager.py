import json

file_path = 'data.json'

class FileManager:
  def __init__(self):
    pass

  def read_file(self):
    with open(file_path,'r') as file:
      content = file.read()
    return json.loads(content)

  def write_file(self, data):
    with open(file_path, 'w') as file:
      json.dump(data, file, indent=4)