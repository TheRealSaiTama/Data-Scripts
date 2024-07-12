import sys
import pandas as pd 

def fill_missing_data(csv_file):
    try: 
        df = pd.read_csv(csv_file)

        if not df.isnull().values.any():
            print("No missing data found.")
            return
        
        df = df.interpolate(method='linear', limit_direction='both')
        df.to_csv('interpolated_'+ csv_file, index=False)

        print("Missing data filled successfully.")

    except Exception as e:
        print("An error occurred: ", e)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python interpolatedata.py <csv_file>")
        sys.exit(1)
    else:
        fill_missing_data(sys.argv[1])

