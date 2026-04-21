# Schedule Lynx Assistant Help Page

Welcome to the Schedule Lynx Assistant Help page!

## What Is This Tool?

This tool creates `person.json` files. A `person.json` file is a simple file that contains one person's weekly schedule. You can create a `person.json` file with this tool, download it, and text it to your friends. Then, you or your friends can upload up to 12 `person.json` files at a time to the [Schedule Lynx App](https://schedule-lynx.streamlit.app/), which will generate a side-by-side schedule containing the weekly availability of you and all your friends!

## How To Use This Tool


To use this tool, perform the following steps. Perform numbered steps in the order listed, and bulleted steps in any order within their context.

1. Write your name in the "Name" field. This name will be displayed on all schedules generated using this `person.json` file.

2. Edit the "Entries" field either by typing in it or by pressing the +/- buttons. The number of entries is the number of unique time-blocked schedule elements that you can add. 1 entry corresponds to 1 weekly event.

3. Fill in your entries. To do this:
    - Enter the start time of the event you are recording. These times are to the nearest 15 minutes, and are :warning: **<u>expressed in army time</u>** :warning:. That is, "1:00" is 1 AM, and "13:00" is 1 PM. PLEASE take note of this! 
    - Enter the end time of the event.
    - Select the days of the week on which the event occurs. 

For example, if I have a class which occurs on Mondays and Wednesdays from 11:00 AM to 3:00 PM, I would write:

![image](https://raw.githubusercontent.com/PurpleRabbit75/Schedule-Lynx-Assistant/refs/heads/main/extras/input_example.png)


## Common Issues

### My Event Isn't There!

There are two common causes of this.

1. The event was accidentally scheduled in AM/PM rather than army time. This is a _very common issue!_ You can double check by opening your `person.json` file. If you see a time entry that looks like `(4, 0)` for an event that's supposed to be at 4 PM, then you've found your issue!

2. The event entry didn't save. To fix this, you can either open your `person.json` file in a text editor and add your event manually (being careful to follow the [`person.json` specification](https://github.com/PurpleRabbit75/person.json/blob/main/SPECIFICATION.md)!) or you can re-enter your events in the app. (HINT: you can use the "preview" feature to make sure that all your events saved in the file before you close the browser window!)


### How do I open a `person.json` file?

Many, many apps can open `person.json` files, since they follow a widely used format. Here are a few:

- Notepad, Notepad++, TextEdit, BBEdit, and similar text editors
- Microsoft Word, Microsoft Excel
- Firefox, MS Edge, Chrome, Safari, Brave, and all other modern browsers
- VS Code, and all modern IDEs
- Vim, Nano, Emacs, and if all else fails, `cat`

If you don't have any of these, try double-clicking on the file and seeing how your OS suggests you open it. `.json` files are really just specially formatted text, and opening it with an unsupported editor won't do it any harm.

All of the above editors will display the "raw text" of the `person.json` file. The real use of `person.json` files, though, is to convert them into schedules that line up with the schedules of your friends! You can do this using [schedule-lynx.streamlit.app](https://schedule-lynx.streamlit.app) :)

### How can I create an event which doesn't start or stop on a 15-minute block?

You can edit your downloaded `person.json` file using any text editor. See the [specification](https://github.com/PurpleRabbit75/person.json/blob/main/SPECIFICATION.md) for how to do this without breaking the format of your file.
