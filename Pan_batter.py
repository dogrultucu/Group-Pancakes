import time

class PancakeRobot:
    def __init__(self, name):
        self.name = name

    def squeeze_batter(self, instruction, squeeze_time):
        print(f"Instruction: {instruction}")
        print("Squeezing batter...")

        start_time = time.time()

        # squeeze until time limit is reached
        while time.time() - start_time < squeeze_time:
            print("Batter flowing...")
            time.sleep(1)

        # pause after time limit
        self.pause()

    def pause(self):
        print("Time limit reached.")
        print("Pausing squeeze.")
        print("Batter flow stopped.")


# create robot object
robot = PancakeRobot("McFlippy")

# give instruction as STRING
instruction = "Squeeze pancake batter to form a round Scottish pancake"

# squeeze for 5 seconds
robot.squeeze_batter(instruction, squeeze_time=5)
