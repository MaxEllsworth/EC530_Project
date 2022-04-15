
<!-- markdownlint-configure-file {
  "MD013": {
    "code_blocks": false,
    "tables": false
  },
  "MD033": false,
  "MD041": false
} -->

<div align="center">

# Medical Device Data Application
---
</div>

<!--ts-->
   * [Workflow](#Workflow)
   * [Databases](#Databases)
   * [Chat Module](#Chat_Module)
   * [Branching Strategy](#Branching_Strategy)

<!--te-->
# Workflow
![Alt Text](img/agile_env.png)*`flake8`, `coverage` added in `main.yml`* 

# Databases
![Alt Text](img/original_schema.png)*A schema for a variety of database tables is documented in the json format*

# Chat Module
## User Story: 
The purpose of the chat module is to facilitate communcation between the patient and a medical profesisonal (doctor or nurse). 

## API
## Data Model

# 
# Branching Stragety
 - For now, all commits will be made to main
 - In the future, a `dev` branch could be added for pushes of code that is:
   - experimental
   - going to fail unit tests
   - an incomplete component of a larger module or function

# Phase Zero / One
- Set up an Agile environment
- Set up testing
- Add a README
- Determine a branching strategy: when to and when not to add to `main`
- Create a device interface with the following:
  - Data fields
  - Error conditions
  - The following fields:
    - Temperature
    - Blood pressure
    - Pulse
    - Oximeter
    - Weight
    - Glucometer
- Implement a shell of the device interface
- Implement unit tests
- Implement a simulation to send data via an example program to help users of your system
- Document the interface well


# In-Class Suggestions
- What to include in the user table:
  - ID
  - First name
  - Last name
  - Role: make this an array of roles, since each user can have multiple roles 
  - Weight
  - Height
  - Medical Card
  - Address
  - Primary Care
  - Insurance
  - Billing info
  - Medications
  - Family
  - Gender
  - Medical History
  - Allergies
- What to include in the device table:
  - Date of purchase
  - Device type
  - MAC Address
  - User assigned to
  - Firmware version
  - Software version
  - Assigner (?)

<!-- https://wiki.python.org/moin/DocumentationTools -->
<!--https://www.npmjs.com/package/redoc-cli-->

<!--source .python_venv/bin/activate && pip freeze > requirements.txt && git pull origin main && echo "`date -d @$(date +%s)`" >> pushes.py && git add . &&  git commit -m "`date -d @$(date +%s)`"&& git push origin main-->

