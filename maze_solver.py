import turtle
import time

# อ่านไฟล์และแปลงเป็นโครงสร้างเขาวงกต
def read_maze_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    maze = []
    for line in lines:
        row = [1 if char == '+' else 0 for char in line.strip()]
        maze.append(row)

    return maze

# ตั้งค่าหน้าจอ
def setup_window():
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("Maze Solver with Turtle")
    screen.setup(700, 700)
    return screen

# ตัวแสดงผลของกำแพง, เส้นทาง, จุดเริ่มต้น และจุดสิ้นสุด
class MazeTurtle(turtle.Turtle):
    def __init__(self, color, shape="turtle"):
        super().__init__()
        self.shape(shape)  # ใช้รูปร่างที่ต้องการ (default: "turtle")
        self.color(color)
        self.penup()
        self.speed(0)

def draw_maze(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            screen_x = -300 + (x * 24)
            screen_y = 300 - (y * 24)
            if grid[y][x] == 1:  # กำแพง
                wall.goto(screen_x, screen_y)
                wall.stamp()

def solve_maze(x, y):
    if (x, y) == goal_pos:  # พบทางออก
        print("Maze solved!")
        return True
    if (x, y) in visited or maze[y][x] == 1:
        return False

    visited.add((x, y))
    path_marker.goto(-300 + (x * 24), 300 - (y * 24))
    path_marker.color("green")  # สีเขียวเมื่อเดินไปข้างหน้า
    path_marker.stamp()

    # ลองไปในแต่ละทิศทาง (ขวา, ซ้าย, ลง, ขึ้น)
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        if solve_maze(x + dx, y + dy):
            return True

    # สีแดงเมื่อถอยกลับ (backtrack)
    visited.remove((x, y))
    path_marker.goto(-300 + (x * 24), 300 - (y * 24))
    path_marker.color("red")  # สีแดงเมื่อถอยกลับ
    path_marker.stamp()
    return False

# อ่านเขาวงกตจากไฟล์
maze = read_maze_from_file("maze.txt")

# ตรวจสอบว่ามีข้อมูลในไฟล์หรือไม่
if not maze:
    print("Error: Maze file is empty or invalid!")
    exit()

# ค้นหาจุดเริ่มต้นและจุดสิ้นสุด (กำหนดเอง)
start_pos = (1, 1)  # สามารถปรับค่าได้
goal_pos = (len(maze[0]) - 2, len(maze) - 2)  # กำหนดจุดออกแบบง่ายๆ

# สร้างหน้าต่าง
screen = setup_window()

# กำหนดสัญลักษณ์ของวัตถุ
wall = MazeTurtle("black", shape="square")  # กำแพงเป็นรูปสี่เหลี่ยม
path_marker = MazeTurtle("green")  # เส้นทางเป็นรูปเต่า

# วาดเขาวงกต
visited = set()
draw_maze(maze)

# แก้ปัญหาเขาวงกต
if start_pos:
    solve_maze(*start_pos)

turtle.done()