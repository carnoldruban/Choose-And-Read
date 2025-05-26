def get_initial_prompt():
    prompt = """Build a webpage for color palette exploration using HTML/CSS/JS, as shown in the attached image. It needs to display a series of five horizontal color swatches. Each swatch must show its hex color code text directly on it and have its background set to that color. Implement a feature where each color swatch includes a lock icon that can be toggled to a locked/unlocked visual state. Also, enable users to drag and drop the color swatches to change their order in the palette."""
    image_url = "https://i.postimg.cc/mrpJHKqL/prompt-image.jpg"
    
    print("Initial Prompt:")
    print("---")
    print(prompt)
    print("---")
    print(f"Reference Image URL: {image_url}")

if __name__ == "__main__":
    get_initial_prompt()
