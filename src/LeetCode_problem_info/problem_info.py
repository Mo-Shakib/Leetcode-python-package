class Get_Info:
    def __init__(self):
        problem_file = open('src/LeetCode_problem_info/all-questions.txt','r')
        self.problem_data = {}
        for line in problem_file:
            line = line.strip()
            line = line.split(',')
            self.problem_data[int(line[0])] = line[1:]
        problem_file.close()
    
    def problem_title(self, problem_id):
        return self.problem_data[problem_id][0]
    
    def problem_details(self, problem_id):
        return self.problem_data[problem_id]

    def problem_url(self, problem_id):
        title = self.problem_data[problem_id][0]
        title = title.replace(' ','-')
        title = title.lower()
        url = 'https://leetcode.com/problems/' + title
        return url
