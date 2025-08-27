# import os
# import re
# import shutil
# from docx import Document
# from docx.document import Document as _Document
# from docx.oxml.text.paragraph import CT_P
# from docx.oxml.table import CT_Tbl
# from docx.table import _Cell, Table
# from docx.text.paragraph import Paragraph

# # --- STEP 1: Define the Table of Contents ---
# # We will use this as the absolute source of truth for splitting the document.
# TOC_STRING = """
# Designer Materials
# Tutorial 0: Foundational Concepts
# Studio Console
# Introduction
# Tutorial 1: Creating a Login page
# Practical 1.1: Add Background Image
# Practical 1.2: Create Layout
# Practical 1.3: Add 4 Text components
# Practical 1.4: Add Form Template
# Tutorial 2: Creating the Landing Page
# Practical 2.1: Create Initial Layout
# Practical 2.2: Create heading
# Practical 2.3: Add Image Background to root page
# Practical 2.4: Add Button Group
# Practical 2.5: Create responsive card
# Tutorial 3: Creating the Listing Page (Optional)
# Practical 3.1: Create Initial Layout
# Practical 3.2: Create Heading and Breadcrumb
# Practical 3.3: Create Search form
# Practical 3.4: Create List header
# Practical 3.5: Create Table
# Tutorial 4: Creating a Form with Steps
# Introduction: Form Fields
# Introduction: Form Validation
# Practical 4.1: Setting up the Form
# 4.1.1 Creating the Form skeleton
# 4.1.2 Form Setup Complete
# 4.1.3 The Source Code Panel
# Practical 4.2: Form Fields and Form Validation
# 4.2.1 Context
# 4.2.2 Objective
# 4.2.4 Course Info Form Validation
# 4.2.5 Form Completion
# Practical 4.3: Create the ‘Instructor Particulars’ Form
# 4.3.1 Context
# 4.3.2 Objective
# 4.3.3 Requirements
# 4.3.4 Hints
# 4.3.5 Expected Result
# Practical 4.4: ‘Class Location’ Form
# 4.4.1 Context
# 4.4.2 Objective
# 4.4.3 Requirements
# 4.4.4 Creating a Field with 2 inputs
# 4.4.5 Styling for the Inputs
# 4.4.6 Validation for both input fields
# 4.4.8 Form Completion
# Practical 4.5: Class Schedule Form
# 4.5.1 Context
# 4.5.2 Objective
# 4.5.3 Requirements
# 4.5.4 Custom Date Validation
# 4.5.5 Creating the Form field that can add new Rows
# 4.5.6 Form Completion
# Practical 4.6: Cascade Dropdown
# 4.6.1 Context
# 4.6.2 Requirements
# 4.6.3 Adding the Logic
# Practical 4.7: Setting field values using Form Variables (Optional)
# 4.7.1 Context
# 4.7.2 Requirements
# 4.7.3 Adding the ‘MyInfo’ Button
# 4.7.4 Adding the logic
# Practical 4.8: Binding it all together
# 4.8.1 Adding the code
# 4.8.2 Bind currentStep variable to Step Component
# 4.8.3 OnClick Events for the Next buttons
# 4.8.4 Set conditions for the Forms to be visible
# Practical 4.9: Modal Dialog Box
# 4.9.1 Steps for Creating a Modal Dialog
# 4.9.2 Adding the logic for the Modal Dialog
# And Finally
# Additional Information
# Tutorial 5: Tables, Sorting and Pagination
# Practical 5.1: The Table Component
# 5.1.1 Setting up the Table Component
# 5.1.2 Setting the Table Headers
# 5.1.3 Adding a Static Dataset to the Table
# Practical 5.2: Table Sorting & Pagination
# 5.2.1 Setup
# 5.2.2 Sorting
# 5.2.3 Pagination
# 5.2.4 Page Sizing
# Practical 5.3: Download functionality (Optional)
# 5.3.1 Add a download button
# 5.3.2 Add the download code
# 5.3.3 Event bind the download button
# Tutorial 6: Charts and Graphs
# Practical 6.1: Adding Graph Components
# 6.1.1 Setup Steps
# 6.1.2 Adding a Bar Graph
# 6.1.3 Sending Data to the Graph
# 6.1.4 Adding a Pie Chart
# 6.1.5 Sending Data to the Graph
# Tutorial 7: Using External JS Libraries
# Practical 7.1: Importing a UUID JS Library (Demonstration)
# 7.1.1 Setup Steps
# 7.1.2 Adding the Library
# 7.1.3 Using the library
# Tutorial 8: Theme Designer
# Practical 8.1: Customize new theme
# Practical 8.2 Apply theme to your application
# Additional Information
# Tutorial 9: Preview Mode
# Practical 9.1: Preview Mode and Collaborative Commenting
# Practical 9.2: Navigator Creation / Page Linking
# 9.2.1 Navigator Creation
# 9.2.2 Customize Navigator Menu
# 9.2.3 Page Linking
# Practical 9.3: Page Tagging for External Review (Demonstration)
# Tutorial 10: Page Improvement
# Practical 10.1: Page Analysis with Page Scan (Demonstration)
# Practical 10.2: Mobile Responsive UI (Demonstration)
# Practical 10.3: Translation using i18n (Demonstration)
# Tutorial 11: Page Import From Template
# Tutorial 12: Main and Micro Applications
# Practical 12.1 Export and Import Pages to Main/Micro Apps (Optional)
# Practical 12.2 Add Action Page Type to Main App (Optional)
# Tutorial 13: Build screen skeleton
# Layout: Section vs Block
# Layout: Block vs Cell
# Block VS Cell
# Example: Webpage walkthrough example
# Step 1: Create layout
# Step 2: Divide cell horizontally for left block
# Step 3: Split cell into two
# Step 4: Add a card component
# Step 5: Add 3 Card components
# Step 6: Add a table component
# Step 7: Add components to the right block
# Example
# Developer Materials
# Architecture
# Tutorial 14: Git Setup & Creation of New Branch
# Practical 14.1: Connect with Gitlab
# Practical 14.2: Initialize Git Repository
# 14.2.1 Frontend - Initialize Git Repository
# 14.2.2 Backend - Initialize Git Repository
# Practical 14.3: Create and Switch to new branch
# 14.3.1 Frontend Git Branch Management
# 14.3.2 Backend Git Branch Management (Optional)
# Tutorial 15: Master Code Integration
# Practical 15.1: Integrating Master Code
# Practical 15.2: Multi language support (Optional)
# Tutorial 16: Custom Login Page Integration
# Practical 16.1: Login Page Integration
# Tutorial 17: Database Designer
# Practical 17.1: Setup Database and tables
# Connect to the PostgreSQL Server
# Creating a New Table
# Adding Rows to Table
# Benefits of Database designer
# Tutorial 18: Service / API Designer
# Practical 18.1: Creating Service and Controller
# Navigating the Service / API Designer
# Adding a Service
# Adding a Database
# Adding a Controller
# Adding Datasource & Configure API Endpoints
# Tutorial 19: Datasource API Binding
# Practical 19.1: Binding API to Table (GET)
# Practical 19.2: Binding API to Form submission (POST)
# Adding DataType & Datasource
# Import Remaining APIs
# Binding to FormSubmission
# Binding POST Form using “Encode”
# Tutorial 20: Error Handling
# Practical 20.1: Redirect to custom error page
# Tutorial 21: Workflow Designer
# Practical 21.1: Using default workflow (Claim-based routing)
# Practical 21.2: Designing and Deploying custom workflow
# Practical 21.3: Workflow observability
# Tutorial 22: Code Generation (Backend)
# Practical 22.2: Generating and Running Backend Code
# Generate Code
# Understanding Generated Backend Code Structure
# Tutorial 23: Profile for local development
# Practical 23.1: Running be-services
# Practical 23.2: Update Profile feature
# Tutorial 24: Customize Privilege for Page Permission
# Tutorial 25: Code Generation (Frontend)
# Practical 25.1: Generating and Running Frontend Code
# Installation of Necessary Prerequisites:
# Generate Code
# Running nginx
# Running the generated code
# Triggering Error
# Tutorial 26: Push and Merge Code to Git
# Practical 26.1: Frontend Git Management
# Create New Tag and Git Push
# Merge Code to Main Branch + Push Main Branch
# Practical 26.2: Backend Git Management (Optional)
# Create New Tag and Git Push
# Merge Code to Main Branch + Push Main Branch
# Additional Information - Branch Management
# Tutorial 27: Job Scheduler
# Practical 27.1: Creating and Running Job (Demonstration)
# Tutorial 28: IAM
# Court Case Example: How "Subject" Works
# Practical Example: Judge Case Assignment
# Practical 28.1: Assignment of custom menu (Optional)
# Practical 28.2: Endpoint Assignment (Optional)
# """

