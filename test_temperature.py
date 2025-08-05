#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
温度转换程序测试脚本
"""

from temperature_converter import celsius_to_fahrenheit, fahrenheit_to_celsius

def test_conversions():
    """测试温度转换功能"""
    print("测试温度转换功能:")
    print("=" * 40)
    
    # 测试摄氏度转华氏度
    test_cases_c_to_f = [
        (0, 32),      # 水的冰点
        (100, 212),   # 水的沸点
        (37, 98.6),   # 人体体温
        (25, 77),     # 室温
        (-40, -40),   # 摄氏度和华氏度相等的点
    ]
    
    print("摄氏度转华氏度测试:")
    for celsius, expected_fahrenheit in test_cases_c_to_f:
        result = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C = {result:.1f}°F (期望: {expected_fahrenheit}°F)")
    
    print("\n华氏度转摄氏度测试:")
    # 测试华氏度转摄氏度
    test_cases_f_to_c = [
        (32, 0),      # 水的冰点
        (212, 100),   # 水的沸点
        (98.6, 37),   # 人体体温
        (77, 25),     # 室温
        (-40, -40),   # 摄氏度和华氏度相等的点
    ]
    
    for fahrenheit, expected_celsius in test_cases_f_to_c:
        result = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F = {result:.1f}°C (期望: {expected_celsius}°C)")
    
    print("\n所有测试完成！")

if __name__ == "__main__":
    test_conversions()