from logger import logger


def run():
    with open('2022/01/input.txt', 'r') as f:
        lines = f.read().splitlines()

    calories = []
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
            if len(calories) == 0:
                max_calory = 0
            else:
                max_calory = calories[0]

            logger.info(f"Elf number {elf_number} is carrying {current_calories} which is more than the previous maximum ({max_calory}) ")
            calories.append(current_calories)
            calories = sorted(calories, reverse=True)
                
            current_calories = 0
            elf_number += 1

    logger.info(f"Part one: Elf number {elf_number} is carrying {calories[0]} which is the maximum")
    logger.info(f"Part two: Sum of calories carried by top three elves: {sum(calories[:3])}")
            

if __name__ == "__main__":
    run()
