import pandas as pd
import numpy as np
import Tkinter as tk
import csv

class Leaderboard:

    df = pd.read_csv('leaderboard.csv')
    #sort the the leaderboard csv and get the smallest value
    smallest_value = np.sort(df['Score'].unique())[:1]

    def add_value(self, df,  username, highscore):
        df2 = pd.DataFrame({'Username': [username], 'Score': [highscore]})
        return df2

    def sort_values(self, df):
        df = df.sort_values(by='Score', ascending=False)
        df = df.reset_index(drop=True)
        return df

    def updated_leaderboard(self, df,username, highscore):
        df2 = self.add_value(df, username, highscore) #creates a new leaderboard with the new username and score
        sorted_values = self.df.sort_values(by='Score', ascending=False).head(25) #Resorts the main table
        b = pd.concat([sorted_values, df2])  #merges the two leaderboards together
        b = b[['Username', 'Score']] #Puts the columns in the correct order
        b = self.sort_values(b) #Sorts the leaderboard with the new value
        b.to_csv('leaderboard.csv') #updates the CSV file with the new leaderboard

	#display function utilised code from https://stackoverflow.com/questions/42748343/how-to-show-csv-file-in-a-grid/42748973
    def leader_board(self):
            root = tk.Tk()
            # open file
            with open("leaderboard.csv") as file:
                reader = csv.reader(file)
                # r and c tell us where to grid the labels
                r = 0
                for col in reader:
                    c = 0
                    for row in col:
                        # styling
                        label = tk.Label(root, width=12, height=2, \
                                              text=row, relief=tk.RIDGE)
                        label.grid(row=r, column=c)
                        c += 1
                    r += 1

            root.mainloop()
