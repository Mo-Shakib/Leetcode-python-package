# LeetCode Problem Info

Get information of LeetCode problems

## Instructions

1. Install:

```
pip install Leetcode-problem-info
```

2. Get details of a problem

```python
from LeetCode_problem_info import problem_info

# initialize drive object to get problem data
drive = problem_info.Get_Info()
# get problem title by entering problem id
drive.problem_title(id)

# Get problem details by entering problem id
drive.problem_details(id)
# this methord will return three property as a list data
# Example: ['Two Sum', '45.20%', 'Easy']

# get problem url by entering problem id
drive.problem_url(id)
```