# def get_header_set_from_toc(toc_string):
#     """Processes the raw ToC string into a clean set of headers for fast lookups."""
#     headers = set()
#     for line in toc_string.strip().split('\n'):
#         # Remove page numbers and clean up the line
#         cleaned_line = re.sub(r'\s+\d+$', '', line).strip()
#         # Remove leading numbers/bullets like "4.1.1" as they might not be in the text
#         cleaned_line = re.sub(r'^[\d\s\.]+', '', cleaned_line).strip()
#         if cleaned_line:
#             headers.add(cleaned_line)
#     # Add back some specific headers that might have been cleaned too aggressively
#     headers.add("Block VS Cell") 
#     return headers

# def sanitize_filename(name):
#     """Removes invalid characters for file/folder names."""
#     name = name.replace(' ', '_')
#     return re.sub(r'[\\/*?:"<>|]', "", name).strip()

# def iter_block_items(parent):
#     """Yields each paragraph and table in document order."""
#     if isinstance(parent, _Document): parent_elm = parent.element.body
#     elif isinstance(parent, _Cell): parent_elm = parent._tc
#     else: raise ValueError("Unsupported parent type")
#     for child in parent_elm.iterchildren():
#         if isinstance(child, CT_P): yield Paragraph(child, parent)
#         elif isinstance(child, CT_Tbl): yield Table(child, parent)

