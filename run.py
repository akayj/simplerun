from simplerun import concurrent_run

bats = ['sleep 3', 'uptime | wc -l', 'sleep 5']

r = concurrent_run(bats)
print(r)
