"""Saitama"""

from math import ceil

req_push = int(input())
req_sit = int(input())
req_luk = int(input())
req_run = int(input())
day_push = int(input())
day_sit = int(input())
day_run = int(input())
day_luk = int(input())

push = ceil(req_push / day_push)
sit = ceil(req_sit / day_sit)
luk = ceil(req_luk / day_luk)
run = ceil(req_run / day_run)

print(max(push, sit, luk, run))
