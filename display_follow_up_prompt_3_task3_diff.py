def get_follow_up_prompt_3_task3_diff():
    prompt = """After a comparison is made and the diff results are displayed, please add a summary line of text above the diff results. This summary should state the total number of lines in the 'Original Code' and the total number of lines in the 'Changed Code', for example: 'Comparison: Original (X lines) vs. Changed (Y lines)'. This summary should only be visible when diff results are present."""
    
    print("Follow-up Prompt 3 (Task 3 - Code Diff Checker):")
    print("---")
    print(prompt)
    print("---")

if __name__ == "__main__":
    get_follow_up_prompt_3_task3_diff()
