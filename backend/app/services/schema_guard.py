def normalize_dtype(dtype):

    dtype = str(dtype).lower()

    if dtype in ["object", "str", "string"]:
        return "string"

    if dtype in ["int64", "int32", "int"]:
        return "integer"

    if dtype in ["float64", "float32", "float"]:
        return "float"

    return dtype


def detect_schema_drift(df, expected_schema):

    current_schema = {}

    for column in df.columns:

        current_schema[column] = normalize_dtype(
            df[column].dtype
        )

    normalized_expected_schema = {}

    for column, dtype in expected_schema.items():

        normalized_expected_schema[column] = (
            normalize_dtype(dtype)
        )

    missing_columns = []

    extra_columns = []

    datatype_changes = {}

    # CHECK MISSING COLUMNS
    for column in normalized_expected_schema:

        if column not in current_schema:

            missing_columns.append(column)

    # CHECK EXTRA COLUMNS
    for column in current_schema:

        if column not in normalized_expected_schema:

            extra_columns.append(column)

    # CHECK DATATYPE CHANGES
    for column in normalized_expected_schema:

        if column in current_schema:

            expected_type = (
                normalized_expected_schema[column]
            )

            current_type = current_schema[column]

            if expected_type != current_type:

                datatype_changes[column] = {

                    "expected": expected_type,

                    "received": current_type
                }

    return {

        "missing_columns": missing_columns,

        "extra_columns": extra_columns,

        "datatype_changes": datatype_changes
    }