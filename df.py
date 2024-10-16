def move_column(df, column_name, col_index):
    """
    Move a specified column to a new column index in a DataFrame.

    Parameters:
    df (pd.DataFrame): The input DataFrame.
    column_name (str): The name of the column to move.
    col_index (int): The new index position for the column.

    Returns:
    pd.DataFrame: The DataFrame with the column moved to the new position.
    """
    cols = list(df.columns)
    cols.remove(column_name)
    cols.insert(col_index, column_name)
    return df[cols]
