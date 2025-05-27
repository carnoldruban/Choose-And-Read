def get_follow_up_prompt_3_task2():
    prompt = """Add a new feature to the 'Default Text' section in the sidebar. Below the textarea, include a button or link labeled 'Suggest Placeholders'. When clicked, it should populate the 'Default Text' textarea (and consequently the main text input and previews) with a randomly selected placeholder phrase from a predefined list of at least three distinct, short, typography-relevant phrases (e.g., 'The quick brown fox', 'Handgloves', 'Myriad Pro'). Each click should offer a chance at a new random phrase from the list."""
    
    print("Follow-up Prompt 3 (Task 2 - Typography):")
    print("---")
    print(prompt)
    print("---")

if __name__ == "__main__":
    get_follow_up_prompt_3_task2()
