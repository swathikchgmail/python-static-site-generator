import path from pathlib

class Site():
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest


   def create_dir(self, path):
       directory(self.dest, self.source / relative_to())
       mkdir(True, True)

   def build(self)
       for path in self.source.rglob("*")
           if(path == directory):
               create_dir(path)
