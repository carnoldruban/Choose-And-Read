def get_initial_prompt_task3_kanban():
    prompt = """Using Next.js and Typescript, please create the basic structure for a Kanban-style task management board, taking visual cues from the provided reference image. The board should display three distinct columns, for example labeled 'To Do', 'In Progress', and 'Done'. Within each of these columns, implement functionality to render individual task cards; each card should initially just show a placeholder title, for instance, 'Task Item 1'. Finally, enable basic drag-and-drop functionality that allows users to move these task cards from one column to another."""
    image_url = "https://i.postimg.cc/5tQ5BBwz/prompt-image.jpg"
    
    print("Initial Prompt (Task 3 - Kanban Board Tool):")
    print("---")
    print(prompt)
    print("---")
    print(f"Reference Image URL: {image_url}")

if __name__ == "__main__":
    get_initial_prompt_task3_kanban()