# def save_section(section_path, section_name, content):
#     """Saves the collected Markdown content to a file."""
#     if not content.strip(): return
#     os.makedirs(section_path, exist_ok=True)
#     file_path = os.path.join(section_path, f"{sanitize_filename(section_name)}.md")
#     with open(file_path, "w", encoding="utf-8") as f:
#         f.write(content)
#     print(f"Saved section: {file_path}")

# def process_docx_by_toc(doc_path, output_root="output"):
#     """Splits a .docx into numbered section folders based on the ToC."""
#     if os.path.exists(output_root):
#         shutil.rmtree(output_root)
#     os.makedirs(output_root)

#     document = Document(doc_path)
#     header_set = get_header_set_from_toc(TOC_STRING)

#     image_parts = {
#         rel_id: rel.target_part
#         for rel_id, rel in document.part.rels.items()
#         if "image" in rel.target_ref
#     }
    
#     current_section_content = ""
#     current_section_name = "00_Introduction"
#     section_counter = 0
#     current_section_path = os.path.join(output_root, f"{section_counter:03d}_{sanitize_filename(current_section_name)}")
#     image_counter = 0

#     for block in iter_block_items(document):
#         if isinstance(block, Paragraph):
#             paragraph_text = block.text.strip()
#             # Clean the text the same way we cleaned the ToC headers for a better match
#             cleaned_paragraph_text = re.sub(r'^[\d\s\.]+', '', paragraph_text).strip()

#             # --- NEW LOGIC: Check if the paragraph text is in our header set ---
#             if paragraph_text in header_set or (cleaned_paragraph_text in header_set and cleaned_paragraph_text):
#                 print(f"Found header: '{paragraph_text}'")
#                 save_section(current_section_path, current_section_name, current_section_content)
                
#                 section_counter += 1
#                 current_section_name = paragraph_text
#                 folder_name = f"{section_counter:03d}_{sanitize_filename(current_section_name)}"
#                 current_section_path = os.path.join(output_root, folder_name)
                
#                 current_section_content = f"# {paragraph_text}\n\n"
#             else:
#                 current_section_content += paragraph_text + "\n\n"

#             # Image extraction logic (remains the same)
#             for run in block.runs:
#                 for inline_shape in run.element.xpath('.//wp:inline'):
#                     blip_embed_query = inline_shape.xpath('.//a:blip/@r:embed')
#                     if blip_embed_query:
#                         r_id = blip_embed_query[0]
#                         if r_id in image_parts:
#                             image_part = image_parts[r_id]
#                             section_img_dir = os.path.join(current_section_path, "images")
#                             os.makedirs(section_img_dir, exist_ok=True)
#                             ext = image_part.content_type.split('/')[-1]
#                             image_filename = f"image_{image_counter}.{ext}"
#                             image_path = os.path.join(section_img_dir, image_filename)
#                             with open(image_path, "wb") as img_file:
#                                 img_file.write(image_part.blob)
#                             current_section_content += f"![Image Description](./images/{image_filename})\n\n"
#                             image_counter += 1

#     save_section(current_section_path, current_section_name, current_section_content)

# # --- HOW TO USE ---
# process_docx_by_toc("converted_document.docx")

# print("\nProcessing complete!")
# print("Check the 'output' folder for your structured documentation.")



