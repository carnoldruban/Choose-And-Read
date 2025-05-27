def display_evaluations_task2():
    rubric_evaluations = [
        {
            "rubric_item": "Rubric 1 (Task 2): Provide prominent text input field...",
            "original_model_eval": "No Issues",
            "original_model_justification": "N/A",
            "alternate_model_eval": "No Issues",
            "alternate_model_justification": "N/A (Code identical to Original)",
        },
        {
            "rubric_item": "Rubric 2 (Task 2): Include font selection mechanism...",
            "original_model_eval": "No Issues",
            "original_model_justification": "N/A",
            "alternate_model_eval": "No Issues",
            "alternate_model_justification": "N/A (Code identical to Original)",
        },
        {
            "rubric_item": "Rubric 3 (Task 2): Provide font size controller...",
            "original_model_eval": "No Issues",
            "original_model_justification": "N/A",
            "alternate_model_eval": "No Issues",
            "alternate_model_justification": "N/A (Code identical to Original)",
        },
        {
            "rubric_item": "Rubric 4 (Task 2): Make 'Theme' selector functional...",
            "original_model_eval": "No Issues",
            "original_model_justification": "N/A",
            "alternate_model_eval": "No Issues",
            "alternate_model_justification": "N/A (Code identical to Original)",
        },
        {
            "rubric_item": "Rubric 5 (Task 2): 'Display Text Size' toggle controls visibility/state...",
            "original_model_eval": "No Issues",
            "original_model_justification": "N/A",
            "alternate_model_eval": "No Issues",
            "alternate_model_justification": "N/A (Code identical to Original)",
        },
        {
            "rubric_item": "Rubric 6 (Task 2): Activate 'Layout' selector with visual feedback...",
            "original_model_eval": "No Issues",
            "original_model_justification": "N/A",
            "alternate_model_eval": "No Issues",
            "alternate_model_justification": "N/A (Code identical to Original)",
        },
        {
            "rubric_item": "Rubric 7 (Task 2): 'Suggest Placeholders' button and logic...",
            "original_model_eval": "No Issues",
            "original_model_justification": "N/A",
            "alternate_model_eval": "No Issues",
            "alternate_model_justification": "N/A (Code identical to Original)",
        },
        {
            "rubric_item": "Rubric 8 (Task 2): Non-functional 'Display Text Case' toggle...",
            "original_model_eval": "Major Issues",
            "original_model_justification": "The 'Display Text Case' toggle switch (id='displayTextCase') in the sidebar is visible but has no JavaScript event listener or functionality. The separate 'Support only uppercase' checkbox (id='supportUppercase') handles uppercasing, but the toggle itself is non-operational.",
            "alternate_model_eval": "Major Issues",
            "alternate_model_justification": "The 'Display Text Case' toggle switch (id='displayTextCase') in the sidebar is visible but has no JavaScript event listener or functionality. (Code identical to Original)",
        },
        {
            "rubric_item": "Rubric 9 (Task 2): Overall UI Cohesion & Polish (Implicit/Subjective)...",
            "original_model_eval": "Minor Issues",
            "original_model_justification": "Minor inconsistencies or alignments possible in such a complex UI, e.g., alignment of 'Support only uppercase' checkbox label, or default browser styles for some inputs in dark mode not perfectly matching custom theme.",
            "alternate_model_eval": "Minor Issues",
            "alternate_model_justification": "Minor inconsistencies or alignments possible. (Code identical to Original)",
        },
        {
            "rubric_item": "Rubric 10 (Task 2): Ensure reasonable responsiveness (Implicit)...",
            "original_model_eval": "Minor Issues",
            "original_model_justification": "Complex two-column layout with fixed-width sidebar is likely to have usability issues (cramping, misalignment) on narrow screens without specific responsive CSS adaptations.",
            "alternate_model_eval": "Minor Issues",
            "alternate_model_justification": "Complex two-column layout likely to have usability issues on narrow screens. (Code identical to Original)",
        }
    ]

    print("--- Evaluation of Model Outputs - Task 2: Typography ---")
    for i, item_eval in enumerate(rubric_evaluations):
        print(f"\n{item_eval['rubric_item']}")
        print(f"  Original Model (Task 2, Turn 4):")
        print(f"    Evaluation: {item_eval['original_model_eval']}")
        print(f"    Justification: {item_eval['original_model_justification']}")
        print(f"  Alternate Model (Task 2):")
        print(f"    Evaluation: {item_eval['alternate_model_eval']}")
        print(f"    Justification: {item_eval['alternate_model_justification']}")
        print("-" * 40)

if __name__ == "__main__":
    display_evaluations_task2()
