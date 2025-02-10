import os
import time
import keyboard
from Stack import *  # นำเข้า Stack และ _StackNode จาก stack.py

class maze:
    def __init__(self) -> None:
        self.maze = [
                    ["X", "X", "X", "X", " ", "X", "X"],
                    ["X", " ", "X", "X", " ", " ", "X"],
                    ["X", " ", " ", " ", "X", " ", "X"],
                    ["X", " ", "X", " ", "X", " ", "X"],
                    ["X", " ", "X", " ", " ", " ", "X"],
                    ["X", " ", "X", "X", "X", "X", "X"],
                    ]
        self.ply = pos(5, 1)  # ตำแหน่งเริ่มต้น
        self.end = pos(0, 4)  # ตำแหน่งทางออก
        self.maze[self.ply.y][self.ply.x] = "P"  # ตั้งตัวละครที่จุดเริ่มต้น
        self.maze[self.end.y][self.end.x] = "E"  # ตั้งทางออก

    def isInBound(self, y, x):
        if 0 <= y < len(self.maze) and 0 <= x < len(self.maze[0]):
            return True
        return False

    def print(self):
        os.system("cls")  
        for row in self.maze:
            print(" ".join(row))
        print("\n")

    def move(self, current_pos, direction):
        # ทิศทางการเดิน
        directions = {
            "up": (-1, 0),
            "down": (1, 0),
            "left": (0, -1),
            "right": (0, 1)
        }
        dy, dx = directions[direction]
        next_pos = pos(current_pos.y + dy, current_pos.x + dx)
        if self.isInBound(next_pos.y, next_pos.x) and self.maze[next_pos.y][next_pos.x] not in ["X", "Z"]:
            return next_pos
        return None

    def brute_force(self):
        stack = Stack()
        stack.push(self.ply)
        visited = set()

        while not stack.isEmpty():
            # ตรวจสอบการกดปุ่ม "q" เพื่อออกจากโปรแกรม
            if keyboard.is_pressed("q"):
               print("Quit Program")
               break

            current_pos = stack.peek()

            # ถ้าถึงตำแหน่งทางออก
            if current_pos.y == self.end.y and current_pos.x == self.end.x:
                self.maze[current_pos.y][current_pos.x] = "P"  # ทำเครื่องหมายที่ทางออก
                self.print()
                print(">>>>> Congraturation!!!ๆ <<<<<")
                return True

            visited.add((current_pos.y, current_pos.x))
            self.maze[current_pos.y][current_pos.x] = "Z"  # ทำเครื่องหมายตำแหน่งที่เดินผ่าน

            # ลองเดินในทุกทิศทาง
            for direction in ["up", "down", "left", "right"]:
                next_pos = self.move(current_pos, direction)
                if next_pos and (next_pos.y, next_pos.x) not in visited:
                    self.maze[next_pos.y][next_pos.x] = "P"  # ทำเครื่องหมายตำแหน่งใหม่
                    stack.push(next_pos)  # เพิ่มตำแหน่งใหม่ลงใน Stack
                    self.print()
                    time.sleep(0.25)  # หน่วงเวลาให้เห็นการเคลื่อนที่
                    break
            else:
                # ถ้าไม่มีทิศทางที่เดินได้ ให้ย้อนกลับ
                stack.pop()

        print("No path to the exit!")
        return False


class pos:
    def __init__(self, y, x) -> None:
        self.y = y
        self.x = x


# ------------------------ #
# ===== MAIN PROGRAM ===== #
# ------------------------ #

m = maze()
m.print()

# เริ่มต้นการหาทางออกด้วย Brute Force
m.brute_force()