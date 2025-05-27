def get_initial_prompt_task2():
    prompt = """Create a webpage for typography and font visualization using HTML/CSS/JS, based on the attached image. The page should include:
1.  A prominent text input field where a user can type their own sample text.
2.  A font selection feature that allows the user to choose from at least three different web-safe fonts (e.g., 'Arial', 'Georgia', 'Courier New'), and the sample text should immediately render in the chosen font.
3.  A font size controller, such as a slider or number input, that allows the user to dynamically adjust the font size of the sample text."""
    image_url = "https://i.postimg.cc/CK9M3bfS/prompt-image.jpg"
    
    print("Initial Prompt (Task 2 - Typography):")
    print("---")
    print(prompt)
    print("---")
    print(f"Reference Image URL: {image_url}")

if __name__ == "__main__":
    get_initial_prompt_task2()
