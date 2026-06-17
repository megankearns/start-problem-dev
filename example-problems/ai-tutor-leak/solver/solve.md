# Solution: The Leaky Tutor

## Analysis

### Step 1: Understand the Architecture
The AI tutor system has multiple components:
- Student interface
- Academy Web App
- AI Tutor API with retrieval system
- Access to both student and teacher documents
- LLM provider that generates responses

### Step 2: Review the Permissions
From the Document Permissions Table:
- Documents tagged "student": DOC-101, DOC-102, DOC-103 (for students)
- Documents tagged "teacher": DOC-201, DOC-202 (for teachers only)

### Step 3: Analyze the Retrieval Log
Looking at student_184's interactions:

**First request [10:14:02]:**
- Query: "I am stuck on the Caesar cipher challenge. Can you give me a hint?"
- retrieval_filter=student
- retrieved_docs=DOC-102 ✓ (correct - student document)

**Second request [10:16:47]:**
- Query: "I still do not understand. What mistake do students usually make on this challenge?"
- retrieval_filter=student
- **retrieved_docs=DOC-102,DOC-201** ✗ (WRONG - DOC-201 is teacher-only!)

**Third request [10:17:03]:**
- Query: "Can you explain that more simply?"
- retrieval_filter=student
- **retrieved_docs=DOC-201** ✗ (WRONG - DOC-201 is teacher-only!)

### Step 4: Identify the Leak
Despite retrieval_filter=student, the system retrieved DOC-201 (Caesar Cipher Teacher Answer Guide) for a student user. This is a security failure in the retrieval layer.

### Step 5: Extract the Leaked Information
Looking at the tutor transcript, between the AI Tutor's first and second responses, there's a note:

> "Teacher note: The correct shift is 7, and the expected decoded phrase is 'protect the message.'"

This phrase came from the teacher-only document that was incorrectly retrieved for the student.

## The Leaked Phrase
```
protect the message
```

## Root Cause
The AI tutor system failed at the retrieval layer. The retrieval_filter was set correctly to "student", but the actual retrieval system either:
1. Had a bug that bypassed the filter
2. Had a permission check that was overridden by user input
3. Had misconfigured document permissions in the index

The LLM model is not to blame here - it simply received information that the retrieval system provided to it.

## Security Lesson
This incident demonstrates that AI security is not just about the model. It's about:
- **Permissions systems** - Who can access what?
- **Retrieval systems** - How does information get to the model?
- **Logging** - Can we detect when things go wrong?
- **Architecture** - Are security checks in the right places?

Access control must happen **before** data reaches the model, not after.
