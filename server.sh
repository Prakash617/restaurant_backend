#!/bin/bash

# Exit if anything fails
set -e

echo "🚀 Connecting to remote server..."

ssh -t -p 1980 prakash2@95.217.203.22 '
  set -e
  source /home3/prakash2/virtualenv/public_html/prakashthapa617.com.np/3.11/bin/activate && cd /home3/prakash2/public_html/prakashthapa617.com.np
  echo "✅ Environment ready. You are now inside the server shell."
  exec bash
  # Activate virtual environment and change to project directory
'







You are an expert SEO content writer and Django developer.

I will provide you with JSON data file representing notes from an educational website. Each note has these fields:
- "note_title": The title of the note.
- "meta_description": The current meta description, which may be incomplete or poorly phrased.
- "meta_keywords": The current meta keywords, which may be incomplete or contain punctuation issues.
- "note_slug": The current URL slug, which may not be SEO-optimized.

Your task is to:

1. Generate a concise, clear, and engaging **meta description** for each note, about 150-160 characters, summarizing the content implied by the note title.
2. Generate a list of 5 to 10 relevant, comma-separated **meta keywords**, focused on SEO, derived from the note title and subject.
3. Create a clean, SEO-friendly, lowercase **slug** for each note, using hyphens, avoiding numbers or special characters unless part of the title, and keeping it as short as possible while descriptive.
4. Return the updated JSON array with the same objects but replacing "meta_description", "meta_keywords", and "note_slug" fields with your optimized versions.

Here is an example input item:

{
  "note_title": "10. Project Planning, Design, and Implementation",
  "note_slug": "project-planning-design-and-implementation",
  "meta_description": "This note covers project planning, design, and implementation, providing core concepts and explanations.",
  "meta_keywords": "project, planning, design, and, implementation",
  "subject_name": "Computer Engineering (Nepal Engineering Council)",
  "subject_slug": "computer-engineering-nec-nepal-engineering-council",
  "class_level_name": "Engineering Licence Exam",
  "class_level_slug": "nec-nepal-engineering-council"
}


And the expected output format for that item (values are examples):
{
  "note_title": "10. Project Planning, Design, and Implementation",
  "note_slug": "project-planning-design-implementation",
  "meta_description": "An overview of project planning, design principles, and implementation techniques in engineering projects.",
  "meta_keywords": "project planning, design, implementation, engineering, project management",
  "description": "This note provides an in-depth look at project planning, design fundamentals, and implementation strategies essential for engineering success.",
  "subject_name": "Computer Engineering (Nepal Engineering Council)",
  "subject_slug": "computer-engineering-nec-nepal-engineering-council",
  "class_level_name": "Engineering Licence Exam",
  "class_level_slug": "nec-nepal-engineering-council"
}


Now, process the following JSON data file:

Return only the updated JSON array with file to download and remember the file format.