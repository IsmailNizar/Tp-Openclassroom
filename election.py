# -*- coding: utf-8 -*-
import random
import os

# Initialize seed so we always get the same result between two runs.
# Comment this out if you want to change results between two runs.
# More on this here: http://stackoverflow.com/questions/22639587/random-seed-what-does-it-do
random.seed(0)

##################################################
#################### VOTES SETUP #################
##################################################
VOTES = 100000
MEDIAN = VOTES/2
CANDIDATES = {
    "hermione": "Hermione Granger",
    "balou": "Balou",
    "chuck-norris": "Chuck Norris",
    "elsa": "Elsa",
    "gandalf": "Gandalf",
    "beyonce": "Beyoncé"
}

MENTIONS = [
    "Excellent",
    "Très bien",
    "Bien",
    "Assez Bien",
    "Passable",
    "Insuffisant",
    "A rejeter"
]
##################################################
#################### FUNCTIONS ###################
##################################################

def create_votes():
    return [
        {
            "hermione": random.randint(3, 6),
            "balou": random.randint(0, 6),
            "chuck-norris": random.randint(0, 2),
            "elsa": random.randint(1, 2),
            "gandalf": random.randint(3, 6),
            "beyonce": random.randint(2, 6)
        } for _ in range(0, VOTES)
    ]

# fonction qui retourne le score mediane et son index
def mediane(name):
    r = 0
    for i in range(7):
        r += candidates[name][i]
        if r > 50000:
            return r,i

#fonction qui collect une vote et la mettre dans une table
def collectV(i,name):
    h = votes[i][name]
    candidates[name][h] +=1

#fonction qui collect tous les votes disponibles
def collectAllVotes():
    for i in range(0,len(votes)):
        for k in candidates.keys():
            collectV(i,k)

#fonction qui trier les candidats selon leurs mention
def sort_candidates_by(mentions):
    unsorted = [(key, (mention["mention"], mention["result"])) for key, mention in mentions.items()]
    swapped = True
    while swapped:
        swapped = False
        for j in range(0, len(unsorted) - 1):
            if unsorted[j + 1][1] < unsorted[j][1]:
                unsorted[j+1], unsorted[j] = unsorted[j], unsorted[j+1]
                swapped = True
    #retourner une liste dedans des dictionaires sous cette fomre dessous ...
    return [
        {
            "name": candidate[0],
            "mention": candidate[1][0],
            "score": candidate[1][1],
        }
        for candidate in unsorted
    ]

def print_result(resultF):
    for k in resultF:
        score = k["score"] * 100 / VOTES
        mention = MENTIONS[k["mention"]]
        if k["mention"] == 0 :
            print("Gagnat : {} a eu un score {} % de mention : {}".format(k["name"],score,mention))
        else:
            print("- {} a eu un score {} % de mention : {}".format(k["name"],score,mention))

if __name__ == '__main__':
    score  = {} 
    scoreG = {}
    #generation des votes
    votes = create_votes()
    #initialisation des candidates
    candidates = {
    'hermione': [0, 0, 0, 0, 0, 0, 0],
    'balou': [0, 0, 0, 0, 0, 0, 0],
    'chuck-norris': [0, 0, 0, 0, 0, 0, 0],
    'elsa': [0, 0, 0, 0, 0, 0, 0],
    'gandalf': [0, 0, 0, 0, 0, 0, 0],
    'beyonce': [0, 0, 0, 0, 0, 0, 0]
    }
    #regroupement des resultats dans un Dict
    collectAllVotes()
    for k in candidates.keys():
        result,mention = mediane(k)
        score = {"mention" : mention , "result" : result}
        scoreG[k] = score
    
    r = sort_candidates_by(scoreG)
    print_result(r)

os.system("pausse")