# -*- coding: utf-8 -*-

import time
import argparse
from src.csp_solver import MapColoringCSP
from src.map_data import PROVINCES, NEIGHBORS, COLORS
from src.visualization import MapVisualizer

def main():
    # تنظیم پارامترهای ورودی
    parser = argparse.ArgumentParser(description='رنگ‌آمیزی نقشه ایران با استفاده از CSP')
    parser.add_argument('--colors', type=int, default=4, help='تعداد رنگ‌های مورد استفاده')
    parser.add_argument('--save', type=str, help='مسیر ذخیره تصویر خروجی')
    parser.add_argument('--no-visualization', action='store_true', help='عدم نمایش گرافیکی')
    args = parser.parse_args()
    
    # محدود کردن تعداد رنگ‌ها
    used_colors = COLORS[:args.colors]
    print(f"استفاده از {args.colors} رنگ: {', '.join(used_colors)}")
    
    # تعریف دامنه برای هر استان
    domains = {province: used_colors.copy() for province in PROVINCES}
    
    # ایجاد نمونه از حل‌کننده CSP
    problem = MapColoringCSP(PROVINCES, domains, NEIGHBORS)
    
    # اندازه‌گیری زمان اجرا
    start_time = time.time()
    
    # اجرای الگوریتم
    solution = problem.solve()
    
    # محاسبه زمان اجرا
    execution_time = time.time() - start_time
    
    if solution:
        print("\nراه حل یافت شد:")
        for province, color in sorted(solution.items()):
            print(f"{province}: {color}")
        
        # نمایش آمار اجرا
        stats = problem.get_statistics()
        print(f"\nآمار اجرا:")
        print(f"تعداد بازگشت‌ها: {stats['backtrack_count']}")
        print(f"تعداد تخصیص‌ها: {stats['assignment_count']}")
        print(f"تعداد شکست‌ها: {stats['failure_count']}")
        print(f"زمان اجرا: {execution_time:.4f} ثانیه")
        
        # نمایش گرافیکی نتیجه
        if not args.no_visualization:
            visualizer = MapVisualizer(PROVINCES, NEIGHBORS)
            visualizer.visualize(solution, args.save)
    else:
        print("هیچ راه حلی یافت نشد!")
        print(f"\nآمار اجرا:")
        stats = problem.get_statistics()
        print(f"تعداد بازگشت‌ها: {stats['backtrack_count']}")
        print(f"تعداد تخصیص‌ها: {stats['assignment_count']}")
        print(f"تعداد شکست‌ها: {stats['failure_count']}")
        print(f"زمان اجرا: {execution_time:.4f} ثانیه")

if __name__ == "__main__":
    main()
