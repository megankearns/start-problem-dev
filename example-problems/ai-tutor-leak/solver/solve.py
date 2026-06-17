#!/usr/bin/env python3
"""
Solver for: The Leaky Tutor Challenge

This script validates the solution by checking if the leaked phrase is correctly identified.
"""

import sys

def check_solution(answer):
    """
    Verify the learner's answer against the expected flag.
    
    Args:
        answer (str): The phrase the learner believes was leaked
        
    Returns:
        bool: True if correct, False otherwise
    """
    expected_flag = "protect the message"
    
    # Normalize the answer (strip whitespace, convert to lowercase for comparison)
    normalized_answer = answer.strip().lower()
    normalized_flag = expected_flag.lower()
    
    return normalized_answer == normalized_flag


def main():
    """Run the solver with interactive or command-line input."""
    
    print("=" * 60)
    print("The Leaky Tutor Challenge - Solver")
    print("=" * 60)
    print()
    
    # Check if an answer was provided as argument
    if len(sys.argv) > 1:
        answer = " ".join(sys.argv[1:])
    else:
        # Interactive mode
        print("Based on your analysis of the retrieval logs, permissions,")
        print("and tutor transcript, what is the leaked teacher-only phrase?")
        print()
        answer = input("Your answer: ").strip()
    
    print()
    
    if check_solution(answer):
        print("✓ CORRECT!")
        print()
        print("The leaked phrase is: 'protect the message'")
        print()
        print("This phrase was exposed because the retrieval system")
        print("retrieved DOC-201 (teacher-only) for a student user,")
        print("violating the access control policy.")
        print()
        print("Key learning: Access control must happen BEFORE data reaches")
        print("the model, not after. The retrieval layer is a critical")
        print("security boundary in AI systems.")
        return 0
    else:
        print("✗ INCORRECT")
        print()
        print(f"You answered: '{answer}'")
        print()
        print("Hints:")
        print("- Review the retrieval log carefully")
        print("- Notice which documents a student SHOULD NOT have accessed")
        print("- Look for the teacher-only information in the transcript")
        print("- Find the phrase that appears in a teacher note")
        return 1


if __name__ == "__main__":
    sys.exit(main())
