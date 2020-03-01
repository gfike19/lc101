"""
A program to take grade input and calculate a student's GPA
"""



def get_grades():
	grades = []
	continue_entry = True
	
	# gather grade information
	while continue_entry:
	    grade = input("Your grade (0.0-4.0): ")
	    credits = input("# credits: ")
	
	    # store grades
	    grades.append({'grade': float(grade), 'credits': int(credits)})
	
	    user_wants_to_continue = input("Enter another grade? [y/n]: ")
	    if user_wants_to_continue == 'n':
	        continue_entry = False
	return grades


# compute GPA
def compute_GPA(grades):
	#grades = get_grades()
	total_quality_score = 0
	total_credits = 0
	
	# calculate quality scores and total
	for grade_info in grades:
	    total_quality_score += (grade_info['grade'] * grade_info['credits'])
	    total_credits += grade_info['credits']
	
	gpa = total_quality_score / total_credits
	return gpa
	
def main():
	grades = get_grades()
	gpa = compute_GPA(grades)
	print("Your GPA is:", gpa)

if __name__ == '__main__':
    main()