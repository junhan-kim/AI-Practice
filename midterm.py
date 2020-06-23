
# 제약사항
# MSA 적용 x, 특정 사이트 내의 디렉토리간 이동만 가능
# 그 밖에 실제 구현은 문자열 파싱과 관련된 수많은 예외사항에 대해서는 적용하진 못했고
# 실제 어플리케이션으로서의 완성도는 매우 낮으며
# 그냥 알고리즘을 기반으로 구현에 목적을 둠

# 테스트 케이스(제약사항을 충족하는)
# https://stackoverflow.com  https://stackoverflow.com/teams/use-cases
# https://github.com         https://github.com/collections/pixel-art-tools  
# https://stackexchange.com  https://stackexchange.com/about/security


# 주석 달고, ipynb로 바꾸기



import argparse
import sys
from bs4 import BeautifulSoup
import requests
import requests.exceptions
from urllib.parse import urlsplit
from urllib.parse import urlparse
from collections import deque
from heapq import heappush, heappop
from queue import PriorityQueue
from difflib import SequenceMatcher


parser = argparse.ArgumentParser(
    description="python midterm.py https://github.com https://github.com/collections/pixel-art-tools",
)

# src must be parent website of dest, but no matter during tracing
parser.add_argument("src", help="source webpage")
parser.add_argument("dest", help="destination webpage on the same website")

args = parser.parse_args()

src = args.src
dest = args.dest

protocols = (
    "https://",
    "http://"
)

top_level_domains = (
    ".com",
    ".org",
    ".net",
    ".edu",
    ".gov",
)


# Check if valid top level domain
for domain in top_level_domains:
    if not src.find(domain) == -1:
        is_src_valid = 1
        src_top_level_domain = domain
        if not dest.find(domain) == -1:
            is_dest_valid = 1
            dest_top_level_domain = domain
        else:
            is_dest_valid = 0
        break
    else:
        is_src_valid = 0
        
# Check if valid protocol
for protocol in protocols:
    if not src.find(protocol) == -1:
        is_src_valid = 1
        src_protocol = protocol
        if not dest.find(protocol) == -1:
            is_dest_valid = 1
            dest_protocol = protocol
        else:
            is_dest_valid = 0
        break
    else:
        is_src_valid = 0

# Get src and dest domain
src_split = src.split('.', 3)
if src_split[1] == src_top_level_domain.split('.')[1]:
    domain = src_split[0].split(src_protocol, 1)[1]
    subdomain = ''
elif src_split[2] == src_top_level_domain.split('.')[1]:
    domain = src_split[1]
    subdomain = src_split[0]


print('domain : ' + domain)
print('src_top_level_domain : ' + src_top_level_domain + '\n')
print('src : ' + src)
print('dest : ' + dest)
print('==================================')

def get_heuristic(local_url):
  #local_val = len(local_url.split('/'))
  #dest_val = len(dest.split('/'))
  string_match_ratio = SequenceMatcher(None, local_url, dest).ratio()
  return (1 - string_match_ratio)

def get_neighbor(cur):
  response = requests.get(cur)
  soup = BeautifulSoup(response.text, "lxml")
  ret = []
  for link in soup.find_all('a'):
    anchor = link.attrs["href"] if "href" in link.attrs else ''
    if ((protocols[0] in anchor) or (protocols[1] in anchor)):  # prefix with http or https
      if (((anchor.split('/'))[2]).split('.')[0] == domain): # ignoring for MSA
        ret.append(anchor)
    else:
      ret.append(src + anchor)
  return ret

def greedy_search(start, goal):
  fringe = PriorityQueue() 
  fringe.put((0, start))
  came_from = {} 
  came_from[start] = None
  
  while not fringe.empty():
    current = fringe.get()[1]
    if current == goal:
      break
    print('cur : ' + current) 
    print('==================================')
    for next in get_neighbor(current):
      if next not in came_from:
        print('next : ' + next)
        priority = get_heuristic(next)
        print('heuristic value : ' + str(get_heuristic(next)))
        fringe.put((priority, next))
        came_from[next] = current
    print('\n')
  return came_from

came_from = greedy_search(src, dest)
print('Reached the goal')
print('\n')
print('=== Website stack trace ===')
cur = dest
while not (cur == None):
  print(cur)
  cur = came_from[cur]
