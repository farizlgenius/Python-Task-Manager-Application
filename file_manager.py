import json

file_path = 'data.json'

# File Manager Class
# Responsible for reading and writing data to the JSON file
class FileManager:
  def __init__(self):
    pass

  # Read data from the JSON file
  def read_file(self):
    with open(file_path,'r') as file:
      content = file.read()
    return json.loads(content)

  # Write data to the JSON file
  def write_file(self, data):
    with open(file_path, 'w') as file:
      json.dump(data, file, indent=4)