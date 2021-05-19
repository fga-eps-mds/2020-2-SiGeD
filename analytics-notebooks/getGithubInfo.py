import requests
from datetime import datetime

class Issue:
  def __init__(self, number, title, labels, sprint):
    self.number=number
    self.title=title
    self.labels=labels
    self.sprint=sprint

def get_issues_by_label(label):
  issues=[]
  page=1
  while True:
    issues_per_page = requests.get('http://api.github.com/repos/fga-eps-mds/2020-2-SiGeD/issues?state=all&per_page=100&page={}&pulls=true&labels={}'.format(page, label))
    
    if issues_per_page.headers['X-RateLimit-Remaining'] == '0':
      timestamp = int(issues_per_page.headers['X-RateLimit-Reset'])
      date_time = datetime.fromtimestamp(timestamp)
      reset = date_time.strftime("%d/%m/%Y, %H:%M:%S")
      print('ATENÇÃO:')
      print('Limite de requisições atingido, espere até {}.'.format(reset))
      break
    
    else:
      for item in issues_per_page.json():
        issue = Issue(item['number'], item['title'], item['labels'], item['milestone'])
        issues.append(issue)
      page+=1
      if len(issues_per_page.json()) == 0:
        break

  print(label + ' ' +  str(len(issues)))
  return issues

def get_issues_by_milestone(milestone):
  issues=[]
  page=1
  while True:
    issues_per_page = requests.get('http://api.github.com/repos/fga-eps-mds/2020-2-SiGeD/issues?state=all&per_page=100&page={}&pulls=true&milestone={}'.format(page, milestone))
    
    if issues_per_page.headers['X-RateLimit-Remaining'] == '0':
      timestamp = int(issues_per_page.headers['X-RateLimit-Reset'])
      date_time = datetime.fromtimestamp(timestamp)
      reset = date_time.strftime("%d/%m/%Y, %H:%M:%S")
      print('ATENÇÃO:')
      print('Limite de requisições atingido, espere até {}.'.format(reset))
      break

    
    else:
      print(issues_per_page.json())
      for item in issues_per_page.json():
        issue = Issue(item['number'], item['title'], item['labels'], item['milestone'])
        issues.append(issue)
      page+=1
      if len(issues_per_page.json()) == 0:
        break

  print(milestone + ' ' +  str(len(issues)))
  return issues

# def separate_issues_in_sprints(issues):
#   sprints = {}

#   for issue in issues:
#     sprint_num = issue.sprint['number']
#     if sprints

if __name__ == '__main__':
  # hard = get_issues_by_label('HARD')
  # medium = get_issues_by_label('MEDIUM')
  # easy = get_issues_by_label('EASY')

  # hotfix = get_issues_by_label('HOTFIX')
  # docs = get_issues_by_label('DOCS')
  # feature = get_issues_by_label('FEATURE')

  # arq = get_issues_by_label('ARQ')
  # devops = get_issues_by_label('DEVOPS')
  # analytics = get_issues_by_label('ANALYTICS')

  # us = get_issues_by_label('US')

  # eps = get_issues_by_label('EPS')
  # mds = get_issues_by_label('MDS')

  for sprint in range(15):
    issues_per_sprint = get_issues_by_milestone(sprint)



#     "HOTFIX": 4,
#     "DOCS": 2,
#     "FEATURE": 3,
#     "ARQ": 2,
#     "DEVOPS": 5,
#     "ANALYTICS": 2,
#     "US": 4,
#     "EASY": 9,
#     "MEDIUM": 1,
#     "HARD": 2,
#     "EPS": 5,
#     "MDS": 7

#     Total: 

#     Issues por sprint