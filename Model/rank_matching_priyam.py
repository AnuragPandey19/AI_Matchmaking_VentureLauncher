import pandas as pd

def get_top_5_investors_for_startup(prediction_df, startup_name):
    """
    Returns the top 5 investor matches for a given startup, sorted by prediction score.

    Parameters:
        prediction_df (pd.DataFrame): DataFrame with columns ['startup_name', 'investor_name', 'prediction_score']
        startup_name (str): Name or ID of the startup

    Returns:
        pd.DataFrame: Top 5 investors for the startup
    """
    filtered = prediction_df[prediction_df['startup_name'] == startup_name]
    
    if filtered.empty:
        print(f"No prediction data found for startup: {startup_name}")
        return pd.DataFrame()

    top_5 = (
        filtered.sort_values(by='prediction_score', ascending=False)
        .head(5)
        .reset_index(drop=True)
    )
    return top_5
