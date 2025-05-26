def display_evaluations():
    rubric_evaluations = [
        {
            "rubric_item": "Rubric Item 1: Display five horizontally arranged color swatches...",
            "original_model_eval": "No Issues",
            "original_model_justification": "N/A",
            "alternate_model_eval": "No Issues",
            "alternate_model_justification": "N/A",
        },
        {
            "rubric_item": "Rubric Item 2: Ensure locked swatches are immovable...",
            "original_model_eval": "Major Issues",
            "original_model_justification": "Locked swatches can still be displaced when other unlocked swatches are dragged near them. This fails the requirement that they 'cannot be moved from their current position or be displaced.'",
            "alternate_model_eval": "Major Issues",
            "alternate_model_justification": "Locked swatches can still be displaced when other unlocked swatches are dragged near them. This fails the requirement that they 'cannot be moved from their current position or be displaced.' (Code is identical to Original Model)",
        },
        {
            "rubric_item": "Rubric Item 3: Include a lock icon that visually toggles...",
            "original_model_eval": "No Issues",
            "original_model_justification": "N/A",
            "alternate_model_eval": "No Issues",
            "alternate_model_justification": "N/A",
        },
        {
            "rubric_item": "Rubric Item 4: Dynamically adjust hex code text color for readability...",
            "original_model_eval": "No Issues",
            "original_model_justification": "N/A",
            "alternate_model_eval": "No Issues",
            "alternate_model_justification": "N/A",
        },
        {
            "rubric_item": "Rubric Item 5: Provide clear visual feedback for copy to clipboard...",
            "original_model_eval": "Minor Issues",
            "original_model_justification": "The 'Copied!' message is positioned `top: -30px;` relative to the `hex-code-container`, which might be too high or visually disconnected from the copy icon itself, potentially being obscured.",
            "alternate_model_eval": "Minor Issues",
            "alternate_model_justification": "The 'Copied!' message is positioned `top: -30px;` relative to the `hex-code-container`, which might be too high or visually disconnected from the copy icon itself, potentially being obscured. (Code is identical to Original Model)",
        },
        {
            "rubric_item": "Rubric Item 6: Present a visually balanced and intuitive UI (Implicit/Subjective)...",
            "original_model_eval": "No Issues",
            "original_model_justification": "N/A",
            "alternate_model_eval": "No Issues",
            "alternate_model_justification": "N/A",
        },
        {
            "rubric_item": "Rubric Item 7: Ensure reasonable responsiveness (Implicit)...",
            "original_model_eval": "Minor Issues",
            "original_model_justification": "Swatches use `flex: 1` and could become very narrow on small screens, potentially cramping content, as no specific responsive adjustments are made for smaller viewports.",
            "alternate_model_eval": "Minor Issues",
            "alternate_model_justification": "Swatches use `flex: 1` and could become very narrow on small screens, potentially cramping content, as no specific responsive adjustments are made for smaller viewports. (Code is identical to Original Model)",
        },
        {
            "rubric_item": "Rubric Item 8: Allow reordering of swatches via drag-and-drop...",
            "original_model_eval": "No Issues",
            "original_model_justification": "N/A",
            "alternate_model_eval": "No Issues",
            "alternate_model_justification": "N/A",
        },
        {
            "rubric_item": "Rubric Item 9: Provide an interactive option to change swatch color...",
            "original_model_eval": "No Issues",
            "original_model_justification": "N/A",
            "alternate_model_eval": "No Issues",
            "alternate_model_justification": "N/A",
        }
    ]

    print("--- Evaluation of Model Outputs ---")
    for i, item_eval in enumerate(rubric_evaluations):
        print(f"\n{item_eval['rubric_item']}")
        print(f"  Original Model (Turn 4 / 'modal output 4'):")
        print(f"    Evaluation: {item_eval['original_model_eval']}")
        print(f"    Justification: {item_eval['original_model_justification']}")
        print(f"  Alternate Model ('New Modal output'):")
        print(f"    Evaluation: {item_eval['alternate_model_eval']}")
        print(f"    Justification: {item_eval['alternate_model_justification']}")
        print("-" * 40)

if __name__ == "__main__":
    display_evaluations()
