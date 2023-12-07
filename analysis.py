# analysis.py
# -----------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


######################
# ANALYSIS QUESTIONS #
######################

# Set the given parameters to obtain the specified policies through
# value iteration.

def question2():
    answerDiscount = 0.9
    answerNoise = -1
    return answerDiscount, answerNoise

def question3a():
    #Prefira a saída próxima (+1), arriscando o precipício (-10)
    answerDiscount = 0.1 #indicando que recompensas futuras são menos significativas 
    answerNoise = 0 # noise 0 para prosseguir logo para o caminho mais rapido
    answerLivingReward = 0.5  #valor baixo para ir para o reward 1
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'


def question3b():
    #Prefira a saída próxima (+1), mas evitando o penhasco (-10)
    answerDiscount = 0.3 # aumentar a significatividade das recompensas futuras
    answerNoise = 0.2 # noise em 0.2 para confundir, fazendo para tomar o caminho mais longo
    answerLivingReward = 0.1 #valor baixo para ir para o reward 1
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3c():
    #Prefira a saída mais distante (+10), arriscando o precipício (-10)
    answerDiscount = 0.1 
    answerNoise = 0 # noise 0 para preferir o caminho mais rapido
    answerLivingReward = 5 #valor alto para preferir o reward 10
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3d():
    #Prefira a saída mais distante (+10), evitando a falésia (-10)
    answerDiscount = 0.3 # aumentar a significatividade das recompensas futuras
    answerNoise = 0.2 # noise para confundir, para ir para o caminho mais longo
    answerLivingReward = 1 # valor alto para preferir o reward maior que 1
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3e():
    #Evite as saídas e o penhasco (para que um episódio nunca termine)
    answerDiscount = 0.3
    answerNoise = 0.2
    answerLivingReward = 10 # reward muito alto para preferir qualquer valor maior que 10
    #mais o tabuleiro não apresenta nenhum reward maior que 10
    #então vai procurar para sempre
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question8():
    answerEpsilon = None
    answerLearningRate = None
    return answerEpsilon, answerLearningRate
    # If not possible, return 'NOT POSSIBLE'

if __name__ == '__main__':
    print('Answers to analysis questions:')
    import analysis
    for q in [q for q in dir(analysis) if q.startswith('question')]:
        response = getattr(analysis, q)()
        print('  Question %s:\t%s' % (q, str(response)))
