from random import uniform
from geometricObjects.convexHull import ConvexHull
from userInterface.userInputManager import UserInputManager

def main():
	runConvexHull()


def runConvexHull():
	locations = getInput()
	convexHull = ConvexHull()
	convexHull.runAlgorithm()


def getInput():
	inputMode = UserInputManager.stringInput("How would you like to input points?", ["random", "from file"])
	if inputMode == "random":
		locations = inputByPointGeneration()

	elif inputMode == "from file":
		locations = inputFromFile()

	else:
		raise Exception("The input format given was invalid.")
	
	return locations


def inputFromFile():
	fileName = input("Please enter the name of the file: ")
	fileHandle = open(fileName, "r")
	locations = [[float(comp) for comp in line.split()] for line in fileHandle.readlines()]
	fileHandle.close()
	return locations


def inputByPointGeneration():
	dimensions = UserInputManager.intInput("How many spatial dimensions should this convex hull exist in?", min=1)
	numPoints = UserInputManager.intInput("How many points should be generated?", min=1)
	locations = generatePoints(dimensions, numPoints)
	return locations


def generatePoints(dimensions, numPoints):
		locations = []
		for dim in range(dimensions): 
			for pointN in range(numPoints):
				pointFound = False
				while not pointFound:
					point = [uniform() for dim in range(dimensions)]
					if sum(component*component for component in point) <= 1:
						locations.append(point)
						pointFound=True
		return locations



if __name__ == '__main__':
	main()