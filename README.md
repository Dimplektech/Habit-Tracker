# Pixela Habit Tracker

This Python script interacts with the [Pixela API](https://docs.pixe.la/) to track daily coding habits by creating a graph and posting data (e.g., minutes spent coding). The user can log, update, or delete coding activity for any given day.

## Features
- **Create a User Account** (account creation is commented out, assuming it's already done).
- **Create a Graph** to track your coding habit in minutes.
- **Log Daily Coding Time** by posting the time spent coding.
- **Update Logged Time** for a specific date.
- **Delete Logged Time** for a specific date.

## Requirements

- Python 3.x
- `requests` library (`pip install requests`)
- Pixela account (with token and username)
- Environment variables to store sensitive information

## Installation

1. Clone the repository or download the script.

```bash
git clone https://github.com/Dimplektech/Habit-Tracker.git
cd pixela-habit-tracker
```

2. Install the required Python packages:

```bash
pip install requests
```

## Environment Variables

This script requires two environment variables to be set:

- `APP_USERNAME`: Your Pixela username.
- `APP_TOKEN`: Your Pixela API token.

### Setting Up Environment Variables

1. On **Linux/macOS**, you can set environment variables by adding the following lines to your `.bashrc`, `.bash_profile`, or `.zshrc` file:

    ```bash
    export APP_USERNAME="your_pixela_username"
    export APP_TOKEN="your_pixela_token"
    ```

   After adding these lines, run the following command to apply the changes:

    ```bash
    source ~/.bashrc  # or ~/.bash_profile or ~/.zshrc depending on your shell
    ```

2. On **Windows**:

    You can set environment variables through the System Properties. Follow these steps:
    - Go to **Control Panel > System and Security > System > Advanced system settings**.
    - Click **Environment Variables**.
    - Under **User variables**, click **New** and add `APP_USERNAME` with your Pixela username and `APP_TOKEN` with your API token.

    Alternatively, you can use the command prompt:

    ```bash
    setx APP_USERNAME "your_pixela_username"
    setx APP_TOKEN "your_pixela_token"
    ```

## Usage

Once the environment variables are set, you can run the script to track your coding habit.

```bash
python pixela_habit_tracker.py
```

### Key Steps in the Program:

1. **Create a Graph** (Step is commented out, but you can uncomment it to create a new graph).
   The graph tracks coding time in minutes. You can access your graph via a URL like:
   ```bash
   https://pixe.la/v1/users/<your_username>/graphs/graph1
   ```

2. **Post a Value**: Log your daily coding time by running the script. It will prompt you to enter the number of minutes spent coding.

3. **Update a Value** (Optional): You can update the value for any specific date by uncommenting the `PUT` request section in the script.

4. **Delete a Value** (Optional): You can delete a value for any specific date by uncommenting the `DELETE` request section in the script.

### Example URLs:

- **Access Your Graph**: 
  `https://pixe.la/v1/users/<your_username>/graphs/<graph_id>`

- **Post to Graph**: 
  `https://pixe.la/v1/users/<your_username>/graphs/<graph_id>`

## Script Overview

```python
# Step 1: Create a user account (commented out)
# Step 2: Create a graph to track coding time
# Step 3: Post daily coding time
# Step 4: Update a logged value for a specific day (optional)
# Step 5: Delete a value for a specific day (optional)
```

## Example Output

When you run the script and input the number of minutes spent coding:

```bash
How Long did you do coding today? (Enter in Minutes): 120
{"message":"Success.","isSuccess":true}
```

## Contributing

Feel free to fork this repository and submit pull requests to enhance or improve the code. All contributions are welcome!

## License

This project is licensed under the MIT License.


