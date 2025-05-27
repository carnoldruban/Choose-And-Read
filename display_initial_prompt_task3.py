def get_initial_prompt_task3():
    prompt = """Develop a basic lesson navigation page for an online course platform using Next.js and Typescript, referencing the style of the attached image. The page should feature a responsive sidebar that lists course sections and individual lessons within those sections; for example, 'Section 1: Introduction' with 'Lesson 1.1: Overview' and 'Lesson 1.2: Key Concepts' listed beneath it. The main content area should initially display a placeholder welcoming users or prompting them to select a lesson. Ensure that clicking a lesson name in the sidebar updates the main content area to show placeholder text indicating the selected lesson's title and some sample content, for instance, 'Displaying content for Lesson 1.1: Overview'."""
    image_url = "https://i.postimg.cc/L89GVcPK/prompt-image.jpg"
    
    print("Initial Prompt (Task 3 - Online Course Platform):")
    print("---")
    print(prompt)
    print("---")
    print(f"Reference Image URL: {image_url}")

if __name__ == "__main__":
    get_initial_prompt_task3()
