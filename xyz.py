import matplotlib.pyplot as plt

def get_student_scores(student_name):
    print(f"\nEnter scores for {student_name}:")
    assessments = []
    scores = []
    
    num = int(input("How many assessments? "))
    
    for i in range(num):
        a = input(f"Assessment {i+1} name: ")
        s = float(input(f"Score in {a}: "))
        assessments. append(a)
        scores. append(s)
    return assessments, scores

def plot_comparison(assessments, s1_scores, s2_scores, student1, student2):
    plt.figure(figsize=(10,5))
    plt.plot(assessments, s1_scores, marker='o', label=student1)
    plt.plot(assessments, s2_scores, marker='o', label=student2)
    
    plt.title("Performance Trend Comparison")
    plt.xlabel("Assessments")
    plt.ylabel("Scores")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    
    plt.show()

def main():
    print("=== Student Performance Comparison Tool ===")
    
    student1 = input("Enter Student 1 name: ")
    student2 = input("Enter Student 2 name: ")
    
    assessments1, scores1 = get_student_scores(student1)
    assessments2, scores2 = get_student_scores(student2)
    
    
    if assessments1 != assessments2:
        print("\nError: Assessments must be identical for comparison!")
        return
    
    plot_comparison(assessments1, scores1, scores2, student1, student2)

if __name__ == "__main__":
    main()
