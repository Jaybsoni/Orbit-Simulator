class SpaceDebri():  # Quick Update

	@staticmethod
	def mass_to_size(mass):
		# given some space debri with mass it determines its "size"
		radius = mass/1000
		return radius

	def __init__(self, mass, position, velocity, acceleration):
		"""
		:param mass: float
		:param position: list of floats
		:param velocity: list of floats
		:param acceleration:  list of floats

		Initializes an instance of the SpaceDebri object with above specifications
		"""
		self.mass = mass
		self.position = position
		self.velocity = velocity
		self.acceleration = acceleration
		self.radius = SpaceDebri.mass_to_size(mass)
		
	def dist(self, other):
		"""
		:param other:
		:return:
		calculates the distance between two instances of the spacedebri objects
		"""

		x1 = self.position[0]
		x2 = other.position[0]
		y1 = self.position[1]
		y2 = other.position[1]
		z1 = self.position[2]
		z2 = other.position[2]

		r = ((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)**0.5
		return r

	def update_position(self):
		# updates the position field based on the velocity of the space debri (time evolves it)
		delta_x = (self.velocity[0])*self.dt
		delta_y = (self.velocity[1])*self.dt
		delta_z = (self.velocity[2])*self.dt

		new_x = self.position[0] + delta_x
		new_y = self.position[1] + delta_y
		new_z = self.position[2] + delta_z

		self.position = [new_x, new_y, new_z] 

		# print("The new position is ({},{},{})".format(new_x,new_y,new_z)) for debug purposes

	@classmethod
	def from_string(cls, string_data):
		# alternate constructor of instances of space debri (to easily make instances via .txt or .csv files)
		mass, pos_x, pos_y, pos_z, vel_x, vel_y, vel_z, acc_x, acc_y, acc_z = string_data.split(" ")
		
		pos = [float(pos_x), float(pos_y), float(pos_z)]
		vel = [float(vel_x), float(vel_y), float(vel_z)]
		acc = [float(acc_x), float(acc_y), float(acc_z)]

		return cls(float(mass), pos, vel, acc, mass_to_size(float(mass)))

	def update_velocity(self):
		# updates the velocity of the space debri via the acceleration
		delta_x = (self.acceleration[0]) * self.dt
		delta_y = (self.acceleration[1]) * self.dt
		delta_z = (self.acceleration[2]) * self.dt

		new_x = self.velocity[0] + delta_x
		new_y = self.velocity[1] + delta_y
		new_z = self.velocity[2] + delta_z

		self.velocity = [new_x, new_y, new_z]

	def collision_check(self, other):
		# determines if the space debri instance is within contact distance of another piece of space debri
		distance = self.dist(other)
		radius1 = self.radius
		radius2 = other.radius

		if (radius1 + radius2) >= distance:
			return True

	def relative_position_vector(self, other):
		# returns a lst of positions which corresponds to the vector going from self --> other and vice versa
		x1 = self.position[0]
		x2 = other.position[0]
		y1 = self.position[1]
		y2 = other.position[1]
		z1 = self.position[2]
		z2 = other.position[2]

		S_O = [(x2 - x1), (y2 - y1), (z2 - z1)] 
		O_S = [-1*S_O[0], -1*S_O[1], -1*S_O[2]]
		return S_O, O_S