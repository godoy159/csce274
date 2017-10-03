import interface

def main():

  commands = interface()

  commands.connect()
  print "setting the robot to start"	
  comands.write_raw(128)

  commands.drive()