import os
import re
import shutil
from docx import Document
from docx.document import Document as _Document
from docx.oxml.text.paragraph import CT_P
from docx.oxml.table import CT_Tbl
from docx.table import _Cell, Table
from docx.text.paragraph import Paragraph

# --- STEP 1: Define the list of all headers from the ToC ---
TOC_STRING = """
Designer Materials
Tutorial 0: Foundational Concepts
Studio Console
Introduction
Tutorial 1: Creating a Login page
Practical 1.1: Add Background Image
Practical 1.2: Create Layout
Practical 1.3: Add 4 Text components
Practical 1.4: Add Form Template
Tutorial 2: Creating the Landing Page
Practical 2.1: Create Initial Layout
Practical 2.2: Create heading
Practical 2.3: Add Image Background to root page
Practical 2.4: Add Button Group
Practical 2.5: Create responsive card
Tutorial 3: Creating the Listing Page (Optional)
Practical 3.1: Create Initial Layout
Practical 3.2: Create Heading and Breadcrumb
Practical 3.3: Create Search form
Practical 3.4: Create List header
Practical 3.5: Create Table
Tutorial 4: Creating a Form with Steps
Introduction: Form Fields
Introduction: Form Validation
Practical 4.1: Setting up the Form
Practical 4.2: Form Fields and Form Validation
Practical 4.3: Create the ‘Instructor Particulars’ Form
Practical 4.4: ‘Class Location’ Form
Practical 4.5: Class Schedule Form
Practical 4.6: Cascade Dropdown
Practical 4.7: Setting field values using Form Variables (Optional)
Practical 4.8: Binding it all together
Practical 4.9: Modal Dialog Box
And Finally
Additional Information
Tutorial 5: Tables, Sorting and Pagination
Practical 5.1: The Table Component
Practical 5.2: Table Sorting & Pagination
Practical 5.3: Download functionality (Optional)
Tutorial 6: Charts and Graphs
Practical 6.1: Adding Graph Components
Tutorial 7: Using External JS Libraries
Practical 7.1: Importing a UUID JS Library (Demonstration)
Tutorial 8: Theme Designer
Practical 8.1: Customize new theme
Practical 8.2 Apply theme to your application
Tutorial 9: Preview Mode
Practical 9.1: Preview Mode and Collaborative Commenting
Practical 9.2: Navigator Creation / Page Linking
Practical 9.3: Page Tagging for External Review (Demonstration)
Tutorial 10: Page Improvement
Practical 10.1: Page Analysis with Page Scan (Demonstration)
Practical 10.2: Mobile Responsive UI (Demonstration)
Practical 10.3: Translation using i18n (Demonstration)
Tutorial 11: Page Import From Template
Tutorial 12: Main and Micro Applications
Practical 12.1 Export and Import Pages to Main/Micro Apps (Optional)
Practical 12.2 Add Action Page Type to Main App (Optional)
Tutorial 13: Build screen skeleton
Layout: Section vs Block
Layout: Block vs Cell
Block VS Cell
Example: Webpage walkthrough example
Developer Materials
Architecture
Tutorial 14: Git Setup & Creation of New Branch
Practical 14.1: Connect with Gitlab
Practical 14.2: Initialize Git Repository
Practical 14.3: Create and Switch to new branch
Tutorial 15: Master Code Integration
Practical 15.1: Integrating Master Code
Practical 15.2: Multi language support (Optional)
Tutorial 16: Custom Login Page Integration
Practical 16.1: Login Page Integration
Tutorial 17: Database Designer
Practical 17.1: Setup Database and tables
Tutorial 18: Service / API Designer
Practical 18.1: Creating Service and Controller
Tutorial 19: Datasource API Binding
Practical 19.1: Binding API to Table (GET)
Practical 19.2: Binding API to Form submission (POST)
Tutorial 20: Error Handling
Practical 20.1: Redirect to custom error page
Tutorial 21: Workflow Designer
Practical 21.1: Using default workflow (Claim-based routing)
Practical 21.2: Designing and Deploying custom workflow
Practical 21.3: Workflow observability
Tutorial 22: Code Generation (Backend)
Practical 22.2: Generating and Running Backend Code
Tutorial 23: Profile for local development
Practical 23.1: Running be-services
Practical 23.2: Update Profile feature
Tutorial 24: Customize Privilege for Page Permission
Tutorial 25: Code Generation (Frontend)
Practical 25.1: Generating and Running Frontend Code
Tutorial 26: Push and Merge Code to Git
Practical 26.1: Frontend Git Management
Practical 26.2: Backend Git Management (Optional)
Tutorial 27: Job Scheduler
Practical 27.1: Creating and Running Job (Demonstration)
Tutorial 28: IAM
Court Case Example: How "Subject" Works
Practical Example: Judge Case Assignment
Practical 28.1: Assignment of custom menu (Optional)
Practical 28.2: Endpoint Assignment (Optional)
"""

