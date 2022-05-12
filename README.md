# Task (Badger Maps)

A Python script which analyzes' a companies data, and retrieves multiple endpoints:

- The customer with the earliest check-in date.
- The customer with the latest check-in date.
- A list of customer’s full names ordered alphabetically.
- A list of the companies user’s jobs ordered alphabetically.

Testing the run-time speed of the script:

On Windows machines:
```
Measure-Command {start-process python -ArgumentList (".\main.py") -Wait}
```

which in turn returns:
```
Days              : 0
Hours             : 0
Minutes           : 0
Seconds           : 1
Milliseconds      : 20
Ticks             : 10207249
TotalDays         : 1.18139456018519E-05
TotalHours        : 0.000283534694444444
TotalMinutes      : 0.0170120816666667
TotalSeconds      : 1.0207249
TotalMilliseconds : 1020.7249
```

Alternatively, simply running the script will also show the runtime.

```
python main.py
```