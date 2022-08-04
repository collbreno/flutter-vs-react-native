import os
from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import math
import matplotlib.ticker as mtick

GRAPHS_FOLDER = 'outputs/graphs'

def convert_float_to_string_percentage(p: float) -> str:
    p = 0 if math.isnan(p) else np.round(p*100, 2)
    return f'{p}%'

def count_frames_per_execution(dataframe: pd.DataFrame) -> pd.DataFrame:
    cols = ['framework', 'app', 'execution_id']
    frames = dataframe.groupby(cols).size().to_frame(name='frames').reset_index()
    janky_frames = dataframe[dataframe.frame_time>16].groupby(cols).size().to_frame(name='janky_frames').reset_index()
    merged = frames.merge(janky_frames, how='left').fillna(0)
    merged.janky_frames = merged.janky_frames.astype(int)
    return merged

def plot_janky_percentage(dataframe: pd.DataFrame, app: str):
    app_df = dataframe[dataframe.app==app]
    app_df = count_frames_per_execution(app_df)
    app_df['execution'] = list(range(0, 50)) + list(range(0,50))
    app_df['janky_percentage'] = (app_df['janky_frames'] / app_df['frames'])*100
    ax = sns.lineplot(data=app_df, x='execution', hue='framework', y='janky_percentage')
    ax.set(
        xlabel = 'Execução', 
        ylabel = 'Porcentagem de janky frames',
        title = app
    )
    ax.yaxis.set_major_formatter(mtick.PercentFormatter())
    plt.savefig(f'{GRAPHS_FOLDER}/{app}.png', bbox_inches='tight')
    plt.cla()
    plt.clf()
    
if __name__ == '__main__':
    os.makedirs(GRAPHS_FOLDER, exist_ok=True)
    df = pd.read_csv('dataframe.csv')
    df = df[df.app != 'list_rec']

    for app in df.app.unique():
        sns.set(rc = {'figure.figsize':(15,8)})
        plot_janky_percentage(df, app)