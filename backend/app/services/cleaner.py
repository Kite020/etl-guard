import pandas as pd
import re


def clean_data(df):

    cleaning_report = {}

    # =========================
    # REMOVE DUPLICATES
    # =========================

    original_rows = len(df)

    df = df.drop_duplicates()

    duplicates_removed = original_rows - len(df)

    # =========================
    # HANDLE MISSING VALUES
    # =========================

    missing_before = int(
        df.isnull().sum().sum()
    )

    # Fill object/string columns
    string_columns = df.select_dtypes(
        include=["object"]
    ).columns

    for col in string_columns:

        df[col] = df[col].fillna(
            "Not Available"
        )

    # Fill numeric columns
    numeric_columns = df.select_dtypes(
        include=["number"]
    ).columns

    for col in numeric_columns:

        median_value = df[col].median()

        df[col] = df[col].fillna(
            median_value
        )

    # =========================
    # STANDARDIZE STRING DATA
    # =========================

    for col in string_columns:

        df[col] = (
            df[col]
            .astype(str)
            .str.strip()
        )

    # =========================
    # FIX NEGATIVE VALUES
    # =========================

    negative_fixed = {}

    ignored_columns = [
        "phone",
        "id",
        "zipcode",
        "zip",
        "transaction"
    ]

    for col in numeric_columns:

        column_name = col.lower()

        # Ignore phone/id style fields
        if any(
            ignored in column_name
            for ignored in ignored_columns
        ):
            continue

        try:

            negative_count = int(
                (df[col] < 0).sum()
            )

            if negative_count > 0:

                negative_fixed[col] = (
                    negative_count
                )

                # Replace negatives with 0
                df.loc[
                    df[col] < 0,
                    col
                ] = 0

        except Exception:
            pass

    # =========================
    # FIX INVALID EMAILS
    # =========================

    email_pattern = (
        r'^[\w\.-]+@[\w\.-]+\.\w+$'
    )

    invalid_email_fixed = 0

    for col in df.columns:

        if "email" in col.lower():

            invalid_mask = df[col].apply(

                lambda x: not bool(
                    re.match(
                        email_pattern,
                        str(x)
                    )
                )
            )

            invalid_count = int(
                invalid_mask.sum()
            )

            invalid_email_fixed += (
                invalid_count
            )

            df.loc[
                invalid_mask,
                col
            ] = "invalid@example.com"

    # =========================
    # CLEANING REPORT
    # =========================

    cleaning_report[
        "duplicates_removed"
    ] = int(duplicates_removed)

    cleaning_report[
        "missing_values_filled"
    ] = int(missing_before)

    cleaning_report[
        "negative_values_fixed"
    ] = negative_fixed

    cleaning_report[
        "invalid_emails_fixed"
    ] = int(invalid_email_fixed)

    return df, cleaning_report