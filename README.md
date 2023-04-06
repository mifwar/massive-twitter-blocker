# massive-twitter-blocker

## Description

A Python script that automates blocking multiple Twitter users at once

## Dependencies

- Python 3.6+
- Selenium

## Installation

1. Clone this repository: `git clone https://github.com/mifwar/massive-twitter-blocker.git`
2. Install the dependencies: `pip install -r requirements.txt`

## Usage

1. Clone this repository to your local machine using `git clone https://github.com/mifwar/massive-twitter-blocker.git`.
2. Modify the `personal.txt` file and fill it with your Twitter username and password, separated by a new line.
3. Modify the `accounts.txt` file and add the Twitter usernames of the users you want to block, one per line.
4. Open a terminal window and navigate to the root directory of the project.
5. Run the script using the command: `python main.py`
6. Watch as the script navigates to each user's profile, blocks them, and moves on to the next user.

Note: If a user is already blocked, the script will skip them and move on to the next user.

## Contributing

1. Fork it (https://github.com/mifwar/massive-twitter-blocker/fork)
2. Create your feature branch (`git checkout -b feature/your-feature-name`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature-name`)
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
