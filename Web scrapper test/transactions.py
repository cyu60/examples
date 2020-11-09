import useAPI
import clean_transactions
from matplot import plot_histogram

class Transactions():

    def __init__(self):
        self.transactions_data = []
        self.fig = None

    def is_empty(self):
        return len(self.transactions_data) == 0

    def update_transactions(self, form):
        threshold_value = form.threshold_value.data
        time_ago = form.time_ago.data
        start_block = useAPI.get_start_block(
            time_ago, 0)  # haven't incoperated mins yet
        df = useAPI.get_transfer_events(start_block, threshold_value)
        display_df = clean_transactions.display_df(df)
        self.transactions_data.clear()
        self.transactions_data.extend(display_df.to_dict('records'))

        # return matplot fig
        if not self.is_empty():
            self.fig = plot_histogram(df)
            # print("fig is created")
