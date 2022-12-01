from logger import logger


def run():
    with open('2022/01/input.txt', 'r') as f:
        lines = f.read().splitlines()

    max_calories = 0
    current_calories = 0
    elf_number = 1
    for line in lines:
        
        if line:
            try:
                calory = int(line)
                current_calories += calory
            except ValueError:
                logger.exception("Cannot get calories from line")
        else:
            if current_calories > max_calories:
                logger.info(f"Elf number {elf_number} is carrying {current_calories} which is more than the previous maximum ({max_calories}) ")
                max_calories = current_calories
                
            current_calories = 0
            elf_number += 1

    logger.info(f"Elf number {elf_number} is carrying {max_calories} which is the maximum")
            

if __name__ == "__main__":
    run()
