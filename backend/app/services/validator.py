import pandas as pd
import re


def validate_data(df):

    validation_report = {}

    # NULL VALUE CHECK
    null_values = df.isnull().sum()
    validation_report["null_values"] = (
        null_values[null_values > 0].to_dict()
    )

    # DUPLICATE CHECK
    duplicates = df.duplicated().sum()
    validation_report["duplicates"] = int(duplicates)

    # NEGATIVE VALUE CHECK
    negative_columns = {}

    numeric_columns = df.select_dtypes(include=['number']).columns

    ignored_columns = [
        "phone",
        "id",
        "zipcode",
        "zip"
    ]

    for col in numeric_columns:

        column_name = col.lower()

        if any(
            ignored in column_name
            for ignored in ignored_columns
        ):
            continue

        try:

            negative_count = (df[col] < 0).sum()

            if negative_count > 0:

                negative_columns[col] = int(
                    negative_count
                )

        except Exception:
            pass
    
    validation_report["negative_values"] = negative_columns

    # INVALID EMAIL CHECK
    invalid_emails = 0

    email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    for col in df.columns:

        if "email" in col.lower():

            invalid_emails += df[col].apply(
                lambda x: not bool(
                    re.match(email_pattern, str(x))
                ) if pd.notnull(x) else False
            ).sum()

    validation_report["invalid_emails"] = int(invalid_emails)

    return validation_report