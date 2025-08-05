#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
温度转换程序测试脚本
"""

from temperature_converter import celsius_to_fahrenheit, fahrenheit_to_celsius

def test_conversions():
    """
    测试温度转换函数
    """
    print("测试温度转换函数...")
    
    # 测试一些已知的转换值
    test_cases = [
        # (摄氏度, 华氏度)
        (0, 32),      # 水的冰点
        (100, 212),   # 水的沸点
        (37, 98.6),   # 人体正常体温
        (-40, -40),   # 两个温度标度的交点
        (25, 77),     # 室温
    ]
    
    print("\n摄氏度 → 华氏度转换测试:")
    for celsius, expected_fahrenheit in test_cases:
        result = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C → {result:.1f}°F (期望: {expected_fahrenheit}°F)")
        assert abs(result - expected_fahrenheit) < 0.1, f"转换错误: {celsius}°C"
    
    print("\n华氏度 → 摄氏度转换测试:")
    for expected_celsius, fahrenheit in test_cases:
        result = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F → {result:.1f}°C (期望: {expected_celsius}°C)")
        assert abs(result - expected_celsius) < 0.1, f"转换错误: {fahrenheit}°F"
    
    print("\n✅ 所有测试通过！转换函数工作正常。")

if __name__ == "__main__":
    test_conversions()