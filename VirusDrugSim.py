#
# PROBLEM 5
#
def simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, numTrials):
    """
    Runs simulations and plots graphs for problem 5.

    For each of numTrials trials, instantiates a patient, runs a simulation for
    150 timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end plots the average virus population size
    (for both the total virus population and the guttagonol-resistant virus
    population) as a function of time.

    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1). 
    numTrials: number of simulation runs to execute (an integer)
    
    """
    timeSteps=300
    avgPop={}
    avgResPop={}
    for j in range(timeSteps):
        avgPop[j]=[]
        avgResPop[j]=[]
    
    
    virus=ResistantVirus(maxBirthProb,clearProb,resistances,mutProb)
    infection=[]
    for k in range(numViruses):
        infection.append(virus)
    
    
    for i in range(numTrials):
        victim=TreatedPatient(infection,maxPop)
        for j in range(timeSteps):
            if j == 149: #administer drug
                victim.addPrescription('guttagonol')   
            avgPop[j].append(victim.getTotalPop())
            avgResPop[j].append(victim.getResistPop(['guttagonol']))
            victim.update()


    #plot
    PopPlot=[]
    ResPopPlot=[]
    for k,v in sorted(avgPop.items()):
        PopPlot.append(float(sum(v))/len(v))
    for k,v in sorted(avgResPop.items()):
        ResPopPlot.append(float(sum(v))/len(v))
    print(PopPlot)
    print(ResPopPlot)
    pylab.plot(range(len(PopPlot)),PopPlot,label='Total Population')
    pylab.plot(range(len(PopPlot)),ResPopPlot,label='Resistant Population')
    pylab.title('Average Virus Population During Simulation')
    pylab.xlabel('Time Step')
    pylab.ylabel('Average Virus Population')
    pylab.legend()
    pylab.show()