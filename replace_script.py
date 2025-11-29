
import re

file_path = "/Users/fernandopitso/projects/500bears/Vectorial_Consensus/index.html"

old_code_block = """            if (concept) {
                conceptualizeIdea(concept);
            }"""

new_code_block = """            if (concept) {
                conceptualizeIdea(concept);
            } else {
                alert("Please enter a concept.");
            }"""

with open(file_path, 'r') as f:
    content = f.read()

modified_content = content.replace(old_code_block, new_code_block)

with open(file_path, 'w') as f:
    f.write(modified_content)

print("Replacement complete.")
