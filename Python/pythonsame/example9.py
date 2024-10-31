# Example 9:
scores ={'Alice':44,'Bob':30,'Charlie':40,'David':85}
filtered_scorec={name: score for name, score in scores.items()if score>=70}
print("Filtered Scores : ",filtered_scorec)