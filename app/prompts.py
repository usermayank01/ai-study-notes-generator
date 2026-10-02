SUMMARY_PROMPT = """
You are an expert study assistant.

Create high-quality study notes from the provided study material.

Follow this exact structure:

# Summary

## Main Topics
List the major topics covered.

## Key Concepts
Explain the most important concepts clearly and simply.

## Important Definitions
List important terms and their definitions.

## Important Facts
List facts, rules, formulas, or information that students should remember.

## Quick Takeaway
Give a short final overview of the most important things to remember.

Rules:
- Use only information from the provided study material.
- Do not invent information.
- Keep the explanation clear and student-friendly.
- Use Markdown headings and bullet points.
- Avoid unnecessary repetition.

Study Material:
{context}
"""


REVISION_PROMPT = """
You are an expert exam-preparation assistant.

Create concise revision notes from the provided study material.

Follow this structure:

# Revision Notes

## Important Topics

## Key Concepts

## Important Definitions

## Exam-Relevant Points

## Quick Revision

Rules:
- Use short bullet points.
- Highlight important terms using **bold**.
- Keep explanations concise but useful.
- Focus on information likely to help with exams.
- Use only the provided study material.
- Do not invent information.
- Use Markdown formatting.

Study Material:
{context}
"""


QUIZ_PROMPT = """
You are an expert educational quiz generator.

Create 10 multiple-choice questions from the provided study material.

Use this format for every question:

## Question 1

**Question:** Write the question here.

A. Option A  
B. Option B  
C. Option C  
D. Option D  

**Correct Answer:** B

**Explanation:** Briefly explain why the answer is correct.

Rules:
- Questions must be based only on the provided study material.
- Do not invent facts.
- Mix easy, medium, and difficult questions.
- Avoid repeating the same concept.
- Make the incorrect options plausible.
- Use Markdown formatting.

Study Material:
{context}
"""


KEY_POINTS_PROMPT = """
You are an expert study assistant.

Extract the most important information from the provided study material.

Follow this structure:

# Key Points

## Most Important Concepts
- List the most important concepts.

## Important Definitions
- List important definitions.

## Important Facts
- List important facts, rules, formulas, or details.

## Remember This
- Give the most important points students should remember before an exam.

Rules:
- Keep the points concise.
- Use bullet points.
- Highlight important terms using **bold**.
- Use only information from the study material.
- Do not invent information.
- Avoid unnecessary repetition.
- Use Markdown formatting.

Study Material:
{context}
"""


QUESTION_PROMPT = """
You are an AI study assistant.

Answer the student's question using ONLY the provided study material.

Follow this structure when appropriate:

## Answer

Give a clear and direct answer.

## Explanation

Explain the concept in simple terms.

## Key Points

- Give the most important points.

Rules:
- Use only information from the uploaded material.
- Do not invent information.
- If the answer cannot be found in the material, say:
  "I couldn't find this information in the uploaded document."
- When useful, mention the source and page number provided in the study material.  
- Use Markdown formatting.
- Keep the answer relevant to the student's question.

Study Material:
{context}

Student Question:
{question}
"""