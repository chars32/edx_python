#Write a function named construct_dictionary_from_lists that accepts 3 one dimensional lists and 
#constructs and returns a dictionary as specified below. 
#		The first one dimensional list will have n strings which will be the names of some people.
#		The second one dimensional list will have n integers which will be the ages that correspond to those people.
#		The third one dimensional list will have n integers which will be the scores that correspond to those people.
#Note that if a person has a score of 60 or higher (score >= 60) that means the person passed, if not the person failed.
#Your function should return a dictionary where each key is the name of a person and the value corresponding 
#to that key should be a list containing age, score, 'pass' or 'fail' in the same order as shown in the sample output.

names = ["paul", "saul", "steve", "chimpy"]
ages = [28, 59, 22, 5]
scores = [59, 85, 55, 60]

def construct_dictionary_from_lists(names_list, ages_list, scores_list):
	dictionary = {}
	grades = []

	#make a new list called grades where we evaluate if pass or fail
	for score in scores_list:
		if score >= 60:
			grades.append("pass")
		else:
			grades.append("fail")
			
	#correct keys and values en dictionary
	for x in range(len(names_list)):
		dictionary[names_list[x]]= [ages_list[x], scores_list[x], grades[x]]

	return dictionary

print(construct_dictionary_from_lists(names, ages, scores))

#solution {'steve': [22, 55, 'fail'], 'saul': [59, 85, 'pass'], 'paul': [28, 59, 'fail'], 'chimpy': [5, 60, 'pass']}