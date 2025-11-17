from pathlib import Path

def total_salary(path):
    file_path = Path(path)

    if not file_path.exists():
       print(f'File by path  "{path}" not found.')
       return 0, 0
    
    total = 0
    count = 0

    try:
        with file_path.open("r", encoding= "utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                try: 
                    name, salary = line.split(",")
                    salary = float(salary)
                    total += salary
                    count += 1
                except ValueError:
                    print(f"String processing error: {line}")

        if count ==0:
            return 0, 0

        average = total / count
        return total, average

    except Exception as e:           
        print(f"An error occurred: {e}")
        return 0, 0
    
total, average = total_salary("salary_file.py")
print(f"Total salary: {total}, average salary: {average}")



from pathlib import Path

def get_cats_info(path):
    file_path = Path(path)


    if not file_path.exists():
        print(f"file '{path}' not found.")
        return[]
    
    cats = []

    try:
        with file_path.open("r", encoding= "utf-8") as file:
            for line in file:
                line = line.strip
                if not line:
                    continue
                try:
                    cat_id, name, age = line.split(",")
                    cat_dict = {
                        "id": cat_id,
                        "name": name,
                        "age": age
                }
                    cats.append(cat_dict)
                except ValueError:
                    print(f"Error processing line: {line}")
                    continue
        return  cats

    except Exception as e:
        print(f"An error occured while reading the file:{e}")
        return[]
    

cats_info = get_cats_info("kiot.py")
print(cats_info)
