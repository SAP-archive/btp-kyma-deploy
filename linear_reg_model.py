import numpy as np
import pandas as pd
import joblib


class Linear_Reg_Model:
    def __init__(self, model):
        msg = "model load fail"
        try:
            self.model = model
            print("model loaded")
        except:
            print(msg)

    def predict(self, data):
        column_names = ['Units_Sold', 'Unit_Price', 'Unit_Cost',
                        'Total_Revenue', 'Total_Cost']
        inputs = np.asarray(data["instances"])
        df = pd.DataFrame(inputs, columns=column_names)

        results = self.model.predict(df)
        return results
