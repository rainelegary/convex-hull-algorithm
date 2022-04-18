import math

class UserInputManager:
    @classmethod
    def stringInput(cls, prompt, optionsList):
        optionsString = cls.stringOptions(optionsList)
        while True:
            response = input(prompt + optionsString)
            if response.lower() in optionsList:
                return response
            else:
                print("Invalid input, please try again.")

    
    @classmethod
    def intInput(cls, prompt, min=-math.inf, max=math.inf):
        optionsString = cls.intOptions(min,max)
        while True:
            try:
                num = int(input(prompt + optionsString))
                if min <= num and num <= max: 
                    return num
                else:
                    print("Please select a number within the bounds.")
            except:
                print("number entered is not an integer.")

            
    @classmethod
    def stringOptions(cls, optionsList):
        optionsString = " (options: "
        for i in range(len(optionsList) - 1):
            optionsString += optionsList[i] + ", "
        optionsString += optionsList[-1] + ")"
        return optionsString


    @classmethod
    def intOptions(cls, min, max):
        return " (min: " + str(min) + ", max: " + str(max) + ")"
        


    
    
        