from base import Visualizer
from typing import List, Optional, Union
from plotly.subplots import make_subplots

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


class NumericalVisualizer(Visualizer):
   """A visualization automator specializing in 
   numerical variables.
   """
   df: Optional[pd.DataFrame]
   categorical: List[str]
   ordinal: List[str]
   numerical: List[str]

   def __init__(self) -> None:
      """Initialize the dataset and classify the columns
      based on their data types.
      """
      super().__init__()

   def create_summary_table(self, cols: Union[str, List[str]]) -> pd.DataFrame:
      pass

   def get_visualizations(self, *args) -> Optional[go.Figure]:
      pass