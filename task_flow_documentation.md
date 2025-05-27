# Task Flow & Prompt Documentation

This document outlines the sequence of tasks performed, the Python scripts used to display prompts and rubrics, and the content of those prompts/rubrics.

## 1. Initial Prompt Generation and Display

*   **Objective:** Define the initial requirements for the color palette webpage.
*   **Script Used:** `display_initial_prompt.py`
*   **Content Displayed by Script:**
    ```
    Initial Prompt:
    ---
    Build a webpage for color palette exploration using HTML/CSS/JS, as shown in the attached image. It needs to display a series of five horizontal color swatches. Each swatch must show its hex color code text directly on it and have its background set to that color. Implement a feature where each color swatch includes a lock icon that can be toggled to a locked/unlocked visual state. Also, enable users to drag and drop the color swatches to change their order in the palette.
    ---
    Reference Image URL: https://i.postimg.cc/mrpJHKqL/prompt-image.jpg
    ```

## 2. Follow-up Prompt 1 Generation and Display

*   **Objective:** Provide refinements and bug fixes for the initial implementation.
*   **Script Used:** `display_follow_up_prompt_1.py`
*   **Content Displayed by Script:**
    ```
    Follow-up Prompt 1:
    ---
    Thanks for the start. Let's refine this.
    First, the hex code text on the color swatches needs to be readable. Please make the hex code text color dynamic: it should be white on dark background colors and black on light background colors.
    Second, the lock functionality has a bug: when a color is locked (shows 🔒), it should *not* be draggable. Currently, it's the opposite. Please fix this.
    Finally, please remove the 'color-name' (e.g., 'Giants orange') displayed below the hex code, as this was not requested.
    ---
    ```
    *(Self-correction: The original subtask asked to append this to `display_prompt.py`. It was later decided to create separate files for each prompt for clarity and then delete the composite `display_prompt.py` file.)*

## 3. (Notional) Follow-up Prompt 2 (Implicit - No separate script created for display)

*   **Objective:** Introduce requirements for swatch immovability when locked and copy-to-clipboard functionality.
*   **Content:** (This prompt was part of the broader context leading to the rubrics but not explicitly put into its own display script in this sequence of subtasks.)
    *   "Ensure that color swatches marked as 'locked' (e.g., displaying a 🔒 icon) cannot be moved from their current position or be displaced when other swatches are dragged and dropped nearby or into their position."
    *   "Add a 'copy to clipboard' icon/button for each hex code. On click, it should copy the hex code. Provide visual feedback (e.g., 'Copied!') briefly."

## 4. (Notional) Follow-up Prompt 3 (Implicit - No separate script created for display)

*   **Objective:** Introduce requirement for a color picker to change swatch colors.
*   **Content:** (This prompt was also part of the broader context leading to the rubrics.)
    *   "Add an option for the user to change the color of a swatch (e.g., by clicking the swatch or a color picker icon next to it, opening the system color picker)."

## 5. Comprehensive Rubric Definition and Display

*   **Objective:** Define detailed grading criteria covering all explicit and implicit requirements from the prompts.
*   **Script Used:** `display_all_rubrics.py`
*   **Content Displayed by Script:** (This script prints a long string containing 9 detailed rubric items. Refer to the script's content or its execution output for the full text. Key aspects covered include: initial swatch display, lock immovability, lock toggle, dynamic text color, copy feedback, UI balance, responsiveness, drag-and-drop reordering, and color picker functionality.)

## 6. Evaluation Display

*   **Objective:** Show side-by-side evaluations of two model outputs against the defined rubrics.
*   **Script Used:** `display_evaluations.py`
*   **Content Displayed by Script:** (This script prints a list of dictionaries, where each dictionary represents an evaluation for one rubric item for an "Original Model" and an "Alternate Model". It details any issues found and justifications. Refer to the script or its output for full details.)

## File Management Tasks

*   **Creation of `display_prompt.py` (Initial Step):** Created to hold the initial prompt.
*   **Modification of `display_prompt.py`:** The first follow-up prompt was initially appended to this file.
*   **Decision to Refactor:** To improve clarity, `display_prompt.py` was later replaced by individual files for each specific prompt (`display_initial_prompt.py`, `display_follow_up_prompt_1.py`).
*   **Deletion of `display_prompt.py`:** This file was deleted after its content was split into more granular files.
*   **Creation of `rubrics.md`:** A separate Markdown file to store a more general project rubric (distinct from the detailed script-displayed rubrics).
*   **Creation of `task_flow_documentation.md` (This file):** To document the overall process.

This flow ensures that all prompts, rubrics, and evaluations are clearly defined, versioned (implicitly through file creation stages), and displayable for review.
