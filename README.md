# LeetCode Problem Info

Get information of LeetCode problems

## Instructions

1. Install:

```
pip install Leetcode-problem-info
```

2. import
```python
from LeetCode_problem_info import problem_info
```
initialize drive object to get problem data
```python
drive = problem_info.Get_Info()
```
Get problem title using problem ```id```
```python
drive.problem_title(id)
```
##### Get problem details by entering problem id
```python
drive.problem_details(id)
```
Output: ```['Two Sum', '45.20%', 'Easy']```

Get problem ```url``` by entering problem id
```python
drive.problem_url(id)
```
