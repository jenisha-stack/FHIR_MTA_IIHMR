import csv
import uuid
import json

"""
This script represents the Translator layer of the MTA.
It demonstrates how legacy CSV data is converted into FHIR resources.
"""

with open("sample_input/rmhc_sample.csv") as file:
    reader = csv.DictReader(file)

    for row in reader:
        patient_uuid = str(uuid.uuid4())

        patient = {
            "resourceType": "Patient",
            "id": patient_uuid,
            "identifier": [
                {"system": "http://rmhc.org/sid/policy-id", "value": row["patient_id"]}
            ],
            "name": [
                {
                    "given": [row["first_name"]],
                    "family": row["last_name"]
                }
            ],
            "gender": row["gender"],
            "birthDate": row["dob"]
        }

        observation = {
            "resourceType": "Observation",
            "status": "final",
            "code": {
                "text": row["obs_code"]
            },
            "valueQuantity": {
                "value": float(row["obs_value"])
            },
            "effectiveDateTime": row["obs_date"],
            "subject": {
                "reference": f"urn:uuid:{patient_uuid}"
            }
        }

        bundle = {
            "resourceType": "Bundle",
            "type": "transaction",
            "entry": [
                {"resource": patient, "request": {"method": "POST", "url": "Patient"}},
                {"resource": observation, "request": {"method": "POST", "url": "Observation"}}
            ]
        }

        print(json.dumps(bundle, indent=2))
