Source System: RMHC Legacy CSV  
Target System: FHIR Transaction Bundle

Mapping:

CSV Field → FHIR Element

patient_id → Patient.identifier  
patient_name → Patient.name.text  
gender → Patient.gender  
phone → Patient.telecom  
address → Patient.address.text  

height_cm → Observation (Body Height)  
weight_kg → Observation (Body Weight)  
waist_cm → Observation (Waist Circumference)  
hip_cm → Observation (Hip Circumference)  

Derived:
BMI = weight / (height in meters²)  
WHR = waist / hip  

All mapped resources are wrapped in a single Transaction Bundle
to guarantee atomicity.
