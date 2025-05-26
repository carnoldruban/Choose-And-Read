def get_follow_up_prompt_1():
    prompt = """Thanks for the start. Let's refine this.
First, the hex code text on the color swatches needs to be readable. Please make the hex code text color dynamic: it should be white on dark background colors and black on light background colors.
Second, the lock functionality has a bug: when a color is locked (shows 🔒), it should *not* be draggable. Currently, it's the opposite. Please fix this.
Finally, please remove the 'color-name' (e.g., 'Giants orange') displayed below the hex code, as this was not requested."""
    
    print("Follow-up Prompt 1:")
    print("---")
    print(prompt)
    print("---")

if __name__ == "__main__":
    get_follow_up_prompt_1()
