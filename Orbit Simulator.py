class SpaceDebri: 

	G = (6.67408)*10**(-11) ## Gravitational constant 
	dt = 0.0001 			## "small" change in time (sec)
	ds = 0.0001				## "small" change in position (meters)

	def __init__(self, mass, position, velocity, acceleration): 
		self.mass = mass
		self.position = position
		self.velocity = velocity
		self.acceleration = acceleration
		
	def dist(self, other):
		x1 = self.position[0]
		x2 = other.position[0]
		y1 = self.position[1]
		y2 = other.position[1]
		z1 = self.position[2]
		z2 = other.position[2]

		R = ((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)**(0.5)
		return R

	def time_evolve(self)
		pass


	@classmethod
	def from_string(cls, string_data):
		mass, pos_x, pos_y, pos_z, vel_x, vel_y, vel_z, acc_x, acc_y, acc_z = string_data.split(" ")
		
		pos = [float(pos_x),float(pos_y),float(pos_z)]
		vel = [float(vel_x),float(vel_y),float(vel_z)]
		acc = [float(acc_x),float(acc_y),float(acc_z)]

		self.mass = float(mass)
		self.position = pos
		self.velocity = vel
		self.acceleration = acc
		
