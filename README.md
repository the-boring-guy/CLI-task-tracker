# CLI Task Tracker
A simple command-line interface task tracker that allows users to manage tasks via add, remove, update, filter and list operations.
## Features
- Add tasks with name and description
- Remove tasks with task id
- Update task status or particulars
- List all tasks
- Filter tasks by status
---
## Tech Stack
- Python 3 (no external libraries)
- JSON (for storage)
---
## Project Structure
- main.py -> CLI interface and user input handling
- utils.py -> Helper functions
- storage.py -> Task storage and data persistence logic
- storage.json -> Persistent task data
- task.py -> Task class(reserved for future use)
---
## How to Run
1. Clone the project repository on your device by running the following command inside your terminal
```bash
git clone https://github.com/the-boring-guy/CLI-task-tracker.git
```
2. Navigate to the project directory
```bash
cd CLI-task-tracker
```
3. Run the program

For macOS:
```bash
python3 main.py
```
For windows:
```bash
py main.py
```
---
## Future Improvements
- Add task priorities
- Add deadline to tasks
---
Thank you!
