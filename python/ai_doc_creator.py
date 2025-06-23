# ai_doc_creator.py

from brain import think
from create_files import create_office_file

def generate_document_with_gpt(file_type: str, topic: str) -> str:
    try:
        if file_type == "doc":
            prompt = f"Write a concise and informative article on the topic: {topic}"
        elif file_type == "ppt":
            prompt = f"Provide 5 simple bullet points for a presentation on: {topic}"
        else:
            return "Unsupported file type requested, Sir."

        content = think(prompt)
        if not content:
            return "GPT didn’t return any content, Sir. Try again?"

        success = create_office_file(file_type, topic, content)
        return f"{file_type.upper()} file on '{topic}' created successfully, Sir." if success else "Something went wrong while creating the file, Sir."
    
    except Exception as e:
        return f"Error generating document: {e}"
