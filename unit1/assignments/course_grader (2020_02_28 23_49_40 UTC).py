# If the average score is greater than or equal to 70 and no single test score is below 50, then return a message 
# of "pass"
# If the average score is lower than 70 or at least one test score is below 50, then return a message of "fail"

def course_grader(test_scores):
    # Your code here
    message = ""
    avg = sum(test_scores) / len(test_scores)

    if avg >= 70:
        for score in test_scores:
            if score < 50:
                message = "fail"
                return message

        message = "pass"
    else:
        message = "fail"
    
    return message

    

def main():
    print(course_grader([100,75,45]))     # "fail"
    print(course_grader([100,70,85]))     # "pass"
    print(course_grader([80,60,60]))      # "fail"
    print(course_grader([80,80,90,30,80]))  # "fail"
    print(course_grader([70,70,70,70,70]))  # "pass"

if __name__ == "__main__":
    main()
