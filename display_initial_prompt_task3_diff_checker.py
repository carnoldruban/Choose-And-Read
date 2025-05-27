def get_initial_prompt_task3_diff_checker():
    prompt = """Please start developing a code difference checker tool using Next.js and Typescript, with the user interface styled similarly to the reference image provided. The initial version should include two main text areas side-by-side, one for pasting the 'original' code and the other for the 'changed' code. Ensure that both text areas display line numbers next to the code. Upon a user action, such as clicking a 'Compare' button, the tool should then visually highlight lines that are different between the two text areas, for instance, by using distinct background colors for added, removed, or modified lines (you can simulate this highlighting for now, focusing on the UI structure for these highlighted states)."""
    image_url = "https://i.postimg.cc/5tQ5BBwz/prompt-image.jpg"
    
    print("Initial Prompt (Task 3 - Code Diff Checker):")
    print("---")
    print(prompt)
    print("---")
    print(f"Reference Image URL: {image_url}")

if __name__ == "__main__":
    get_initial_prompt_task3_diff_checker()
