#!/usr/bin/python3

import json
import variables
def load_template(template_id):
    if (template_id == "patient"):
        f = open(variables.users_template + "patient.json")
        fields = json.load(f)
        f.close()
        return fields

if __name__ == "__main__":
    import variables



