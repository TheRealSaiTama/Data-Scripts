# Data Scripts

This repository contains a collection of scripts designed to make data handling and visualization easier. These scripts provide various utilities to process, clean, manipulate, and visualize data efficiently.

## Scripts

### 1. interpolatedata.py

This script fills missing data in a CSV file using linear interpolation.

#### Usage

```
python interpolatedata.py <csv_file>
```

#### Features

- Reads a CSV file
- Checks for missing data
- Fills missing data using linear interpolation
- Saves the interpolated data to a new CSV file with the prefix 'interpolated_'

#### Dependencies

- pandas

#### How it works

1. The script reads the specified CSV file using pandas.
2. It checks if there's any missing data in the file.
3. If missing data is found, it uses linear interpolation to fill the gaps.
4. The interpolated data is then saved to a new CSV file with the prefix 'interpolated_'.

#### Example

```
python interpolatedata.py mydata.csv
```

This will create a new file named `interpolated_mydata.csv` with all missing data filled.

### 2. barscript.py

This script creates bar charts from CSV data and saves them as image files.

#### Usage

```
python barscript.py <csv_file> <kind_of_bar> <output_file>
```

#### Features

- Reads data from a CSV file
- Creates various types of bar charts
- Saves the chart as an image file

#### Dependencies

- pandas
- matplotlib (implicitly used by pandas for plotting)

#### How it works

1. The script reads the specified CSV file using pandas.
2. It creates a bar chart based on the data and the specified chart type.
3. The resulting chart is saved as an image file.

#### Example

```
python barscript.py sales_data.csv bar sales_chart.png
```

This will create a bar chart from `sales_data.csv` and save it as `sales_chart.png`.

## Contributing

Feel free to contribute to this repository by adding more data handling or visualization scripts, or by improving existing ones. Please ensure that you provide clear documentation for any scripts you add.

## License

[MIT License](LICENSE)
