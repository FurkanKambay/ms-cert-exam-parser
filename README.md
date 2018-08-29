# MS Certification Exam Parser

This is the first Python program I wrote, I learned the language while working on this. My next target is F#.

Outputs the topics of a Microsoft certification exam into a JSON file. ("Skills measured" section in the exam's webpage)

[List of all Microsoft Certification Exams](https://www.microsoft.com/en-us/learning/exam-list.aspx)

Example output for the [Python exam](https://www.microsoft.com/en-us/learning/exam-98-381.aspx):

```jsonc
[
    {
        "label": "Perform Operations using Data Types and Operators (20-25%)",
        "skills": [
            {
                "label": "Perform data and data type operations",
                "items": [
                    "Convert from one data type to another type",
                    "Construct data structures",
                    "Perform indexing and slicing operations"
                ]
            },
            // other skills
        ]
    },
    // other syllabuses
]
```

## Usage

```shell
main.py 98-381 98-361
```

Clearing the cache:

```shell
main.py --clear
```
