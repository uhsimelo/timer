# Timer
This repository is for control and organization of work time.

### Fast info
Those scripts are for helping in a particular way to the team workers and the money giver as its explained below:

-------------------------
## Requirements
1. python3. * must be installed 
2. Linux system

# Instructions

### For Workers
In case of the workers to use have to run **w-run.sh** in console whitout parameters, as shown below:
```bash
./w-run.sh
```
After that enter your name, that will be you future identifier to store your time, and press the button `start` you just have to follow the instructions to stop it or close it.

The times are stored in `times\<user-name>.json` and their structure is the next one:
```json
{
    "-8856090179422580289": {               // datetime.__hash__()
        "datetime": "14 Feb 2018, 02:31:49",// start time
        "elapsed": "2:13:2"                 // time elapsed HH:MM:SS
    },
    "-2040455496698083750": {
        "datetime": "14 Feb 2018, 06:57:32",
        "elapsed": "0:50"
    },
    //...
}
```
About the implementation, for every time you pause it to continue later or stop it the time elapsed will be stored if and only if your time elapsed exceeds the minute.
### For Money-givers
To know the times and payments you have to run **price.py** as follows:
```bash
python price.py <per-hour> ["user-name"]
```
- **per-hour**: payment per hour.
- **user-name**: an specific user-name or it can be omitted to calculate it to everyone in the `\times` folder.

### To the next version:
Another script `plot_time.py` also can show the performance of workers ,located in the times folder, on a graph. And is used as follows, without arguments:
```bash
python plot_time.py
```
