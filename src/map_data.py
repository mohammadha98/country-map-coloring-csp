
PROVINCES = [
    'Tehran', 'Alborz', 'Qazvin', 'Mazandaran', 'Gilan', 'Ardabil',
    'East Azerbaijan', 'West Azerbaijan', 'Zanjan', 'Kurdistan',
    'Kermanshah', 'Hamadan', 'Markazi', 'Qom', 'Esfahan', 'Yazd',
    'Fars', 'Bushehr', 'Hormozgan', 'Kerman', 'Sistan and Baluchestan',
    'South Khorasan', 'Razavi Khorasan', 'North Khorasan', 'Semnan',
    'Golestan', 'Lorestan', 'Ilam', 'Khuzestan', 'Kohgiluyeh and Boyer-Ahmad',
    'Chaharmahal and Bakhtiari'
]


NEIGHBORS = {
    'Tehran': ['Alborz', 'Qazvin', 'Mazandaran', 'Semnan', 'Qom', 'Markazi'],
    'Alborz': ['Tehran', 'Qazvin', 'Markazi', 'Mazandaran'],
    'Qazvin': ['Gilan', 'Mazandaran', 'Alborz', 'Tehran', 'Markazi', 'Hamadan', 'Zanjan'],
    'Mazandaran': ['Gilan', 'Qazvin', 'Alborz', 'Tehran', 'Semnan', 'Golestan'],
    'Gilan': ['Ardabil', 'Zanjan', 'Qazvin', 'Mazandaran'],
    'Ardabil': ['East Azerbaijan', 'Zanjan', 'Gilan'],
    'East Azerbaijan': ['West Azerbaijan', 'Zanjan', 'Ardabil'],
    'West Azerbaijan': ['East Azerbaijan', 'Zanjan', 'Kurdistan'],
    'Zanjan': ['West Azerbaijan', 'East Azerbaijan', 'Ardabil', 'Gilan', 'Qazvin', 'Hamadan', 'Kurdistan'],
    'Kurdistan': ['West Azerbaijan', 'Zanjan', 'Hamadan', 'Kermanshah'],
    'Kermanshah': ['Kurdistan', 'Hamadan', 'Lorestan', 'Ilam'],
    'Hamadan': ['Kurdistan', 'Zanjan', 'Qazvin', 'Markazi', 'Lorestan', 'Kermanshah'],
    'Markazi': ['Hamadan', 'Qazvin', 'Alborz', 'Tehran', 'Qom', 'Esfahan', 'Lorestan'],
    'Qom': ['Markazi', 'Tehran', 'Semnan', 'Esfahan'],
    'Esfahan': ['Qom', 'Semnan', 'South Khorasan', 'Yazd', 'Fars', 'Kohgiluyeh and Boyer-Ahmad', 'Chaharmahal and Bakhtiari', 'Lorestan', 'Markazi'],
    'Yazd': ['Esfahan', 'South Khorasan', 'Kerman', 'Fars'],
    'Fars': ['Esfahan', 'Yazd', 'Kerman', 'Hormozgan', 'Bushehr', 'Kohgiluyeh and Boyer-Ahmad'],
    'Bushehr': ['Khuzestan', 'Kohgiluyeh and Boyer-Ahmad', 'Fars', 'Hormozgan'],
    'Hormozgan': ['Bushehr', 'Fars', 'Kerman', 'Sistan and Baluchestan'],
    'Kerman': ['Yazd', 'South Khorasan', 'Sistan and Baluchestan', 'Hormozgan', 'Fars'],
    'Sistan and Baluchestan': ['South Khorasan', 'Kerman', 'Hormozgan'],
    'South Khorasan': ['Razavi Khorasan', 'Semnan', 'Esfahan', 'Yazd', 'Kerman', 'Sistan and Baluchestan'],
    'Razavi Khorasan': ['North Khorasan', 'Semnan', 'South Khorasan'],
    'North Khorasan': ['Golestan', 'Semnan', 'Razavi Khorasan'],
    'Semnan': ['Golestan', 'Mazandaran', 'Tehran', 'Qom', 'Esfahan', 'South Khorasan', 'Razavi Khorasan', 'North Khorasan'],
    'Golestan': ['North Khorasan', 'Semnan', 'Mazandaran'],
    'Lorestan': ['Kermanshah', 'Hamadan', 'Markazi', 'Esfahan', 'Chaharmahal and Bakhtiari', 'Khuzestan', 'Ilam'],
    'Ilam': ['Kermanshah', 'Lorestan', 'Khuzestan'],
    'Khuzestan': ['Ilam', 'Lorestan', 'Chaharmahal and Bakhtiari', 'Kohgiluyeh and Boyer-Ahmad', 'Bushehr'],
    'Kohgiluyeh and Boyer-Ahmad': ['Khuzestan', 'Chaharmahal and Bakhtiari', 'Esfahan', 'Fars', 'Bushehr'],
    'Chaharmahal and Bakhtiari': ['Khuzestan', 'Lorestan', 'Esfahan', 'Kohgiluyeh and Boyer-Ahmad']
}


COLORS = ['قرمز', 'آبی', 'سبز', 'زرد']
