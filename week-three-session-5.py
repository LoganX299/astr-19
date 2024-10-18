import numpy as np
import math

def main():
	circle = np.linspace(0, 2 * math.pi, 1000)

	for i in circle:
		print(f"x: {i} sin(x): {math.sin(i)}")

if __name__=="__main__":
	main()