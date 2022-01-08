# LeetCode Problem Info

Get information of LeetCode problems

## Instructions

1. Install:

```
pip install Leetcode-problem-info
```

2. Generate an aesthetic ASCII visual:

```python
from LeetCode_problem_info import problem_info

# initialize drive object to get problem data
drive = problem_info.Get_Info()
# get problem title by entering problem id
drive.problem_title(id)

# Get problem details by entering problem id
drive.problem_details(id)

# get problem url by entering problem id
drive.problem_url(id)
