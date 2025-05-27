def get_initial_prompt_task3_w3docs_diff():
    prompt = """Please develop a code difference checker tool using Next.js and Typescript, taking design and functional inspiration from the tool at `https://www.w3docs.com/tools/code-diff/`. The initial version should feature two large text areas placed side-by-side, one clearly designated for 'Original Text/Code' and the other for 'Changed Text/Code'. Ensure that both of these input areas display line numbers. Also, include a prominent 'Compare' button that, when clicked, will (for now) generate a placeholder output below the text areas, indicating where the comparison results showing additions, deletions, and modifications would appear."""
    # The image_url was previously https://i.postimg.cc/5tQ5BBwz/prompt-image.jpg 
    # but the user has now provided a URL to use as a functional reference.
    # For this prompt, the functional reference is more important than a static image.
    functional_reference_url = "https://www.w3docs.com/tools/code-diff/"
    
    print("Initial Prompt (Task 3 - Code Diff Checker - w3docs reference):")
    print("---")
    print(prompt)
    print("---")
    print(f"Functional Reference URL: {functional_reference_url}")

if __name__ == "__main__":
    get_initial_prompt_task3_w3docs_diff()
