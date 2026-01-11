# Mid-Term Assessment (MTA): FHIR Migration Translation Architecture

This repository is submitted as part of the Mid-Term Assessment (MTA) and demonstrates a FHIR Migration Translation Architecture using a Warehouse-based, three-layer model:

Infrastructure → Rulebook → Translator

---

## The Container Advantage
Docker is used to deploy the HAPI FHIR server in a consistent and reproducible way.
It eliminates dependency conflicts ("dependency hell") and ensures that the same
FHIR environment runs on every student machine regardless of operating system.

---

## Semantic Integrity
Legacy systems use magic strings such as "M/F" or "Y/N".
These are resolved using ConceptMaps and FHIR’s `$translate` operation to ensure
correct clinical coding and semantic accuracy.

---

## Transactional Atomicity
All resources are created using FHIR Transaction Bundles with UUID references.
This guarantees that:
- Patient and Observations are created together
- No orphaned clinical data exists
- Either the entire bundle is stored or none of it is

---

## Project Structure

