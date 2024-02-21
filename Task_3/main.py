import sys
from collections import Counter
from  pathlib import Path

def parse_log_line(line: str) -> dict:
    date, time, level, message = line.split(" ", 3)
    return {"date": date, "time": time,  "level": level, "message": message}
   
def load_logs(file_path: str) -> list:
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()
            return [parse_log_line(line.strip()) for line in lines]
    except Exception:
        print(f"The file is not found or its contents are corrupted")    
        
def filter_logs_by_level(logs: list, level: str) -> list:
    return list(filter(lambda log: log["level"].lower() == level.lower() , logs))    
             
def count_logs_by_level(logs: list) -> dict:
    return dict(Counter(log["level"] for log in logs ))

def display_log_counts(counts: dict): 
    print("-----------------------")
    print("Level log    |  Count")
    print("-------------|---------")
    for keys, value in counts.items():
        print (f"{keys:12} | {value:4}")
      

def main():
    if len(sys.argv) == 1:
        print('Usage: python main.py <directory_path>')
        sys.exit(1)
    path = Path(sys.argv[1])
    log_list = load_logs(path)
    dict_count= count_logs_by_level(log_list)
    display_log_counts(dict_count)
    print()
    if len(sys.argv) == 3:
        filtered_list = filter_logs_by_level(log_list, sys.argv[2])
        print(f"Details of the logs for the type {sys.argv[2]}:\n" \
        + "".join(map(lambda el: f"{el["date"]} {el["time"]} - {el["message"]}\n", filtered_list)))
    
    
if __name__ == "__main__":  
    main()
    
    
    
    
    
    
    
 
    