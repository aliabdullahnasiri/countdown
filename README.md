# Countdown Timer Script

This Python script provides a simple and customizable countdown timer. It allows users to set the initial duration in hours, minutes, and seconds, and then displays a real-time countdown in the terminal. The timer visually differentiates between hours, minutes, and seconds, making it easy to track the remaining time.

## Features

- **User-friendly Command-Line Interface:** Easily set the initial duration using command-line options.
- **Customizable Duration:** Set the countdown duration in hours, minutes, and seconds.
- **Visual Differentiation:** The timer visually distinguishes between hours, minutes, and seconds for better readability.
- **Clear Screen Display:** Enhances the user experience with a clear screen after each second.

## Usage
  ```bash
  python countdown_timer.py --hours 1 --minutes 30 --seconds 0
  ```
This will start a countdown timer for 1 hour, 30 minutes, and 0 seconds.

## Installation
- Clone the repository:

  ```bash
  git clone https://github.com/aliabdullahnasiri/countdown.git
  ```
  
- Navigate to the project directory:

  ```bash
  cd countdown 
  ```

- Run the script:

  ```bash
  python countdown.py
  ```

## Options
- `--hours` : Set the initial hours for the countdown (default is 0).
- `--minutes` : Set the initial minutes for the countdown (default is 0).
- `--seconds` : Set the initial seconds for the countdown (default is 30).

## Dependencies
- Python 3
- Click
- Rich

##  License
This project is licensed under the MIT License - see the LICENSE file for details.
