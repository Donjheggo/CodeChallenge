def checkStepNumbers(systemNames, stepNumbers):
    systems = {} 
    for i in range(len(systemNames)): 
        if systemNames[i] in systems: 
            systems[systemNames[i]].append(stepNumbers[i]) 
        else:
            systems[systemNames[i]] = [stepNumbers[i]] 
    for system in systems: 
        steps = systems[system] 
        for i in range(1, len(steps)): 
            if steps[i] <= steps[i-1]: 
                return False 
    return True


systemNames = ["tree_1", "tree_2", "house", "tree_1", "tree_2", "house"]
stepNumbers = [1, 33, 10, 2, 44, 20]

print(checkStepNumbers(systemNames, stepNumbers))