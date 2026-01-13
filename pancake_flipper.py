#!/usr/bin/env python3
"""
6-Axis Robot Arm Pancake Flipper
Bu kod bir 6 eksenli robot kolun pancake çevirme işlemini gerçekleştirir.
"""

import numpy as np
import time
from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class JointAngles:
    """Robot eklem açıları (radyan)"""
    j1: float  # Base rotation
    j2: float  # Shoulder
    j3: float  # Elbow
    j4: float  # Wrist roll
    j5: float  # Wrist pitch
    j6: float  # Wrist yaw
    
    def to_list(self) -> List[float]:
        return [self.j1, self.j2, self.j3, self.j4, self.j5, self.j6]


@dataclass
class CartesianPose:
    """Kartezyen konum ve yönelim"""
    x: float  # mm
    y: float  # mm
    z: float  # mm
    rx: float  # radyan (roll)
    ry: float  # radyan (pitch)
    rz: float  # radyan (yaw)


class RobotArm:
    """6 eksenli robot kol sınıfı"""
    
    def __init__(self):
        self.current_joints = JointAngles(0, 0, 0, 0, 0, 0)
        self.spatula_offset = 200  # Spatula uzunluğu (mm)
        
    def move_to_joints(self, target: JointAngles, speed: float = 0.5):
        """Eklem açılarına hareket et"""
        print(f"Moving to joint angles: {target.to_list()}")
        # Gerçek robot kontrol kodu burada olurdu
        time.sleep(1.0 / speed)
        self.current_joints = target
        
    def move_linear(self, target: CartesianPose, speed: float = 100):
        """Doğrusal hareket (mm/s)"""
        print(f"Linear move to: ({target.x}, {target.y}, {target.z})")
        # IK (Inverse Kinematics) burada hesaplanır
        time.sleep(1.0)
        
    def open_gripper(self):
        """Gripper'ı aç (spatula için kullanılmıyor)"""
        print("Gripper opened")
        
    def close_gripper(self):
        """Gripper'ı kapat"""
        print("Gripper closed")


class PancakeFlipper:
    """Pancake çevirme işlemini yöneten sınıf"""
    
    def __init__(self, robot: RobotArm):
        self.robot = robot
        
        # Çalışma alanı konumları (mm)
        self.pancake_position = CartesianPose(
            x=400, y=0, z=50,  # Tava üzerinde
            rx=0, ry=np.pi, rz=0  # Spatula aşağı bakıyor
        )
        
        self.home_position = JointAngles(
            j1=0, j2=-np.pi/6, j3=np.pi/3,
            j4=0, j5=np.pi/6, j6=0
        )
        
        self.approach_height = 100  # Pancake'in üstünde (mm)
        self.flip_height = 150  # Flip hareketi yüksekliği (mm)
        
    def go_home(self):
        """Home pozisyonuna git"""
        print("\n=== Going to HOME position ===")
        self.robot.move_to_joints(self.home_position)
        
    def approach_pancake(self):
        """Pancake'e yaklaş"""
        print("\n=== Approaching pancake ===")
        
        # Önce üstten yaklaş
        approach_pose = CartesianPose(
            x=self.pancake_position.x,
            y=self.pancake_position.y,
            z=self.pancake_position.z + self.approach_height,
            rx=0, ry=np.pi, rz=0
        )
        self.robot.move_linear(approach_pose, speed=150)
        
        # Yavaşça aşağı in
        insert_pose = CartesianPose(
            x=self.pancake_position.x,
            y=self.pancake_position.y,
            z=self.pancake_position.z + 5,  # Pancake'in hemen altına
            rx=0, ry=np.pi, rz=0
        )
        self.robot.move_linear(insert_pose, speed=50)
        
    def flip_pancake(self):
        """Pancake'i çevir"""
        print("\n=== Flipping pancake ===")
        
        # 1. Spatula'yı pancake'in altına sok
        print("Step 1: Sliding spatula under pancake...")
        slide_pose = CartesianPose(
            x=self.pancake_position.x + 80,  # 80mm ileri
            y=self.pancake_position.y,
            z=self.pancake_position.z + 5,
            rx=0, ry=np.pi, rz=0
        )
        self.robot.move_linear(slide_pose, speed=80)
        time.sleep(0.5)
        
        # 2. Yukarı kaldır
        print("Step 2: Lifting pancake...")
        lift_pose = CartesianPose(
            x=slide_pose.x,
            y=slide_pose.y,
            z=self.pancake_position.z + self.flip_height,
            rx=0, ry=np.pi, rz=0
        )
        self.robot.move_linear(lift_pose, speed=120)
        time.sleep(0.3)
        
        # 3. Flip hareketi (180 derece döndür)
        print("Step 3: Flipping motion...")
        flip_pose = CartesianPose(
            x=lift_pose.x,
            y=lift_pose.y,
            z=lift_pose.z,
            rx=0, ry=np.pi, rz=np.pi  # 180 derece dönüş
        )
        self.robot.move_linear(flip_pose, speed=200)
        time.sleep(0.2)
        
        # 4. Pancake'i geri bırak
        print("Step 4: Placing pancake back...")
        place_pose = CartesianPose(
            x=self.pancake_position.x,
            y=self.pancake_position.y,
            z=self.pancake_position.z + 10,
            rx=0, ry=np.pi, rz=np.pi
        )
        self.robot.move_linear(place_pose, speed=100)
        time.sleep(0.3)
        
        # 5. Spatula'yı çek
        print("Step 5: Withdrawing spatula...")
        withdraw_pose = CartesianPose(
            x=place_pose.x - 100,
            y=place_pose.y,
            z=place_pose.z + 30,
            rx=0, ry=np.pi, rz=0
        )
        self.robot.move_linear(withdraw_pose, speed=150)
        
    def execute_flip_sequence(self):
        """Tam pancake flip sekansını çalıştır"""
        print("\n" + "="*50)
        print("STARTING PANCAKE FLIP SEQUENCE")
        print("="*50)
        
        try:
            # 1. Home pozisyonuna git
            self.go_home()
            time.sleep(1)
            
            # 2. Pancake'e yaklaş
            self.approach_pancake()
            time.sleep(0.5)
            
            # 3. Flip işlemini gerçekleştir
            self.flip_pancake()
            time.sleep(0.5)
            
            # 4. Home'a dön
            self.go_home()
            
            print("\n" + "="*50)
            print("PANCAKE FLIP COMPLETED SUCCESSFULLY! 🥞")
            print("="*50)
            
        except Exception as e:
            print(f"\n❌ ERROR during flip sequence: {e}")
            print("Returning to home position...")
            self.go_home()


def main():
    """Ana program"""
    # Robot ve flipper'ı başlat
    robot = RobotArm()
    flipper = PancakeFlipper(robot)
    
    # Flip sekansını çalıştır
    flipper.execute_flip_sequence()
    
    print("\n✅ Program completed!")


if __name__ == "__main__":
    main()