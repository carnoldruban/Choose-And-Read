def display_all_rubrics():
    rubrics_content = """
# Project Rubrics

## Rubric Item 1
*   **Criteria:** The response **must** display five horizontally arranged color swatches, where each swatch's background color visually matches its displayed hex code, and the hex code text itself is displayed on the swatch.
*   **Technical Implementation Hint:** For example, this can be achieved by setting the `style.backgroundColor` of a `div` element based on a hex string and displaying the string within that `div` using its `textContent` or `innerHTML`.
*   **Origin Prompt:** Initial Prompt (Request 1)
*   **Type:** Explicit
*   **Nature:** Objective
*   **Category Label:** Aesthetics
*   **Image Plan:** Text-only or Singleton

## Rubric Item 2
*   **Criteria:** The response **must** ensure that color swatches marked as 'locked' (e.g., displaying a 🔒 icon) cannot be moved from their current position or be displaced when other swatches are dragged and dropped nearby or into their position.
*   **Technical Implementation Hint:** For example, this requires robust checks within drag-and-drop event handlers (like `dragenter`, `dragover`, `drop`). The logic should prevent any re-parenting or reordering actions in the DOM if either the dragged swatch or the target position (or any swatch that would be shifted) is locked.
*   **Origin Prompt:** Follow-up Prompt 2 (Locked swatch immovability)
*   **Type:** Explicit
*   **Nature:** Objective
*   **Category Label:** Functionality
*   **Image Plan:** Singleton (Illustrating the failure: a locked swatch being moved).

## Rubric Item 3
*   **Criteria:** The response **must** include a lock icon (e.g., 🔓/🔒) on each color swatch that visually toggles between distinct 'locked' and 'unlocked' states upon user click, accurately reflecting the swatch's draggable status.
*   **Technical Implementation Hint:** An example implementation involves using a clickable element (such as a `<span>` or `<button>`) that, on click, changes its visual content (e.g., text emoji, icon class) and updates a data attribute on the swatch. The swatch's `draggable` HTML attribute should also be programmatically updated.
*   **Origin Prompt:** Initial Prompt (Request 2)
*   **Type:** Explicit
*   **Nature:** Objective
*   **Category Label:** Interaction
*   **Image Plan:** Text-only or Singleton

## Rubric Item 4
*   **Criteria:** The response **must** dynamically adjust the color of the hex code text (and any other informational text or icons like 'color name' or 'copy icon' within the swatch info area) on each color swatch to ensure high contrast and readability against the swatch's current background color (e.g., using white text on dark colors, and black text on light colors).
*   **Technical Implementation Hint:** For instance, this typically involves a JavaScript function that calculates the perceived brightness of the background color (e.g., from its RGB components using a standard luminance formula) and then programmatically sets the `style.color` of the text elements to a contrasting color (like #FFFFFF or #000000) based on a brightness threshold.
*   **Origin Prompt:** Follow-up Prompt 1 (Dynamic text color)
*   **Type:** Explicit
*   **Nature:** Objective
*   **Category Label:** Aesthetics
*   **Image Plan:** Text-only or Singleton

## Rubric Item 5
*   **Criteria:** The response **must** provide clear and immediate visual feedback, such as a "Copied!" message, appearing proximally and unobscured next to the hex code or copy icon, for a brief duration (e.g., 1-2 seconds) when the hex code is successfully copied to the clipboard.
*   **Technical Implementation Hint:** As an example, this can be done using JavaScript to trigger the `navigator.clipboard.writeText()` method. Upon successful copy, a predefined message element (initially hidden via CSS `opacity: 0` or `display: none`) would be made visible (e.g., by adding a 'show' class that changes opacity or display) and then hidden again after a short delay using `setTimeout`. The message should be positioned using CSS (e.g., absolute positioning relative to the copy icon or hex code container) to ensure it does not overlap awkwardly with other elements.
*   **Origin Prompt:** Follow-up Prompt 3 (Copy to clipboard & feedback)
*   **Type:** Explicit
*   **Nature:** Objective
*   **Category Label:** Interaction
*   **Image Plan:** Singleton (Showing message placement, potentially highlighting if it's awkward).

## Rubric Item 6
*   **Criteria:** The response **should** present a visually balanced and intuitive user interface, with interactive elements like icons (lock, copy, color picker) being easily identifiable, appropriately sized, and spaced for comfortable user interaction.
*   **Technical Implementation Hint:** For example, this can involve applying consistent padding and margins around elements, ensuring clickable targets are adequately sized (e.g., meeting common accessibility guidelines for touch targets, though not explicitly requested), and using a clear visual hierarchy. CSS Flexbox or Grid can be useful for alignment and spacing.
*   **Origin Prompt:** Implicit
*   **Type:** Implicit
*   **Nature:** Subjective
*   **Category Label:** Aesthetics
*   **Image Plan:** Pairwise (Comparing Turn 4 UI to an ideally balanced reference UI for a similar tool).

## Rubric Item 7
*   **Criteria:** The response **should** ensure that the color palette display is reasonably responsive, maintaining usability and visual organization on smaller screen widths (e.g., down to typical mobile viewport widths like 360-480px), preventing elements from becoming overly compressed or unreadable.
*   **Technical Implementation Hint:** This could be achieved, for example, by using CSS techniques such as flexible layouts (e.g., `flex-wrap: wrap` on the container if swatches are meant to wrap, or ensuring `flex: 1` on swatches allows them to shrink but not to an unusable extent), relative units (like percentages, vw), and potentially CSS media queries to adjust layout, font sizes, or element visibility at different breakpoints.
*   **Origin Prompt:** Implicit
*   **Type:** Implicit
*   **Nature:** Objective
*   **Category Label:** Aesthetics
*   **Image Plan:** Pairwise (Turn 4 output on a simulated mobile view vs. an ideal responsive color palette example).

## Rubric Item 8
*   **Criteria:** The response **must** allow users to reorder color swatches within the palette container using a drag-and-drop mouse interaction, where the visual order of swatches updates to reflect the drop action.
*   **Technical Implementation Hint:** For example, this typically involves setting the `draggable="true"` HTML attribute on swatch elements and implementing JavaScript event handlers for `dragstart` (to store data about the dragged item), `dragend`, `dragover` (to `preventDefault()`), and `dragenter` or `drop` (to handle the DOM manipulation for reordering, such as `insertBefore()`).
*   **Origin Prompt:** Initial Prompt (Request 3)
*   **Type:** Explicit
*   **Nature:** Objective
*   **Category Label:** Functionality
*   **Image Plan:** Text-only

## Rubric Item 9
*   **Criteria:** The response **must** provide an interactive option, such as a clickable color input or icon, on each swatch that allows a user to open a system color picker and change the color of that specific swatch; the swatch's background and displayed hex code must update to the newly selected color.
*   **Technical Implementation Hint:** An example of this is to include an `<input type="color">` element for each swatch. An event listener (e.g., on `input` or `change`) for this input would update the swatch's background color and its displayed hex code value. A visually styled `<label>` could be used to make the color input more appealing.
*   **Origin Prompt:** Follow-up Prompt 1 (Option to change color)
*   **Type:** Explicit
*   **Nature:** Objective
*   **Category Label:** Functionality
*   **Image Plan:** Singleton (Showing the color picker interface activated for a swatch).
"""
    print(rubrics_content)

if __name__ == "__main__":
    display_all_rubrics()
