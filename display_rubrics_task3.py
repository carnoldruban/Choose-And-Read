def display_rubrics_task3():
    rubrics_content = """
# Project Rubrics - Task 3: Code Diff Checker

## Rubric Item 1
*   **Criteria:** The response **must** include two main text areas side-by-side, one clearly designated for 'original' code/text and one for 'changed' code/text.
*   **Technical Implementation Hint:** For example, using two `<textarea>` elements within a parent `div` styled with `display: flex`.
*   **Origin Prompt:** Initial (Task 3)
*   **Type:** Explicit
*   **Nature:** Objective
*   **Category Label:** Functionality
*   **Image Plan:** Singleton (showing the two text areas)

## Rubric Item 2
*   **Criteria:** The response **must** ensure that both input text areas (for 'original' and 'changed' code/text) display line numbers alongside the text as the user types or pastes content.
*   **Technical Implementation Hint:** For example, this typically requires a more complex setup than a plain `<textarea>`, potentially using a library or a custom component that includes a separate `div` for line numbers synced via JavaScript to the textarea's scroll events and line breaks.
*   **Origin Prompt:** Initial (Task 3)
*   **Type:** Explicit
*   **Nature:** Objective
*   **Category Label:** UI/UX Improvement
*   **Image Plan:** Singleton (showing an input textarea lacking line numbers)

## Rubric Item 3
*   **Criteria:** The response **must** include a 'Compare' button that, upon user action, triggers a comparison and visually highlights lines that are different (e.g., added, removed, or modified) in a distinct output area, for instance, by using different background colors for these statuses.
*   **Technical Implementation Hint:** For example, by implementing a JavaScript function attached to a button's `onClick` event. This function would split input strings into arrays of lines, compare them to assign a status (added, removed, modified, unchanged), and then render these lines with conditional CSS classes for background highlighting within new `div` elements.
*   **Origin Prompt:** Initial (Task 3)
*   **Type:** Explicit
*   **Nature:** Objective
*   **Category Label:** Functionality
*   **Image Plan:** Singleton (showing the diff output with highlighted lines)

## Rubric Item 4
*   **Criteria:** The response **must** add a 'Clear' button for each input text area ('Original' and 'Changed'), which, when clicked, empties the content of the respective text area and also clears any displayed diff comparison results from view.
*   **Technical Implementation Hint:** For example, using `<button>` elements with JavaScript `onClick` event listeners that update the state variables holding the textarea content to empty strings and also reset the state variable for diff results to an empty array or null.
*   **Origin Prompt:** Follow-up 1 (Task 3)
*   **Type:** Explicit
*   **Nature:** Objective
*   **Category Label:** UI/UX Improvement
*   **Image Plan:** Text-only

## Rubric Item 5
*   **Criteria:** The response **must** include a 'Swap' button that, when clicked, effectively swaps the content between the 'Original Code/Text' and 'Changed Code/Text' text areas, and also clears any currently displayed diff results.
*   **Technical Implementation Hint:** For example, using a `<button>` with a JavaScript `onClick` event listener. The handler would use a temporary variable to store the content of one textarea state, set the first textarea's state to the second's, set the second to the temporary variable's content, and then reset the diff result state.
*   **Origin Prompt:** Follow-up 2 (Task 3)
*   **Type:** Explicit
*   **Nature:** Objective
*   **Category Label:** Functionality
*   **Image Plan:** Text-only

## Rubric Item 6
*   **Criteria:** The response **must** display a summary line of text (e.g., 'Comparison: Original (X lines) vs. Changed (Y lines)') above or near the diff results, which is visible only when diff results are present and accurately states the total line counts for the compared inputs.
*   **Technical Implementation Hint:** For example, by calculating the line counts from the input strings (e.g., `originalCode.split('\n').length`) and conditionally rendering a `div` containing this formatted text when the diff result state is populated.
*   **Origin Prompt:** Follow-up 3 (Task 3)
*   **Type:** Explicit
*   **Nature:** Objective
*   **Category Label:** UI/UX Improvement
*   **Image Plan:** Singleton (showing the summary line above diff results)

## Rubric Item 7
*   **Criteria:** The diff output display **should** accurately represent basic differences for simple cases, such as identifying lines that are purely added, purely removed, wholly modified, or unchanged, without obvious logical errors in status assignment.
*   **Technical Implementation Hint:** For example, a line present in the 'changed' text but not at a corresponding position in the 'original' should be marked 'added'. A line in 'original' but not 'changed' should be 'removed'. Lines at the same number but with different content are 'modified'. The model's basic algorithm (iterating to max length and comparing line by line) is an attempt at this.
*   **Origin Prompt:** Implicit (derived from the core purpose of a diff tool)
*   **Type:** Implicit
*   **Nature:** Objective
*   **Category Label:** Functionality
*   **Image Plan:** Pairwise (showing a simple input pair and the model's potentially slightly confusing diff output, vs. an ideal simple diff representation for that same pair, if needed to illustrate a subtle flaw).

## Rubric Item 8
*   **Criteria:** Interactive controls like 'Compare', 'Clear', and 'Swap' buttons **should** have appropriate disabled states based on the application state to prevent user error (e.g., 'Compare' should be disabled if one or both input fields are empty).
*   **Technical Implementation Hint:** For example, by binding the `disabled` HTML attribute of `<button>` elements to boolean conditions derived from the state of text area content variables (e.g., `disabled={!originalCode || !changedCode}`).
*   **Origin Prompt:** Implicit (general usability expectation)
*   **Type:** Implicit
*   **Nature:** Objective
*   **Category Label:** UI/UX Improvement
*   **Image Plan:** Text-only or Singleton (showing a disabled button state)

## Rubric Item 9
*   **Criteria:** The overall user interface **should** be clean, visually consistent, and the styling (e.g., Tailwind CSS usage) should be applied coherently across components like the header, input areas, buttons, and diff results, reflecting the style of a typical productivity/developer tool.
*   **Technical Implementation Hint:** For example, ensuring consistent use of font families, spacing, color schemes (beyond diff highlighting), border styles, and responsive behavior to provide a professional look and feel.
*   **Origin Prompt:** Implicit
*   **Type:** Implicit
*   **Nature:** Subjective
*   **Category Label:** Aesthetics
*   **Image Plan:** Pairwise (comparing overall UI to the reference `w3docs.com/tools/code-diff/` or another polished diff tool, focusing on overall layout and style consistency).

## Rubric Item 10
*   **Criteria:** The diff checker interface, including text areas and diff results, **should** be reasonably responsive, ensuring that on smaller screens the layout remains usable (e.g., side-by-side views adapt or stack appropriately) and text remains readable without excessive horizontal scrolling.
*   **Technical Implementation Hint:** For example, using flexible CSS layouts (like Flexbox with wrapping enabled for containers holding the text areas and diff views), percentage-based widths, and potentially media queries to adjust font sizes or switch to a stacked layout for text areas/diff views on narrow viewports.
*   **Origin Prompt:** Implicit
*   **Type:** Implicit
*   **Nature:** Objective
*   **Category Label:** Aesthetics
*   **Image Plan:** Pairwise (showing the Turn 4 output on a simulated mobile view vs. an ideal responsive diff tool layout).
"""
    print(rubrics_content)

if __name__ == "__main__":
    display_rubrics_task3()
