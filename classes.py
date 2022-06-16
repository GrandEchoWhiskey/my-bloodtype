BLOOD_TRAIT = ['A', 'B', '0']
RH_TRAIT = ['+', '-']

RECESIVE_PROBS = 2/3

class Person:
	def __init__(self, bloodtype: list, name='Unnamed'):
		self.bloodtype: list = bloodtype
		self.name = name

	def __str__(self):
		result = f'Preson {self.name}:\n'
		for bt in self.bloodtype:
			result += f"{bt['type'].rjust(2, ' ')}{bt['rh'].ljust(2, ' ')} : "
			result += "{0:>7.2f}%".format(bt['prc'])
		return result
	
	def inherit(self, parent1, parent2):
		return

	def count_probs(self, other):
		return
	
def get_prob_list(bloodtype):
