# پروژه رنگ‌آمیزی نقشه ایران با CSP

این پروژه یک پیاده‌سازی از مسئله رنگ‌آمیزی نقشه ایران با استفاده از الگوریتم‌های حل مسئله محدودیت (Constraint Satisfaction Problem) است. در این پروژه، هر استان ایران باید با یکی از رنگ‌های مجاز رنگ‌آمیزی شود به طوری که هیچ دو استان همسایه‌ای رنگ یکسان نداشته باشند.

## ویژگی‌های پروژه

- پیاده‌سازی کامل الگوریتم Backtracking با Forward Checking
- استفاده از استراتژی MRV (Minimum Remaining Values) برای انتخاب متغیر
- استفاده از استراتژی Degree Heuristic برای بهبود کارایی
- پیاده‌سازی الگوریتم AC-3 برای سازگاری قوس‌ها
- نمایش گرافیکی نقشه ایران با استفاده از networkx و matplotlib
- گزارش آماری از تعداد بازگشت‌ها و تخصیص‌های موفق/ناموفق
- امکان تست با تعداد رنگ‌های مختلف

## ساختار پروژه

```
iran_map_coloring/
├── src/
│   ├── __init__.py
│   ├── csp_solver.py     # پیاده‌سازی الگوریتم‌های CSP
│   ├── map_data.py       # داده‌های نقشه ایران (استان‌ها و همسایگی‌ها)
│   └── visualization.py  # کد نمایش گرافیکی نقشه
├── main.py               # فایل اصلی اجرای برنامه
└── requirements.txt      # کتابخانه‌های مورد نیاز
```


```mermaid
flowchart TB
    %% تعریف استایل‌ها
    classDef dataClass fill:#f9f,stroke:#333,stroke-width:2px
    classDef algorithmClass fill:#bbf,stroke:#333,stroke-width:2px
    classDef visualClass fill:#bfb,stroke:#333,stroke-width:2px
    classDef mainClass fill:#fbb,stroke:#333,stroke-width:2px
    classDef resultClass fill:#ff9,stroke:#333,stroke-width:2px

    main["main.py (فایل اصلی اجرای برنامه)"]
    mapData["map_data.py (داده‌های نقشه ایران)"]
    cspSolver["csp_solver.py (پیاده‌سازی الگوریتم‌های CSP)"]
    visualization["visualization.py (نمایش گرافیکی نقشه)"]

    %% داده‌های اصلی
    provinces["PROVINCES (لیست استان‌های ایران)"]
    neighbors["NEIGHBORS (همسایگی استان‌ها)"]
    colors["COLORS\n(رنگ‌های مجاز)"]

    %% الگوریتم‌های CSP
    mapColoringCSP["MapColoringCSP (کلاس اصلی حل مسئله)"]
    backtracking["Backtracking (الگوریتم جستجوی پسگرد)"]
    forwardChecking["Forward Checking (بررسی محدودیت‌های آینده)"]
    mrv["MRV (انتخاب متغیر با کمترین مقادیر باقیمانده)"]
    degreeHeuristic["Degree Heuristic (انتخاب متغیر با بیشترین محدودیت)"]
    ac3["AC-3\n(الگوریتم سازگاری قوس‌ها)"]

    %% نمایش گرافیکی
    mapVisualizer["MapVisualizer (کلاس نمایش گرافیکی نقشه)"]
    createGraph["_create_graph (ایجاد گراف از استان‌ها و همسایگی‌ها)"]
    visualize["visualize (نمایش نقشه رنگ‌آمیزی شده)"]

    %% نتایج
    solution["Solution (راه حل نهایی رنگ‌آمیزی)"]
    statistics["Statistics (آمار اجرای الگوریتم)"]
    mapImage["Map Image (تصویر نقشه رنگ‌آمیزی شده)"]

    %% ارتباطات
    mapData --> |"استخراج داده‌ها"| provinces
    mapData --> |"استخراج داده‌ها"| neighbors
    mapData --> |"استخراج داده‌ها"| colors

    main --> |"دریافت داده‌ها"| provinces
    main --> |"دریافت داده‌ها"| neighbors
    main --> |"دریافت داده‌ها"| colors

    main --> |"ایجاد نمونه"| mapColoringCSP
    provinces --> |"متغیرها"| mapColoringCSP
    neighbors --> |"محدودیت‌ها"| mapColoringCSP
    colors --> |"دامنه مقادیر"| mapColoringCSP

    mapColoringCSP --> |"استفاده از"| ac3
    mapColoringCSP --> |"استفاده از"| backtracking
    backtracking --> |"استفاده از"| mrv
    backtracking --> |"استفاده از"| degreeHeuristic
    backtracking --> |"استفاده از"| forwardChecking

    mapColoringCSP --> |"تولید"| solution
    mapColoringCSP --> |"تولید"| statistics

    main --> |"دریافت"| solution
    main --> |"دریافت"| statistics

    main --> |"ایجاد نمونه"| mapVisualizer
    provinces --> |"استان‌ها"| mapVisualizer
    neighbors --> |"همسایگی‌ها"| mapVisualizer

    mapVisualizer --> |"استفاده از"| createGraph
    mapVisualizer --> |"استفاده از"| visualize
    solution --> |"ورودی"| visualize

    visualize --> |"تولید"| mapImage

    %% اعمال استایل‌ها به صورت جداگانه
    class main mainClass
    class mapData,provinces,neighbors,colors dataClass
    class cspSolver,mapColoringCSP,backtracking,forwardChecking,mrv,degreeHeuristic,ac3 algorithmClass
    class visualization,mapVisualizer,createGraph,visualize visualClass
    class solution,statistics,mapImage resultClass
```



## نیازمندی‌ها

برای اجرای این پروژه، به کتابخانه‌های زیر نیاز دارید:

```
numpy
matplotlib
networkx
```

می‌توانید با دستور زیر این کتابخانه‌ها را نصب کنید:

```bash
pip install -r requirements.txt
```

## نحوه اجرا

برای اجرای برنامه، دستور زیر را در ترمینال وارد کنید:

```bash
python main.py
```

### پارامترهای اختیاری

- `--colors`: تعداد رنگ‌های مورد استفاده (پیش‌فرض: 4)
- `--save`: مسیر ذخیره تصویر خروجی
- `--no-visualization`: عدم نمایش گرافیکی

مثال:

```bash
python main.py --colors 3 --save map.png
```

## خروجی مورد انتظار

پس از اجرای برنامه، خروجی زیر نمایش داده می‌شود:

1. لیست استان‌ها و رنگ تخصیص داده شده به هر استان
2. آمار اجرای الگوریتم شامل:
   - تعداد بازگشت‌ها
   - تعداد تخصیص‌ها
   - تعداد شکست‌ها
   - زمان اجرا
3. نمایش گرافیکی نقشه رنگ‌آمیزی شده

## نکات پیاده‌سازی

- کد با توضیحات فارسی مستندسازی شده است
- از بهترین شیوه‌های برنامه‌نویسی Python پیروی شده است
- الگوریتم‌های بهینه‌سازی شده برای حل سریع مسئله استفاده شده است
- مدیریت خطاها به درستی انجام شده است

## مثال خروجی گرافیکی

پس از اجرای برنامه، یک نمایش گرافیکی از نقشه ایران با رنگ‌آمیزی استان‌ها نمایش داده می‌شود. هر استان با یک رنگ متفاوت از همسایگانش رنگ‌آمیزی شده است.