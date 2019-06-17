# Maintaing the Dictionary of Employee Date of Birth by using Inner classes concept

class Employee:
	def __init__(self, ename):
		self.name = ename
		print('Enter the Date of Birth of ',self.name)
		dd = int(input('Enter the Date in dd format: '))		# Enter the date of birth of Employee
		mm = int(input('Enter the Month in mm format: '))
		yyyy = int(input('Enter the Year in yyyy format: '))
		self.dob = self.DOB(dd,mm,yyyy,self.name)
		
	def display(self):
		self.dob.display()
		
	class DOB:
		def __init__(self, dd, mm, yyyy,name):
			self.dd = dd
			self.mm = mm
			self.yyyy = yyyy
			self.dd = self.ddate()
			self.yyyy = self.yyear()
			self.name = name
		def ddate(self):
			if self.mm == 1 or self.mm == 3 or self.mm ==  5 or self.mm == 7 or self.mm == 8 or self.mm == 10 or self.mm == 12:
				if self.dd > 0 and self.dd  < 32:
					return self.dd
				else:
					raise ValueError('Enter the date correctly')
			elif self.mm == 4 or self.mm == 6 or self.mm == 9 or self.mm == 11:
				if self.dd > 0 and self.dd  < 31:
					return self.dd
				else:
					raise ValueError('Enter the date correctly')
			elif self.mm == 2 and self.yyyy% 4 == 0 and self.yyyy%100 == 0 and self.yyyy%400 == 0:
				if self.dd > 0 and self.dd  < 30:
					return self.dd
				else:
					raise ValueError('Enter the date correctly')
			elif self.mm == 2 and self.yyyy% 4 == 0 and self.yyyy%100 == 0:
				if self.dd > 0 and self.dd  < 29:
					return self.dd
				else:
					raise ValueError('Enter the date correctly')
			elif self.mm == 2 and self.yyyy%4 == 0:
				if self.dd > 0 and self.dd  < 30:
					return self.dd
				else:
					raise ValueError('Enter the date correctly')
			elif self.mm == 2 and self.yyyy%4 != 0:
				if self.dd > 0 and self.dd  < 29:
					return self.dd
				else:
					raise ValueError('Enter the date correctly')
			else:
				raise ValueError('Enter the month correctly')
		def yyear(self):
			if len(str(self.yyyy)) == 4:
				return self.yyyy
			else:
				raise ValueError('Enter the year in correct format')
		def display(self):
			Edict[self.name] = '{}/{}/{}'.format(self.dd,self.mm,self.yyyy)
			print(Edict)


def decorator(somefunction):
	def wrapper(name, password):
		if name == 'harshit' and password == 'harshit':
			somefunction(name, password)
		else:
			print(' You are not authorized')
	return wrapper

@decorator
def authentic(a,b):
	print('Welcome to Employee Date of Birth Database')
	n = int(input('Enter the no. of Employees: '))
	for i in range(n):	
		ename = input('Enter the name of the employee: ')
		p = Employee(ename)
		p.display()

Edict = {}
username = input('Enter your name: ')
password = input('Enter the password: ')
authentic(username, password)
