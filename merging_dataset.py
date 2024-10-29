import pandas as pd
import numpy as np

# Load the datasets
df1 = pd.read_csv('Mental Health Survey - ANAC 7.csv')
df2 = pd.read_csv('Suicides in India 2001-2012.csv')
df3 = pd.read_csv('mental_health_finaldata_1.csv')
df4 = pd.read_csv('StudentMentalHealth.csv')
df5 = pd.read_csv('District_Wise_Mental_Health_Patients_2021-22.csv')
df6 = pd.read_csv('survey.csv')
df7 = pd.read_csv('Deepression.csv')
df8 = pd.read_csv('anxiety-disorders-treatment-gap.csv')



df1_clean = df1[~df1.index.duplicated(keep='first')]
df2_clean = df2[~df2.index.duplicated(keep='first')]
df3_clean = df3[~df3.index.duplicated(keep='first')]
df4_clean = df4[~df4.index.duplicated(keep='first')]
df5_clean = df5[~df5.index.duplicated(keep='first')]
df6_clean = df6[~df6.index.duplicated(keep='first')]
df7_clean = df7[~df7.index.duplicated(keep='first')]
df8_clean = df8[~df8.index.duplicated(keep='first')]

# Create a new dataframe with the finalized columns
merged_df = pd.DataFrame()

# Demographic Factors
merged_df['Gender'] = pd.concat([df1_clean['Your Gender'], df2_clean['Gender'], df3_clean['Gender'], df4_clean['Choose your gender']])
merged_df['Age group'] = pd.concat([df1_clean['Which age group you would fall into ?'], df2_clean['Age_group'], df3_clean['Age'], df4_clean['Age']])
merged_df['Marital status'] = df4_clean['Marital status']
merged_df['Occupation'] = df3_clean['Occupation']
merged_df['State'] = pd.concat([df2_clean['State'], df6_clean['state']]).reset_index(drop=True)
merged_df['DISTRICT'] = df5_clean['DISTRICT ']

# Mental health activities
merged_df['Meditation and Exercises'] = pd.concat([df1_clean['Of the below activities, which of the items you do'], df6_clean['wellness_program']]).reset_index(drop=True)
merged_df['Sleeping time'] = df7_clean['Sleep']
merged_df['Family Relations'] = pd.concat([df1_clean['Given a rating of 1 to 10, how much are you respected within your immediate family circle ?'], df6_clean['family_history']]).reset_index(drop=True)
merged_df['Relationship status'] = df1_clean['How would you describe your relationship like ?']
merged_df['Concentration'] = df7_clean['Concentration']
merged_df['ever felt depressed'] = df4_clean['Do you have Depression?']
merged_df['taking any treatment?'] = pd.concat([df4_clean['Did you seek any specialist for a treatment?'], df8_clean['Potentially adequate treatment, conditional'], df6_clean['treatment']]).reset_index(drop=True)
merged_df['Phys_health_interview'] = df6_clean['phys_health_interview']
merged_df['Suicidal attempt?'] = df7_clean['Suicidal Ideation']
merged_df['Panic attacks?'] = df7_clean['Panic Attacks']
merged_df['Hopelessness'] = df7_clean['Hopelessness']
merged_df['Depression State'] = df7_clean['Depression State']
merged_df['Social_Weakness'] = df3_clean['Social_Weakness']

# Reset index
merged_df.reset_index(drop=True, inplace=True)

# Handle missing values
merged_df.fillna('Unknown', inplace=True)

# Save the merged dataset
merged_df.to_csv('merged_mental_health_dataset.csv', index=False)

print("Merged dataset has been created and saved as 'merged_mental_health_dataset.csv'")
print("Shape of the merged dataset:", merged_df.shape)
print("\nColumn names:")
print(merged_df.columns.tolist())
print("\nSample data:")
print(merged_df.head())