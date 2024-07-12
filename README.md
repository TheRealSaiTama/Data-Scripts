# Data Scripts

This repository contains a collection of scripts designed to make data handling easier. These scripts provide various utilities to process, clean, and manipulate data efficiently.

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

## Contributing

Feel free to contribute to this repository by adding more data handling scripts or improving existing ones. Please ensure that you provide clear documentation for any scripts you add.

## License

[GNU License](LICENSE)
