import pandas as pd

df = pd.read_csv('Medical_Appointment_No_Shows.csv', sep='\t')

print("🔍 Missing values before cleaning:\n", df.isnull().sum())

df = df.drop_duplicates()

if 'Gender' in df.columns:
    df['Gender'] = df['Gender'].str.strip().str.upper()
if 'Neighbourhood' in df.columns:
    df['Neighbourhood'] = df['Neighbourhood'].str.strip().str.title()
if 'No-show' in df.columns:
    df['No-show'] = df['No-show'].str.strip().str.upper()

if 'ScheduledDay' in df.columns:
    df['ScheduledDay'] = pd.to_datetime(df['ScheduledDay'], errors='coerce')
if 'AppointmentDay' in df.columns:
    df['AppointmentDay'] = pd.to_datetime(df['AppointmentDay'], errors='coerce')

df.columns = df.columns.str.strip().str.lower().str.replace('-', '_').str.replace(' ', '_')

if 'age' in df.columns:
    df['age'] = df['age'].astype(int)

df.to_csv('cleaned_medical_appointments.csv', index=False, sep=' ')

print("✅ Dataset cleaned and saved as 'cleaned_medical_appointments.csv'")
