def get_initial_prompt_task2_revised(): # Renamed function for clarity
    prompt = """Create a webpage for typography and font visualization using HTML/CSS/JS, based on the attached image. I need it to feature a prominent text input field where users can type their own sample text. It should also include a font selection mechanism, for example, a dropdown or clickable previews, allowing users to choose from at least three different web-safe fonts like Arial, Georgia, or Courier New, ensuring the sample text immediately updates to the selected font. Additionally, please implement a font size controller, such as a slider or a number input, so users can dynamically adjust the font size of their sample text."""
    image_url = "https://i.postimg.cc/CK9M3bfS/prompt-image.jpg" # Correct image for Task 2
    
    print("Initial Prompt (Task 2 - Typography - Revised):")
    print("---")
    print(prompt)
    print("---")
    print(f"Reference Image URL: {image_url}")

if __name__ == "__main__":
    get_initial_prompt_task2_revised()
