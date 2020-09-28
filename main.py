from Miner import Miner
import time

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    miner = Miner()
    for x in range(1, 20):
        miner.update()
        time.sleep(1)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
