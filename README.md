# Microsoft Certification Exam Parser

> This is my first Python program. The code might not be the best.

Outputs the topics of a Microsoft certification exam into a JSON file. (The `Skills measured` section in the exam's webpage)

[List of all Microsoft Certification Exams](https://www.microsoft.com/en-us/learning/exam-list.aspx)

## Output

> Excerpt from the output for the [Python exam](https://www.microsoft.com/en-us/learning/exam-98-381.aspx):

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
main.py 98-381
main.py 70-483 98-361
```

Clearing the cache: (deletes the `out/` directory)

```shell
main.py --clear
```
