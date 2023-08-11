import pandas as pd

def check_dataset_relevance(df, keyword):
    """_summary_

    Args:
        df (_type_): _description_
        keyword (_type_): _description_
    """
       
    # Check if the keyword is present in any column of the DataFrame
    keyword_found = any(df.apply(lambda row: keyword in str(row), axis=1))
    
    if keyword_found:
        print(f"The dataset is relevant. It contains the keyword '{keyword}'.")
    else:
        print(f"The dataset is not relevant. It does not contain the keyword '{keyword}'.")

