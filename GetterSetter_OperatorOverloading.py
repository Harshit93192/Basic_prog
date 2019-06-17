''' Create a class for username and password and create a object to check if they are equal and 
use operator overloading to check if both users are equal or not. username should start with e\E and 
password should start with caps by use of property '''

class Validate:
  def __init__(self, username, password):
    self.username = username
    self.password = password

  def __eq__(self, other):
    if self.username == other.username and self.password  == other.password:
      print ('Congartulation!, you have entered the correct username and password')
	  
  def get_username(self):
    return self._username
	  
  def set_username(self, value):
    if value[0] != 'e' and value[0] != 'E':			# Checking if the initial digit of username starts with e or E
      raise ValueError("Username entered is not valid")
    self._username = value

  def get_password(self):
    return self._password
	
  def set_password(self, data):
    if data[0].islower():					# Checking if the first digit of password is in caps or not
      raise ValueError('Entered password is not valid')
    self._password = data

  def __str__(self):
    return ('username {} and password {}'.format(self.username, self.password))
	
  username = property(get_username, set_username)		# Creating a property object by using property function
  password = property(get_password, set_password)
    
a = Validate('EHITGTA', 'QWER')
print (a)
b = Validate('EHITGTA', 'QWER')
print(b)
c = Validate('EHITGTA', 'RWER')
a == b
a == c
