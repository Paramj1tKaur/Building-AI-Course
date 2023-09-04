""" Logistic: sigmoid function. """ 
def sigmoid(x):
	return 1 / (1 + math.exp(-x))

# alternatively

def sigmoid(x):
	x2 = -1.0*x
	a = math.exp(x2)
	nominator = 1
	denominator = 1 + a
	return nominator / denominator
