
import re
from collections import defaultdict
def get_id(log_line):
    position = re.findall('\[\#tid\_[\d\w]+\]',log_line)
    position = [i for i in position if len(i) > 35]
    if position:
        return position[0]
    else:
        return None

def get_time(log_line):
    position = re.findall('\[\d+\-\d+\-\d+T.+Z\]',log_line)
    if position:
        return position[0]
    else:
        return None

if __name__ == '__main__':
    result = defaultdict(dict)
    with open('test_log.log') as f:
        lines = f.readlines()
        for line in lines:
            # print(get_id(line))
            # print(get_time(line))
            # print()
            map_dict ={'InvokerReactive':'invoker receive request time',
                '/usr/bin/docker run':'container startup start time',
                'invoker_docker.run_finish':'container startup finish time',
                'sending initialization to ContainerId':'function init start time',
                'initialization result':'function init finish time',
                'sending arguments to':'function exec start time',
                'running result':'function exec finish time'}
            
            activation_id = get_id(line)
            time_point = get_time(line)

            if not activation_id or not time_point:
                continue
            
            for k,v in map_dict.items():
                if k in line:
                    result[activation_id][v] = time_point
                    break 
    for i in result:
        print(i)
        print(result[i])
        print()
