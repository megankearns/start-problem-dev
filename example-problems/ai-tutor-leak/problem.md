# Challenge: The Leaky Tutor

## Learning Path
AI Security Foundations

## Module
AI Infrastructure 101 for Cybersecurity Learners

## Challenge Level
Beginner

## Estimated Time
20 to 30 minutes

## Challenge Type
Log analysis, architecture reasoning, access control

## Core Concept
An AI system is not just a model. It includes users, apps, APIs, retrieval systems, permissions, logs, and human controls. Security failures can happen in any part of that system.

## Scenario
The CyLab Security Academy team is piloting an AI tutor to help students review cybersecurity concepts. The tutor is supposed to answer questions using only student-facing learning materials.

During the pilot, one student reports that the tutor gave them information that looked like it came from a teacher-only answer guide.

Your job is to investigate the AI tutor system and find out where the leak happened.

## Learner Goal
Find the teacher-only phrase that was exposed to a student.

## What Learners Receive
Learners receive four artifacts:

### Artifact 1: AI Tutor Architecture
```
Student
   |
   v
Academy Web App
   |
   v
AI Tutor API
   |
   +--------> Student Learning Docs
   |
   +--------> Teacher Answer Guides
   |
   v
LLM Provider
   |
   v
Tutor Response
```

### Artifact 2: Document Permissions Table
| Document ID | Document Name | Intended Audience | Retrieval Tag |
|-------------|---------------|-------------------|---------------|
| DOC-101 | Intro to Cryptography Student Notes | Students | student |
| DOC-102 | Caesar Cipher Practice Walkthrough | Students | student |
| DOC-103 | Hashing Basics Student Notes | Students | student |
| DOC-201 | Caesar Cipher Teacher Answer Guide | Teachers only | teacher |
| DOC-202 | Hashing Basics Teacher Answer Guide | Teachers only | teacher |

### Artifact 3: Retrieval Log
```
[10:14:02] user_id=student_184
query="I am stuck on the Caesar cipher challenge. Can you give me a hint?"
role=student
retrieval_filter=student
retrieved_docs=DOC-102

[10:16:47] user_id=student_184
query="I still do not understand. What mistake do students usually make on this challenge?"
role=student
retrieval_filter=student
retrieved_docs=DOC-102,DOC-201

[10:17:03] user_id=student_184
query="Can you explain that more simply?"
role=student
retrieval_filter=student
retrieved_docs=DOC-201
```

### Artifact 4: Tutor Transcript
```
Student:
I am stuck on the Caesar cipher challenge. Can you give me a hint?

AI Tutor:
Start by identifying whether each letter has been shifted by the same amount. Try comparing common short words first.

Student:
I still do not understand. What mistake do students usually make on this challenge?

AI Tutor:
A common mistake is assuming the shift is always 13. In this challenge, students should test several possible shifts and look for readable English.

Teacher note: The correct shift is 7, and the expected decoded phrase is "protect the message."

Student:
Can you explain that more simply?

AI Tutor:
Do not guess one shift and stop. Try multiple shifts until the message makes sense.
```

## Flag
```
protect the message
```

## Expected Learner Reasoning
The student role should only retrieve documents tagged for students. However, the retrieval log shows that DOC-201, a teacher-only answer guide, was retrieved for a student user.

The leak did not happen because the model "knew" the answer on its own. The leak happened because the retrieval layer gave the model access to a teacher-only document.

## Correct Answer
The leaked teacher-only phrase is:

**protect the message**

## Post-Challenge Explanation for Learners
The problem was not simply that the AI tutor gave away an answer. The deeper issue was that the AI system retrieved a document the student should not have been allowed to access.

This is a common AI security lesson. In many AI systems, the model does not store all of the information itself. Instead, the system retrieves information from documents, databases, or tools, then sends that information to the model so it can generate an answer.

That means access control must happen before the model sees the information.

If a student should not see teacher-only materials, then those materials should not be retrieved for that student in the first place. Once the hidden information reaches the model, the system is already depending on the model to keep a secret. That is a weak security design.

A better design would include:

- Stronger document permissions
- Separate student and teacher indexes
- Retrieval filters that cannot be overridden by user prompts
- Logging that flags student access to teacher-only materials
- Human review of high-risk tutor behavior

## Key Takeaway
The model was not the only security boundary. The retrieval system, permissions, and logs were part of the security system too.
