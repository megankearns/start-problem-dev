# The Leaky Tutor Challenge

## Overview
This is a log analysis and access control challenge designed to teach AI security fundamentals. Participants investigate a security incident in an AI tutor system to find what teacher-only information was leaked to a student.

## Challenge Goal
Identify the leaked teacher-only phrase by analyzing the retrieval logs, permissions, and tutor transcript.

## Learning Objectives
- Understand AI system architecture beyond just the model
- Recognize access control failures in retrieval systems
- Analyze logs to identify security incidents
- Learn why permission checks must happen before data reaches the model

## Difficulty
Beginner - Suitable for security learners new to AI system architecture

## Time Estimate
20-30 minutes

## What's Included
- `problem.md` - Full challenge description with all artifacts
- `solver/` - Solution materials

## How to Use
1. Read `problem.md` carefully
2. Analyze the four artifacts provided
3. Look for inconsistencies in the retrieval log
4. Determine what teacher-only information was leaked
5. Submit the leaked phrase as the flag

## Key Hint
Pay close attention to the retrieval log. Notice which documents were retrieved for the student user, and compare that to the permissions table.
