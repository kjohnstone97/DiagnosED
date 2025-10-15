import pandas as pd

ecds_df = pd.read_csv("ecds_codes_max.csv", usecols=["ECDS_SearchTerms", "SNOMED_UK_Preferred_Term", "Flag_ADS"], dtype=str)
ecds_df = ecds_df[ecds_df.ECDS_SearchTerms != "Code deprecated"]
ecds_df = ecds_df.drop_duplicates("SNOMED_UK_Preferred_Term")
ecds_df = ecds_df[ecds_df.Flag_ADS == "1"]
ecds_df = ecds_df.drop("Flag_ADS", axis=1)

ecds_df.to_csv("ecds_df.csv")