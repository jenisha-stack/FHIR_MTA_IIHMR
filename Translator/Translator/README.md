This folder represents the Translator layer of the MTA pipeline.

The Translator converts legacy RMHC CSV data into FHIR-compliant
Transaction Bundles.

The file:
sample_output/patient_bundle.json

demonstrates:
- Creation of Patient, Encounter and Observation resources
- UUID-based internal referencing
- A single atomic transaction bundle
- No orphaned clinical records
- Ready-to-ingest format for a FHIR server
