import requests
from datetime import datetime

class Issue:
  def __init__(self, number, title, labels, sprint):
    self.number=number
    self.title=title
    self.labels=labels
    self.sprint=sprint

def get_issues_by_label_and_milestone(label, milestone):
  issues=[]
  page=1
  while True:
    issues_per_page = requests.get('http://api.github.com/repos/fga-eps-mds/2020-2-SiGeD/issues?state=all&per_page=100&page={}&pulls=true&labels={}&milestone={}'.format(page, label, milestone))
    
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

  print(str(milestone) + ' ' + label + ' ' +  str(len(issues)))
  return issues


# def separate_issues_in_sprints(issues):
#   sprints = {}

#   for issue in issues:
#     sprint_num = issue.sprint['number']
#     if sprints

if __name__ == '__main__':

  for sprint in range(1,15):
    hard = get_issues_by_label_and_milestone('HARD', sprint)
    medium = get_issues_by_label_and_milestone('MEDIUM', sprint)
    easy = get_issues_by_label_and_milestone('EASY', sprint)

    hotfix = get_issues_by_label_and_milestone('HOTFIX', sprint )
    docs = get_issues_by_label_and_milestone('DOCS', sprint )
    feature = get_issues_by_label_and_milestone('FEATURE', sprint )

    arq = get_issues_by_label_and_milestone('ARQ', sprint )
    devops = get_issues_by_label_and_milestone('DEVOPS', sprint )
    analytics = get_issues_by_label_and_milestone('ANALYTICS', sprint )

    us = get_issues_by_label_and_milestone('US', sprint )

    eps = get_issues_by_label_and_milestone('EPS', sprint )
    mds = get_issues_by_label_and_milestone('MDS', sprint )


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