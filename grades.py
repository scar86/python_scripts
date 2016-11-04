#!/usr/bin/python
grades = [100, 100, 90]

def print_grades(grades):
    for grade in grades:
        print grade

def grades_sum(grades):
    total = 0
    for grade in grades: 
        total += grade
    return total
    
def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))
    return average

#def grades_variance(scores):
    #average = grades_average(scores)
    #variance = 0
    #for score in scores:
        #vari = (average - score) ** 2
        #print (average - score) ** 2
        #variance += vari
    #print ""
    #print variance
    #print average
    #print float(len(grades))
    #print variance / float(len(grades))
    #variance = variance / float(len(grades))
    #return variance #/ float(len(grades))
def grades_variance(scores):
    average = grades_average(scores)
    print average
    variance = 0
    for score in scores:
        variance += ((average - score) ** 2)
    return variance / len(scores)
    
print grades_variance(grades)
