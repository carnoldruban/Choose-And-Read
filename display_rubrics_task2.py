def display_rubrics_task2():
    rubrics_content = """
# Project Rubrics - Task 2: Typography and Font Visualization

## Rubric Item 1
*   **Criteria:** The response **must** provide a prominent text input field where users can type their own sample text, and this text must be used to update the font preview areas.
*   **Technical Implementation Hint:** For example, using an `<input type="text">` or `<textarea>` and JavaScript event listeners (`oninput`) to update the `textContent` of preview `div` elements.
*   **Origin Prompt:** Initial Prompt (Task 2) - Request 1
*   **Type:** Explicit
*   **Nature:** Objective
*   **Category Label:** Functionality
*   **Image Plan:** Text-only or Singleton

## Rubric Item 2
*   **Criteria:** The response **must** include a font selection mechanism (e.g., dropdowns) offering at least three distinct web-safe fonts, allowing the user to apply a selected font to the sample text in the preview areas.
*   **Technical Implementation Hint:** For example, using `<select>` elements with `<option>` tags for font names, and JavaScript event listeners (`onchange`) to update the `style.fontFamily` of preview elements.
*   **Origin Prompt:** Initial Prompt (Task 2) - Request 2
*   **Type:** Explicit
*   **Nature:** Objective
*   **Category Label:** Functionality
*   **Image Plan:** Text-only or Singleton

## Rubric Item 3
*   **Criteria:** The response **must** provide a font size controller (e.g., a slider or number input) that allows the user to dynamically adjust the font size of the sample text in the preview areas.
*   **Technical Implementation Hint:** For example, using an `<input type="range">` or `<input type="number">` and JavaScript event listeners (`oninput`) to update the `style.fontSize` of preview elements.
*   **Origin Prompt:** Initial Prompt (Task 2) - Request 3
*   **Type:** Explicit
*   **Nature:** Objective
*   **Category Label:** Interaction
*   **Image Plan:** Text-only or Singleton

## Rubric Item 4
*   **Criteria:** The response **must** make the 'Theme' selector functional, applying a visually distinct dark theme (e.g., dark backgrounds, light text for main page elements and text) when 'Dark' is selected and reverting to a light theme for 'Light'.
*   **Technical Implementation Hint:** For example, by adding/removing a 'dark-theme' class on the `<body>` or main container elements, with corresponding CSS rules for `.dark-theme` descendant selectors affecting backgrounds and text colors.
*   **Origin Prompt:** Follow-up Prompt 1 (Task 2) - Request 1
*   **Type:** Explicit
*   **Nature:** Objective
*   **Category Label:** Aesthetics
*   **Image Plan:** Singleton (showing dark mode applied)

## Rubric Item 5
*   **Criteria:** The response **must** ensure the 'Display Text Size' toggle switch in the sidebar controls the visibility or enabled state of its associated font size slider and number input (e.g., hiding them when the toggle is off).
*   **Technical Implementation Hint:** For example, using a checkbox event listener to add/remove a class (e.g., 'hidden' or 'disabled') to the container of the font size controls, with CSS to achieve `display: none` or visual disablement.
*   **Origin Prompt:** Follow-up Prompt 1 (Task 2) - Request 2
*   **Type:** Explicit
*   **Nature:** Objective
*   **Category Label:** Interaction
*   **Image Plan:** Text-only

## Rubric Item 6
*   **Criteria:** The response **must** activate the 'Layout' selector so that selecting 'Modern', 'Classic', or 'Minimal' applies a distinct visual style (e.g., changes to border, background, or padding) to the main font preview area(s).
*   **Technical Implementation Hint:** For example, by adding/removing layout-specific classes (e.g., `layout-modern`) to the preview container using JavaScript and defining CSS rules for these classes that alter properties like `border`, `background-color`, or `padding`.
*   **Origin Prompt:** Follow-up Prompt 2 (Task 2)
*   **Type:** Explicit
*   **Nature:** Objective
*   **Category Label:** Aesthetics
*   **Image Plan:** Singleton (showing one of the layout styles applied)

## Rubric Item 7
*   **Criteria:** The response **must** include a 'Suggest Placeholders' button/link that, when clicked, populates the 'Default Text' textarea (and consequently synced previews/inputs) with a randomly selected phrase from a predefined list of at least three distinct, short, typography-relevant phrases.
*   **Technical Implementation Hint:** For example, using a JavaScript array of strings, a button element with an `onclick` event listener, and `Math.random()` to select an array element, then updating the textarea's `.value` and other relevant elements.
*   **Origin Prompt:** Follow-up Prompt 3 (Task 2)
*   **Type:** Explicit
*   **Nature:** Objective
*   **Category Label:** Functionality
*   **Image Plan:** Text-only

## Rubric Item 8
*   **Criteria:** The response **must** ensure that all interactive UI controls presented, such as the 'Display Text Case' toggle switch visible in the sidebar, are functional and produce a corresponding change in the UI or font previews when interacted with.
*   **Technical Implementation Hint:** For example, if a toggle for 'uppercase' (identified as 'Display Text Case' toggle in UI) is present, it should have an event listener that, when activated, changes the `style.textTransform` of relevant preview text elements to `uppercase` or `none`.
*   **Origin Prompt:** Implicit (based on UI element presented by model in earlier turns but not explicitly requested to be functional by user, yet expected to work if visible) - OR consider it related to Initial Prompt if UI implies all controls work. Let's class it as Explicit for now due to visibility.
*   **Type:** Explicit 
*   **Nature:** Objective
*   **Category Label:** Functionality
*   **Image Plan:** Singleton (showing the non-functional toggle)

## Rubric Item 9
*   **Criteria:** The response **should** demonstrate a high level of UI cohesion and polish, with consistent styling, spacing, and alignment across all sections (header, sidebar, content area), and all interactive elements should be well-integrated and visually refined, avoiding awkward juxtapositions or misalignments.
*   **Technical Implementation Hint:** For example, using a consistent design language (e.g., similar border styles, button styles, spacing units like `rem` or `em`), ensuring good visual hierarchy, and testing for visual regressions when adding new features.
*   **Origin Prompt:** Implicit
*   **Type:** Implicit
*   **Nature:** Subjective
*   **Category Label:** Aesthetics
*   **Image Plan:** Pairwise (comparing overall UI to a polished reference, or highlighting specific minor inconsistencies).

## Rubric Item 10
*   **Criteria:** The response **should** ensure the typography visualization tool is reasonably responsive, maintaining usability and preventing layout issues (e.g., overlapping elements, unreadable text due to compression, horizontal scrolling) on smaller screen widths (e.g., typical mobile viewports).
*   **Technical Implementation Hint:** For example, using CSS media queries to adjust sidebar width, font sizes of controls/previews, stacking elements differently, or hiding less critical elements on smaller viewports to preserve usability.
*   **Origin Prompt:** Implicit
*   **Type:** Implicit
*   **Nature:** Objective
*   **Category Label:** Aesthetics
*   **Image Plan:** Pairwise (showing Turn 4 output on a simulated mobile view vs. an ideal responsive typography tool).
"""
    print(rubrics_content)

if __name__ == "__main__":
    display_rubrics_task2()
