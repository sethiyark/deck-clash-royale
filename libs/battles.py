# Function to get battle logs go here
import json

from config import DB


def refine_battle_log():
    refined_logs = set()
    count = 0
    logs = DB.find('battle_log', {}, {'_id': 0})
    for l in logs:
        refined_logs.add(json.dumps(l))
        count += 1
        print(count, end=", ")
    print("Dumping to db")
    for battle in refined_logs:
        DB.insert('refined_battle_log', json.loads(battle))
        count -= 1
        print(count, end=', ')


if __name__ == '__main__':
    refine_battle_log()