# --- STEP 2: Define the keywords that signal a new folder should be created ---
MAJOR_HEADER_KEYWORDS = (
    "Tutorial",
    "Designer Materials",
    "Developer Materials",
    "Architecture",
    "And Finally",
    "Additional Information"
)

def get_header_set_from_toc(toc_string):
    """Processes the raw ToC string into a clean set of headers."""
    headers = set(line.strip() for line in toc_string.strip().split('\n') if line.strip())
    return headers

def sanitize_filename(name):
    """Removes invalid characters for file/folder names and shortens it."""
    name = name.replace(' ', '_')
    sanitized = re.sub(r'[\\/*?:"<>|]', "", name).strip()
    return sanitized[:100] # Limit filename length

def iter_block_items(parent):
    """Yields each paragraph and table in document order."""
    if isinstance(parent, _Document): parent_elm = parent.element.body
    elif isinstance(parent, _Cell): parent_elm = parent._tc
    else: raise ValueError("Unsupported parent type")
    for child in parent_elm.iterchildren():
        if isinstance(child, CT_P): yield Paragraph(child, parent)
        elif isinstance(child, CT_Tbl): yield Table(child, parent)

def save_section(section_path, section_name, content):
    """Saves the collected Markdown content to a file."""
    if not content.strip(): return
    os.makedirs(section_path, exist_ok=True)
    file_path = os.path.join(section_path, f"{sanitize_filename(section_name)}.md")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Saved section: {file_path}")

def process_docx_by_major_sections(doc_path, output_root="output"):
    """Splits a .docx into folders based on major keywords like 'Tutorial'."""
    if os.path.exists(output_root):
        shutil.rmtree(output_root)
    os.makedirs(output_root)

    document = Document(doc_path)
    header_set = get_header_set_from_toc(TOC_STRING)

    image_parts = {
        rel_id: rel.target_part
        for rel_id, rel in document.part.rels.items() if "image" in rel.target_ref
    }
    
    current_section_content = ""
    current_section_name = "00_Introduction"
    section_counter = 0
    current_section_path = os.path.join(output_root, f"{section_counter:02d}_{sanitize_filename(current_section_name)}")
    image_counter = 0

    for block in iter_block_items(document):
        if isinstance(block, Paragraph):
            paragraph_text = block.text.strip()

            is_heading = paragraph_text in header_set
            is_major_heading = any(keyword in paragraph_text for keyword in MAJOR_HEADER_KEYWORDS)

            if is_heading and is_major_heading:
                print(f"Found Major Header: '{paragraph_text}'")
                save_section(current_section_path, current_section_name, current_section_content)
                
                section_counter += 1
                current_section_name = paragraph_text
                folder_name = f"{section_counter:02d}_{sanitize_filename(current_section_name)}"
                current_section_path = os.path.join(output_root, folder_name)
                
                # Start new content with a top-level Markdown header
                current_section_content = f"# {paragraph_text}\n\n"
            
            elif is_heading and not is_major_heading:
                # This is a sub-heading, add it to the current content
                current_section_content += f"## {paragraph_text}\n\n"
            
            else:
                # This is regular content
                current_section_content += paragraph_text + "\n\n"

            # Image extraction logic
            for run in block.runs:
                for inline_shape in run.element.xpath('.//wp:inline'):
                    blip_embed_query = inline_shape.xpath('.//a:blip/@r:embed')
                    if blip_embed_query:
                        r_id = blip_embed_query[0]
                        if r_id in image_parts:
                            image_part = image_parts[r_id]
                            section_img_dir = os.path.join(current_section_path, "images")
                            os.makedirs(section_img_dir, exist_ok=True)
                            ext = image_part.content_type.split('/')[-1]
                            image_filename = f"image_{image_counter}.{ext}"
                            image_path = os.path.join(section_img_dir, image_filename)
                            with open(image_path, "wb") as img_file:
                                img_file.write(image_part.blob)
                            current_section_content += f"![Image Description](./images/{image_filename})\n\n"
                            image_counter += 1

    save_section(current_section_path, current_section_name, current_section_content)

# --- HOW TO USE ---
process_docx_by_major_sections("KAIZEN Training Material (Combined) v2.3_compressed (1).docx")

print("\nProcessing complete!")
print("Check the 'output' folder for your structured documentation.")