def course_grader(test_scores):
    total_score = 0
    
    for score in test_scores:
        if score < 50:
            return "fail"
        else:
            total_score += score
    
    average_score = total_score / len(test_scores)
    
    if average_score < 70:
        return "fail"
    else:
        return "pass"