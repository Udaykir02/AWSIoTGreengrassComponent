# Setting Up for CSV Files in Thermostat Simulation

To set up the Thermostat Simulation to work with CSV files, follow these steps:

1. **Create a Directory:**

    Create a directory with a suitable name where you'll store your CSV files. For example, you can create a directory named "csv_data".

2. **Rename File Path in Thermostat Simulation Python File:**

    Open the Python file for the Thermostat Simulation (likely named something like "thermostat_simulation.py") in a text editor or an IDE.

    Find the part of the code where the file path for CSV input/output is specified. It might look something like this:

    ```python
    file_path = "/path/to/csv/file.csv"
    ```

    Update the file path to point to the directory you created in step 1. For example:

    ```python
    file_path = "/path/to/csv_data/file.csv"
    ```

    Ensure that you replace "/path/to/csv_data/" with the actual path to the directory you created.

3. **Save Changes:**

    Save the changes made to the Python file.

4. **Prepare CSV Files:**

    Now, you can prepare your CSV files and place them in the directory you created. Make sure the format of the CSV files matches the expected input/output format of the Thermostat Simulation.

5. **Run the Simulation:**

    Finally, run the Thermostat Simulation Python script. It should now write to the CSV files located in the directory you specified.

By following these steps, you'll have set up the Thermostat Simulation to work with CSV files.
