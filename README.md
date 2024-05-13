# Discord_Coin_Bot

# Discord Economy Bot

## Overview

This Discord bot is designed to assign scores (coins) to users based on their interactions in the chat. Users receive coins when they reply with specific keywords in designated channels.

## Functionality

- **Score Assignment**: Users receive a coin when they reply with certain predefined keywords (`!Done`, `!work`, `!fun`) in the designated channels. Each interaction with these keywords earns the user one coin.

- **Leaderboard**: Users can check the leaderboard by sending the command `/list`. The bot displays the users ranked based on the number of coins they have, from the highest to the lowest.

## Setup

1. **Dependencies**: Make sure you have Python installed on your system. Additionally, install the required Python packages using the following command:

   ```
   pip install discord.py DiscordUtils pandas
   ```

2. **Bot Token**: Replace the `""` in the `bot.run("")` line with your Discord bot token.

3. **Data Storage**: The bot uses a JSON file (`Data.json`) to store user data. Ensure the bot has read and write permissions to this file.

4. **Channels**: Update the `channel` variable with the names of the channels where the bot should monitor messages for keywords.

## Usage

1. Invite the bot to your Discord server.

2. Ensure the bot has necessary permissions to read and send messages in the designated channels.

3. Users can start earning coins by replying with the predefined keywords (`!Done`, `!work`, `!fun`) in the specified channels.

4. To check the leaderboard, users can send the command `/list` in any channel where the bot is active.

## Additional Notes

- The bot considers messages only in channels specified in the `channel` variable.
- Each interaction with the keywords earns the user one coin.
- The leaderboard is updated dynamically based on user interactions.

## Support

For any issues or feature requests, please contact [bot developer's name/email/contact].
