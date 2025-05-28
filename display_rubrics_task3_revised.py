def display_rubrics_task3_revised():
    rubrics_content = """
# Project Rubrics - Task 3: Code Diff Checker (Revised)

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

## Rubric Item 7 (Revised)
*   **Criteria:** The diff output display **should** logically assign statuses (e.g., 'added', 'removed', 'modified', 'unchanged') to lines for simple comparison scenarios, such that the visual representation clearly corresponds to the basic differences between the two input texts.
*   **Technical Implementation Hint:** For example, if a line of text exists in the 'changed' input at a certain position but no corresponding line existed in the 'original' input (e.g., new lines added at the end), it should be marked 'added'. Conversely, if a line from 'original' is absent in 'changed', it should be 'removed'. Lines that are identical in both inputs at the same position should be 'unchanged'. Lines present in both but with different content should be 'modified'.
*   **Origin Prompt:** Implicit (derived from the core purpose of a diff tool)
*   **Type:** Implicit
*   **Nature:** Objective
*   **Category Label:** Functionality
*   **Image Plan:** Pairwise (showing a simple input pair and the model's diff output, comparing against an ideally clear representation if the model's is confusing for that simple case).

## Rubric Item 8 (Revised)
*   **Criteria:** Interactive controls like 'Compare', 'Clear', and 'Swap' buttons **should** visually indicate when they are not active or usable (e.g., appear greyed out or have reduced opacity) if pre-conditions for their operation are not met (such as input fields being empty for 'Compare' or 'Clear').
*   **Technical Implementation Hint:** For example, by conditionally applying CSS classes or the `disabled` HTML attribute to button elements based on the state of relevant data (e.g., `originalCode === '' || changedCode === ''` for the Compare button).
*   **Origin Prompt:** Implicit (general usability expectation)
*   **Type:** Implicit
*   **Nature:** Objective
*   **Category Label:** UI/UX Improvement
*   **Image Plan:** Singleton (showing a button in its correctly disabled state).

## Rubric Item 9 (Revised)
*   **Criteria:** The user interface **should** exhibit a professional and consistent aesthetic, with harmonious styling applied across all components including the header, input areas, buttons, and diff results, aligning with the visual standards of contemporary productivity tools.
*   **Technical Implementation Hint:** For example, by consistent use of a limited color palette (beyond functional highlighting for diffs), uniform typography, predictable spacing and alignment (e.g., using a grid or flexbox consistently), and ensuring interactive elements have a clear and consistent style for states like hover or focus.
*   **Origin Prompt:** Implicit
*   **Type:** Implicit
*   **Nature:** Subjective
*   **Category Label:** Aesthetics
*   **Image Plan:** Pairwise (comparing overall UI to the reference `w3docs.com/tools/code-diff/` or another polished diff tool for visual consistency and professionalism).

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
    display_rubrics_task3_revised()
